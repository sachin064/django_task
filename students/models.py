from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


class Students(models.Model):
    """
    student details table
    """

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    id = models.CharField(primary_key=True, null=False, editable=False,max_length=200)
    registration_number = models.CharField(unique=True, null=False, max_length=15)
    first_name = models.CharField(null=False, unique=False, max_length=10)
    last_name = models.CharField(null=True, max_length=10)
    gender = models.CharField(null=False, max_length=10,choices=Gender.choices)
    date_of_admission = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.TimeField(auto_now=True)

    def save(self,*args,**kwargs):
        first_name = self.first_name
        last_name = self.last_name
        date_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        self.id = first_name[0]+last_name[0]+date_time
        super(Students,self).save(*args,**kwargs)












