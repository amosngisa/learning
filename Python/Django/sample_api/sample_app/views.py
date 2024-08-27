from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404  

# Create your views here.

class StudentView(APIView):

    def get(self, request, *args, **kwargs):
        result = Students.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            student = Students.objects.get(id=kwargs['id'])
        except Students.DoesNotExist:
            return Response({"status": "error", "data": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            student = Students.objects.get(id=kwargs['id'])
        except Students.DoesNotExist:
            return Response({"status": "error", "data": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        student.delete()
        return Response({"status": "success", "data": "Student deleted"}, status=status.HTTP_200_OK)
    
 