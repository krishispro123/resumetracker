from rest_framework import serializers
from .models import Person, Resume





class PersonSerializer(serializers.ModelSerializer) :

    name = serializers.CharField()
    age = serializers.IntegerField(required = False)
    password = serializers.CharField(write_only = True)
    address = serializers.CharField(required = False)
    email = serializers.EmailField()


    class Meta :

        model = Person

        fields = ['name','age','password','address','email']


        
        def validate(self, data) :

            if Person.objects.filter(email = data['email']).exists :

                raise serializers.ValidationError("email already exists")
            


class FileUploadSerializer(serializers.ModelSerializer) :

    person = serializers.CharField(required = False)
    skills = serializers.CharField(required = False)
    qualifications = serializers.CharField(required = False)
    address = serializers.CharField(required = False)
    file = serializers.FileField()





    class Meta :

        model = Resume
        fields = ['person','skills','qualifications','address','file']







    



    

    









