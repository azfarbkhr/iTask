from django.shortcuts import render
from django.http import HttpResponse
from .forms import pushupLogsForm
from .models import pushup_logs
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime, timedelta
import pandas as pd 

def index(request):
    if request.method == 'POST':
        form = pushupLogsForm(request.POST)
        if form.is_valid():
            pushup_log = pushup_logs.objects.create(exercize_date=form.cleaned_data['exercize_date'], pushup_count=form.cleaned_data['pushup_count'])

    else:
        form = pushupLogsForm()

    context = {
        'form': form
    }
    
    return render(request, 'habbit_tracking/index.html', context)

def population_chart(request):

    last_month = datetime.now() - timedelta(days=30)

    queryset = pushup_logs.objects.filter(exercize_date__gt=last_month).values('exercize_date').annotate(pushup_count=Sum('pushup_count')).order_by('exercize_date')

    dates_list = pd.date_range(start=last_month, end = datetime.today()).to_pydatetime().tolist()
    data_list = [0] * len(dates_list)

    labels = []
    
    for index, date_label in enumerate(dates_list):
        labels.append(date_label.strftime('%d-%b-%Y'))

        for item in queryset:
            if date_label.date() == item['exercize_date']:
                data_list[index] += item['pushup_count']

    return JsonResponse(data={'labels': labels, 'data': data_list})
