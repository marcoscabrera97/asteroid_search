from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from upload_files.services.upload_data_service import UploadDataService


class UploadFilesAutomatically(APIView):
    upload_data_service = UploadDataService()

    def get(self, request):
        self.upload_data_service.check_files_not_upload()
        return Response({'dentro': 'ok'})