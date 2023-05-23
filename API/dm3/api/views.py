
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def StudentApi(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializ=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializ.data)
            return HttpResponse(json_data,content_type='application/json')
        else:
            stu=Student.objects.all()
            serializ=StudentSerializer(stu, many=True)
            json_data=JSONRenderer().render(serializ.data)
            return HttpResponse(json_data,content_type='application/json')
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializ=StudentSerializer(data=pythondata)
        if serializ.is_valid():
            serializ.save()
            res={'mes':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data=JSONRenderer().render(serializ.errors)
            return HttpResponse(json_data,content_type='application/json')
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializ=StudentSerializer(stu, data=pythondata, partial=True)
        if serializ.is_valid():
            serializ.save()
            res={'mes':'data Update'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data=JSONRenderer().render(serializ.errors)
            return HttpResponse(json_data,content_type='application/json')
    if request.method=="DELETE":
        json_data=request.body
        Stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(Stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'mess':'Data delete'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)

    
