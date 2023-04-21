from django.db import models

# Create your models here.
job_types=[('Full Time','Full Time'),('Part Time','Part Time')]
class Job(models.Model):
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=job_types)
    description=models.CharField(max_length=1000)
    published_at=models.DateField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experiance=models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
