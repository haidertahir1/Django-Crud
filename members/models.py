from django.db import models

from django.db import models


class Members(models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


#
#
# class Members(models.Model):
#     first_name = models.CharField(max_length=255, default='')
#     last_name = models.CharField(max_length=255, default='')
