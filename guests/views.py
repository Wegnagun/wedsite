from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import GuestAlcoMultiForm
from .models import APPROVAL_CHOICES, TRANSFER_CHOICES

def guest_answer(request):
    if request.method == 'POST':
        form = GuestAlcoMultiForm(request.POST)
        if form.is_valid():
            guest = form.save()
            send_guest_register_notification(guest)
            #return redirect('guests')
    else:
        form = GuestAlcoMultiForm()

    return render(request, 'guests/index.html', {'form': form})

def send_guest_register_notification(guest):
    """Отправляет email-уведомление о новом госте"""
    approval_map = dict(APPROVAL_CHOICES)
    transfer_map = dict(TRANSFER_CHOICES)
    approval = approval_map.get(guest.approval)
    transfer = transfer_map.get(guest.transfer)
    selected_drinks = list(guest.drinks.all())
    drinks_list = [drink.name for drink in selected_drinks] if selected_drinks else ['Не выбраны']
    html_message = render_to_string('emails/new_guest_notification.html', {
        'guest': guest,
        'approval': approval,
        'transfer': transfer,
        'drinks_list': drinks_list
    })

    text_message = render_to_string('emails/new_guest_notification.txt', {
        'guest': guest,
        'approval': approval,
        'transfer': transfer,
        'drinks_list': drinks_list
    })

    recipient_list = [
        'wegnagun@bk.ru',  # email администратора
    ]

    try:
        send_mail(
            subject=f'Новый гость: {guest.fio} дал ответ',
            message=text_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
        print(f"Уведомление отправлено гостем: {guest.fio}")
    except Exception as e:
        print(f"Ошибка отправки email: {e}")

