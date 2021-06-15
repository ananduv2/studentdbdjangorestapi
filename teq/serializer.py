from rest_framework import serializers
from teq.models import Students,Courses

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('__all__')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=('__all__')



