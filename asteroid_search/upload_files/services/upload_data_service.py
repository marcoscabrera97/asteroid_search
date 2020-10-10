from upload_files.models import UploadFiles
from asteroids.models import AsteroidRegistration, Observatories, Devices
import os
from django.conf import settings
from datetime import datetime


class UploadDataService(object):
    def get_observatory_object(self, observatory_code):
        observatory_object = Observatories.objects.filter(code=observatory_code)
        return Observatories.objects.create(code=observatory_code) if not observatory_object.exists() else observatory_object[0]

    def get_device_object(self, device_code, resolution, observatory_object):
        device_object = Devices.objects.filter(code=device_code, resolution=resolution, observatory=observatory_object)
        return Devices.objects.create(code=device_code, resolution=resolution, observatory=observatory_object) if not device_object.exists() else device_object[0]

    def upload_data(self, lines):
        for line in lines:
            line_array = line.split()
            date_time_obj = datetime.strptime(line_array[0] + ' ' + line_array[1], '%Y-%m-%d %H:%M:%S')

            observatory_object = self.get_observatory_object(line_array[2])
            device_object = self.get_device_object(line_array[3], line_array[4], observatory_object)
            AsteroidRegistration.objects.create(
                date=date_time_obj,
                device=device_object,
                matrix=line_array[5]
            )       

    def check_files_not_upload(self):
        file_json = {}
        upload_files_object = UploadFiles.objects.all()
        upload_files_path = settings.BASE_DIR + '/import_files/'
        upload_files = os.listdir(upload_files_path)
        for file_name in upload_files:
            if not UploadFiles.objects.filter(name=file_name).exists():
                file = open(upload_files_path + file_name)
                lines_file = file.readlines()
                file_json = self.upload_data(lines_file[1:])
                UploadFiles.objects.create(name=file_name)
