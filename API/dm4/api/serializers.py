from attr import attr
from itsdangerous import Serializer
from rest_framework import serializers
from .models import Student

def start_with_r(value):
    if value[0].lower() !='r':
        raise serializers.ValidationError('Name should be start with R')

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100, validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    def validate_roll(self, attrs):
        if attrs >=200:
            raise serializers.ValidationError('Seat Fill')
        else:
            return attrs
    # object level Validation
 

    def validate(self, data):
        nm=data.get('name')
        print(nm)
        ct=data.get('city')
        print(ct)
        print(nm.lower())
        print(ct.lower())
        if nm.lower() == 'rohit' and ct.lower() != 'dhaka':
            raise serializers.ValidationError('City must be Dhaka')
        else:
            return data
