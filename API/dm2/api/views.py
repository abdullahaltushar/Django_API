
import io
from rest_framework.parsers import JSONParser
from .models import Student
from api.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_api(request):
    
    if request.method=='GET':
        json_data=request.body
        if request is None:
            print("h")
        print(json_data)
        stream=io.BytesIO(json_data)
        print("hello")
        if stream is not None:
            print("hello2")
            pythondata=JSONParser().parse(stream)
            id=pythondata.get('id', None)
            if id is not None:
                stu=Student.objects.get(id=id)
                serial=StudentSerializer(stu)
                json_data=JSONRenderer().render(serial.data)
                return HttpResponse(json_data, content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
