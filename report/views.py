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


    условие длины необходимо для того, чтобы не возникало проблем
    если отчёт в единственном экземляре
    надо не забыть про удаление отчётов!!!
    """

    # reports = Reports.objects.all() if request.user.is_superuser else Reports.objects.get(id=request.user.pk)
    # if len(reports) == 1:
    #     context = {"report": [reports]}
    # else:
    #     context = {"report": reports}
    # if request.user.is_superuser:
    #     reports = Reports.objects.all()
    #     context = {"reports": reports}
    # else:
    #     reports = Reports.objects.all()
    #     context = {"reports": []}
    # for r in reports:
    #     if r.author == request.user.username:
    #         context["reports"].append(r)
    #
    # return render(request, 'reports.html', context)
    reports = Reports.objects.all()
    if request.user.is_superuser:
        context = {"reports": reports}
    else:
        context = {"reports": []}
        for r in reports:
            if r.author == request.user.username:
                context["reports"].append(r)

    return render(request, 'reports.html', context)

@login_required
def make_report(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            context = {'form': ReportsForm()}
        else:
            context = {'form': ReportsForm(initial={'author': request.user.username})}
        return render(request, 'make_report.html', context)
    if request.method == 'POST':
        if request.user.is_superuser:
            reports_form = ReportsForm(request.POST)
        else:
            reports_form = ReportsForm(request.POST, initial={'author': request.user.username})
        reports_form.save()
        return HttpResponseRedirect('/reports')


@login_required
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


@login_required
def delete_report(request, delete_id):
    current_report = Reports.objects.get(id=delete_id)
    # print(current_report)
    current_report.delete()
    return HttpResponseRedirect('/reports')
