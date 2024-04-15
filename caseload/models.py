from django.db import models

class User(models.Model):
   user_id = models.IntegerField()
   user_name = models.CharField(max_length=30)
   user_password = models.CharField(max_length=30)

class Child(models.Model):
   id_number = models.IntegerField()
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   user = models.ForeignKey('User', on_delete=models.CASCADE)

   def __str__(self):
      return f'{self.first_name}, {self.last_name}, {self.id_number}'

class Session(models.Model):
   session_id = models.IntegerField()
   child = models.ForeignKey('Child', on_delete=models.CASCADE)
   session_date = models.DateField()
   session_time = models.TimeField()
   scheduled_week_day = models.CharField(max_length=30)
   session_attendance = models.CharField(max_length=30)


