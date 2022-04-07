from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeletionMixin
from django.urls import reverse
from .models import Report
from .forms import ReportForm


class AllReports(ListView):
    template_name = "all_reports.html"
    model = Report
    context_object_name = 'all_reports'
    queryset = Report.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.get_full_name()
        if self.request.user.is_superuser:
            context['all_reports'] = Report.objects.all()
        else:
            context['all_reports'] = Report.objects.filter(author=self.request.user.id)
        return context


class CreateReport(CreateView):
    template_name = 'create_report.html'
    form_class = ReportForm
    success_url = '/all_reports'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_reports'] = Report.objects.all()
        context['form'] = ReportForm(initial={'author': self.request.user.username})
        context['username'] = self.request.user.username
        context['full_name'] = self.request.user.get_full_name()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditReport(UpdateView):
    template_name = 'edit_report.html'
    model = Report
    success_url = '/all_reports'
    pk_url_kwarg = 'report_id'
    form_class = ReportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReportForm(instance=Report.objects.get(pk=self.kwargs['report_id']),
                                     initial={'author': self.request.user.username})
        return context


class DeleteReport(DeleteView):
    model = Report
    pk_url_kwarg = 'report_id'
    success_url = '/all_reports'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

