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

class Schedule(models.Model):
   scheduled_week_day = models.CharField(max_length=30)
   session_time = models.TimeField()
   child = models.ForeignKey('Child', on_delete=models.CASCADE)

   def __str__(self):
      return f'{self.child}, {self.scheduled_week_day}, {self.session_time}'

class Session(models.Model):
   child = models.ForeignKey('Child', on_delete=models.CASCADE)
   session_date = models.DateField()
   session_attendance = models.CharField(max_length=30)


