from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class Student_info(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    image = models.ImageField(upload_to="student_image", null=False, blank=False)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
