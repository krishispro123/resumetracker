from django.db import models




class Person(models.Model) :

    name = models.TextField(max_length=60)
    email = models.EmailField(max_length=80)
    password = models.TextField(max_length=80)
    age = models.IntegerField()


class Resume(models.Model) :
    
    

    file = models.FileField(upload_to = 'upload/')
    skills = models.TextField(max_length = 200)
    qualifications = models.TextField(max_length = 200)
    address = models.TextField(max_length = 300)
    





    


    

# Create your models here.
