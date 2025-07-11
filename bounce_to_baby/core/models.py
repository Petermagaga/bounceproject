from django.contrib.auth.models  import AbstractUser
from django.db import models
from datetime import date,timedelta

class User(AbstractUser):

    age=models.IntegerField(null=True,blank=True)
    location=models.CharField(max_length=100,blank=True)
    pregnacy_start_date=models.DateField(null=True,blank=True)
    profile_picture=models.ImageField(upload_to='profile_pics/',blank=True,null=True)

    @property
    def due_date(self):
        if self.pregnacy_start_date:
            return self.pregnacy_start_date + timedelta(weeks=40)
        return None
    @property
    def trimester(self):
        if not self.pregnacy_start_date:
            return None
        weeks=(date.today()-self.pregnacy_start_date).days //7
        if weeks<13:
            return "First"
        elif weeks <27:
            return "second"
        elif weeks <=40:
            return "Third"
        return "Overdue"

class JournalEntry(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mood=models.CharField(max_length=50)
    symptoms=models.TextField(blank=True)
    note=models.TextField(blank=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at} -{self.mood}"
    

class FAQ(models.Model):
    question = models.CharField(max_length=233)
    answer=models.TextField()
    topic=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.question