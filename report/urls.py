from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('make_report', views.make_report, name='make_report'),
    path('edit/<int:report_id>', views.edit_report, name='edit_report'),
    path('delete/<int:delete_id>', views.delete_report, name='delete_report'),
]
