from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import AllReports, CreateReport, EditReport, DeleteReport


urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name="login"),
    path('all_reports/', AllReports.as_view(), name='all_reports'),
    path('create_report/', CreateReport.as_view(), name='create_report'),
    path('edit_report/<int:report_id>/', EditReport.as_view(), name='edit_report'),
    path('<int:report_id>/', DeleteReport.as_view(), name='delete_report'),
    path('logout', LogoutView.as_view(), name='logout'),
]
