from .models import Record
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['doctor', 'patient', 'diagnos', 'date']
        
        widgets = {
            'doctor':TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Врач'
                }),
            'patient':TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пациент'
                }),
            'diagnos':Textarea(attrs={ 
                'class': 'form-control',
                'placeholder': 'Диагноз'
                }),
            'date':DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
                }),
        }