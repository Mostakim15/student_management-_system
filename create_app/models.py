from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/default.jpg', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    department = models.CharField(choices=[
        ('---', 'Select Department'),
        ('CSE', 'Computer Science'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('BBA', 'Bachelor of Business Administration'),
        ("BA", "Bachelor of Arts"),
        ('BCOM', 'Bachelor of Commerce'),
        ('Other', 'Other'),
    ], max_length=500, default='---')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        