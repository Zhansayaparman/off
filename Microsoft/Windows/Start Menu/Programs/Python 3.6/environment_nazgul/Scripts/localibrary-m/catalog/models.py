from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User


class Office(models.Model):

    name = models.CharField(max_length=200, help_text="Enter a office job (e.g. Science Fiction, French Poetry etc.)")
 
    def __str__(self):

        return self.name

from django.urls import reverse

class Workers(models.Model):

    job_name = models.CharField(max_length=200)
    admin = models.ForeignKey('Admin', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Enter ")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    office = models.ManyToManyField(Office, help_text="Select a office for this job")

    def __str__(self):

        return self.job_name

    def get_absolute_url(self):

        return reverse('workers-detail', args=[str(self.id)])



import uuid

class Admin(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)


    def get_absolute_url(self):

        return reverse('admin-detail', args=[str(self.id)])

    def __str__(self):

        return '%s, %s' % (self.last_name, self.first_name)
