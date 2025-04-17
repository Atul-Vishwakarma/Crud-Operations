from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    experience = models.IntegerField(default=0)
    qualification = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=150, blank=True)
    current_company = models.CharField(max_length=150, blank=True)
    notice_period = models.IntegerField(default=0)
    expected_salary = models.CharField(max_length=50, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.name
