from django.urls import path
from core import views

urlpatterns = [
	path('certificates', views.FACListView.as_view(), name='fac-list'),
	path('system-list', views.SystemListView.as_view(), name='system-list'),
]