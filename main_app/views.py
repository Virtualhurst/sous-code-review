from django.shortcuts import render, redirect
from django.db import connection
from .models import DataRecord

def index_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM main_app_datarecord ORDER BY created_on DESC")
        rows = cursor.fetchall() 
    return render(request, 'index.html', {'rows': rows})

def create_record_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        info = request.POST.get('info')
        record = DataRecord(name=name, info=info)
        record.save()
        return redirect('index')
    return render(request, 'detail.html')

def detail_view(request, record_id):
    record = DataRecord.objects.get(id=record_id)
    return render(request, 'detail.html', {'record': record})
