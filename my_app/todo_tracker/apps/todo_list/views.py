from datetime import datetime
from calendar import HTMLCalendar

from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe

from todo_list.models import Task


def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

class CalenderView(generic.ListView):
    model = Task
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.today()
        cal = HTMLCalendar()

        html_cal = cal.formatmonth(today.year, today.month)
        context['calender'] = mark_safe(html_cal)

        return context






