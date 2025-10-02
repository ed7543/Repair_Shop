from django import forms

from RepairApp.models import Repair


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = ['user']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'class': 'datetime-local'}),
            'date': forms.DateInput(attrs={'class': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'is_open':
                "form-check-input"
