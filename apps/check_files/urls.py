from django.urls import path
from .views import CheckFilesView

urlpatterns = [
    path('', CheckFilesView.as_view(), name='check-files'),
]
