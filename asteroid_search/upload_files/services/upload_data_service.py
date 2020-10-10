from upload_files.models import UploadFiles
from asteroids.models import AsteroidRegistration, Observatories, Devices
import os
from django.conf import settings
from datetime import datetime


class UploadDataService(object):
    '''
    Service to save file information in the database'''
    def get_observatory_object(self, observatory_code):
        observatory_object = Observatories.objects.filter(code=observatory_code)
        return Observatories.objects.create(code=observatory_code) if not observatory_object.exists() else observatory_object[0]

    def get_device_object(self, device_code, resolution, observatory_object):
        device_object = Devices.objects.filter(code=device_code, resolution=resolution, observatory=observatory_object)
        return Devices.objects.create(code=device_code, resolution=resolution, observatory=observatory_object) if not device_object.exists() else device_object[0]

    def set_height_width_asteroid(self, matrix, resolution):
        '''
        Get the size of asteroid from the matrix'''
        resolution_array = resolution.split('x')
        width = int(resolution_array[0])
        height = int(resolution_array[1])
        index = 0
        height_asteroid = 0
        width_asteroid = 0
        for i in range(0, height):
            row = matrix[index:width+index]
            if '1' in row:
                height_asteroid += 1
                if row.count('1') > width_asteroid:
                    width_asteroid = row.count('1')
            index += width
        return height_asteroid, width_asteroid

    def upload_data(self, lines):
        for line in lines:
            line_array = line.split()
            date_time_obj = datetime.strptime(line_array[0] + ' ' + line_array[1], '%Y-%m-%d %H:%M:%S')

            observatory_object = self.get_observatory_object(line_array[2])
            device_object = self.get_device_object(line_array[3], line_array[4], observatory_object)
            height, width = self.set_height_width_asteroid(line_array[5], line_array[4])
            AsteroidRegistration.objects.create(
                date=date_time_obj,
                device=device_object,
                height=height,
                width=width
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
