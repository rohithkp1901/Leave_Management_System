from django.db import models

# Create your models here.
class Student(models.Model):
    gender_option=[
        ('Male','Male'),
        ('Female','Female'),
    ]
    username = models.CharField(max_length=50,null=True, unique=True)
    password = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=100,null=True)
    department= models.CharField(max_length=100,null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=gender_option, default='Male')
    image = models.ImageField(null=True,blank=True,upload_to='images/')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=20, default='Pending')
    def __str__(self):
        return self.status
    

