from django.shortcuts import render, redirect
from .models import Record
from .forms import RecordForm

def get_record(request):
    record = Record.objects.all()
    return render(request, 'records/delete_record.html', {'record': record})

def create_record(request):
    error = ''
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма была неверной'
            
    form = RecordForm()
    
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'records/create_record.html', data)