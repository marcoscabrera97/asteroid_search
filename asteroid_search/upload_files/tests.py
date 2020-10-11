from django.test import TestCase, Client, override_settings
from django.conf import settings
from django.urls import reverse
from asteroids.models import AsteroidRegistration
import os
class UploadFilesTestCase(TestCase):
    client = Client()
    @override_settings(IMPORT_FILES=settings.BASE_DIR + '/test_import_files/')
    def setUp(self):
        f= open(settings.IMPORT_FILES + "test_file.txt","w+")
        f.write("date    time    observatory_code    device_code device_resolution   devide_matrix\n")  
        f.write("2019-02-22 12:01:57 ob_35634 de_10354 3x7 000000100100110110000\n")
        f.write("2019-02-25 03:27:21 ob_3482734 de_00234 4x6 000000000100010001100110\n")
        f.write("2019-02-25 03:27:00 ob_3444535 de_00234 4x6 0011111111100010001100110\n")
    
    @override_settings(IMPORT_FILES=settings.BASE_DIR + '/test_import_files/')
    def tearDown(self):
        os.remove(settings.IMPORT_FILES + "test_file.txt")

    @override_settings(IMPORT_FILES=settings.BASE_DIR + '/test_import_files/')
    def test_test(self):
        response = self.client.get('/upload_files')
        count_asteroids = len(AsteroidRegistration.objects.all())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count_asteroids, 3)
