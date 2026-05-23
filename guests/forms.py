from django import forms
from django.forms import RadioSelect
from betterforms.multiform import MultiForm
from .models import Guest, Drinks


class GuestForm(forms.ModelForm):
    """ Форма для регистрации гостей. """

    class Meta:
        model = Guest
        fields = ('fio', 'approval', 'transfer', 'other',)
        widgets = {
            'approval': RadioSelect(),
            'transfer': RadioSelect()
        }

class AlcoForm(forms.Form):
    """ Форма для выбора алкоголя. """
    related_field = forms.ModelMultipleChoiceField(
        queryset=Drinks.objects.all().order_by('sort'),
        label='Что предпочитаете из алкогольных напитков? ',
        required=True,
        widget=forms.CheckboxSelectMultiple(),
    )
        


class GuestAlcoMultiForm(MultiForm):
    form_classes = {
        'guest': GuestForm,
        'alco': AlcoForm,
    }

    def save(self, commit=True):
        guest_instance = self.forms['guest'].save(commit=commit)
        alco_data = self.forms['alco'].cleaned_data['related_field']

        if commit:
            guest_instance.drinks.set(alco_data)
        
        return guest_instance

