from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
# для переправления страницы

from django.http import HttpResponseRedirect

# Create your views here.
from .forms import ReportsForm
from .models import Reports


@login_required
def home(request):
    """
    спросить про reportpage
    отображение отчётов в зависимости от прав пользователя
    условие длины необходимо для того, чтобы не возникало проблем
    если отчёт в единственном экземляре
    надо не забыть про удаление отчётов!!!
    """
    print(dir(request.user)) #методы
    print(request.user.pk)
    reports = Reports.objects.all() if request.user.is_superuser else Reports.objects.get(id=request.user.pk)
    if len(reports) == 1:
        context = {"report": [reports]}
    else:
        context = {"report": reports}
    return render(request, 'reports.html', context)


@login_required
def make_report(request):
    if request.method == 'GET':
        context = {'form': ReportsForm()}
        return render(request, 'make_report.html', context)
    if request.method == 'POST':
        reports_form = ReportsForm(request.POST)
        reports_form.save()
        return HttpResponseRedirect('/reports')


def edit_report(request, report_id):
    current_report = Reports.objects.get(id=report_id)
    if request.method == 'GET':
        current_report_form = ReportsForm(instance=current_report)
        context = {'form': current_report_form}
        return render(request, 'edit_report.html', context)
    if request.method == 'POST':
        current_report_form = ReportsForm(request.POST, instance=current_report)
        current_report_form.save()
        return HttpResponseRedirect('/reports')
