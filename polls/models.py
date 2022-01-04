import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# class History(models.Model):
#     menu_id = models.IntegerField()
#     group_name = models.CharField(max_length=50)
#     updated = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'history'


# class LopSample(models.Model):
#     date_time = models.DateTimeField(blank=True, null=True)
#     last_month = models.DateTimeField(blank=True, null=True)
#     this_month = models.DateTimeField(blank=True, null=True)
#     user_id = models.BigIntegerField(blank=True, null=True)
#     point_amt = models.IntegerField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     gender = models.CharField(max_length=7, blank=True, null=True)
#     category = models.CharField(max_length=7, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'lop_sample'


# class LopSample2(models.Model):
#     date_time = models.DateTimeField(blank=True, null=True)
#     last_month = models.DateTimeField(blank=True, null=True)
#     this_month = models.DateTimeField(blank=True, null=True)
#     user_id = models.BigIntegerField(blank=True, null=True)
#     point_amt = models.IntegerField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     gender = models.CharField(max_length=7, blank=True, null=True)
#     category = models.CharField(max_length=7, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'lop_sample_2'
        
