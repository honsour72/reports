from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserRegion, Reports
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

@login_required
def home(request):
    reports = Reports.objects.all()
    context = {"reports": reports}

    if request.user.is_superuser:
        context['user'] = 'admin'
        return render(request, 'reports.html', context)
    else:
        return HttpResponseRedirect('make_report')


def make_report(request):
    if request.method == 'GET':
        context = {'form': ReportsForm()}
        return render(request, 'make_report.html', context)
    if request.method == 'POST':
        reports_form = ReportsForm(request.POST)
        reports_form.save()
        return HttpResponseRedirect('make_report')
