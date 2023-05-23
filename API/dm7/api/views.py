
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

@api_view(['GET','POST','PUT','DELETE','PATCH'])
def student_api(request, pk=None):
    if request.method=="GET":
        # id=request.data.get('id')
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu, many=True)
            return Response(serializer.data)
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PUT':
        # id= request.data.get('id')
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mes':'Complete Data Update'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        # id= request.data.get('id')
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'mes':'Data Delete'})
    if request.method=='PATCH':
        # id= request.data.get('id')
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mes':'Partial Data Update'})
        else:
            return Response(serializer.errors)




