from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view()
# def helloword(request):
#     return Response({'msg':'Hello World'})
@api_view(['POST','GET'])
def helloword(request):
    if request.method=="POST":
        return Response({'msg':'This is Post', 'data':request.data})
    if request.method=="GET":
        return Response({'msg':'This is Get'})
    