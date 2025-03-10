from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import Person
from rest_framework.views import APIView
from .serializers import PersonSerializer, FileUploadSerializer
from django.core.files.storage import default_storage
import fitz



# Create your views here.

class RegisterView(APIView) :


    def post(self, request) :

        PersonSerializedData = PersonSerializer(data = request.data)

        if PersonSerializedData.is_valid() :

            return Response({
                'sucesss':'details registered successfully'
            }, status = status.HTTP_200_OK)
        

        else :

            return Response({
                'failure' : 'error registering the person'
            }, status =  status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class FileUploadView(APIView) :

    
   

    def post(self, request) :

        FileSerializer = FileUploadSerializer(data = request.data)


        if FileSerializer.is_valid() :

            resume_instance = FileSerializer.save()

            filepath = resume_instance.file.path


            try :
                with fitz.open(filepath) as Doc :

                    textContent = "\n".join([page.get_text() for page in Doc])
                    print(textContent)

                    return Response({
                        'success':textContent
                    }, status = status.HTTP_200_OK)
            



            except Exception as e:
                return Response({
                    'success':'false'
                },status = status.HTTP_500_INTERNAL_SERVER_ERROR)




            return Response({
                'success':"true"
            },status = status.HTTP_200_OK)
        




            


        else :

            return Response({
                'error':'error uploading the file'
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        
    def get(self,request) :

        return Response({
            'success':True
        },status = status.HTTP_200_OK)
        
    

















        





        

