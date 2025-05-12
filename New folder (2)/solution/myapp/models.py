from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    image1 = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name



# # models.py
# from django.db import models

# class UserProfile(models.Model):
#     name = models.CharField(max_length=100)
#     profile_image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.name
