from django.urls import path
from core import views

urlpatterns = [
	path('certificates', views.FACListView.as_view(), name='fac-list'),
	path('certificates/check', views.FACCheckView.as_view(), name='fac-check'),
	path('certificates/create', views.FACCreateView.as_view(), name='fac-create'),
	path('certificates/export', views.FACExportView.as_view(), name='fac-export'),
	path('certificates/<int:pk>/edit', views.FACEditView.as_view(), name='fac-edit'),
	path('certificates/<int:pk>/delete', views.FACDeleteView.as_view(), name='delete-fac'),
	path('certificates/<int:pk>/export', views.FACExportDetailsView.as_view(), name='fac-export'),

	path('system-list', views.SystemListView.as_view(), name='system-list'),
	path('system-list/upload', views.FACUploadView.as_view(), name='fac-upload'),
]
