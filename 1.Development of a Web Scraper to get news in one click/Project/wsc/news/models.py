from enum import unique
from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.
class AllNews(models.Model):
   
    title=models.CharField(verbose_name = 'Title', max_length=200,  default= "")
    link= models.CharField(verbose_name = 'Link',  max_length=200, default= "/")
    created_on = models.DateTimeField(auto_now =True,verbose_name='Scrupping Time')

    class Meta:
        db_table = 'AllNews'
        
    class Meta:
        ordering = ["-created_on"]
        verbose_name = 'All News'
        verbose_name_plural = 'All News'

    def __str__(self):
        return self.title