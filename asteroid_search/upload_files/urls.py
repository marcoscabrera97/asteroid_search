from django.urls import path
from upload_files.views import UploadFilesAutomatically

urlpatterns = [
    path('', UploadFilesAutomatically.as_view()),
]
