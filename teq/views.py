from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from teq.models import Students,Courses
from teq.serializer import StudentSerializer,CourseSerializer

# Create your views here.

# View all students.
class studentlist(APIView):
    def get(self,request):
        students=Students.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

    
# Add new students.
class addstudent(APIView):
    def post(self,request):
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(student_serializer.data,status=status.HTTP_400_BAD_REQUEST)

# Get Student Details.
class studentdetail(APIView):
    def get(self,request,StudentId):
        try:
            students=Students.objects.get(StudentId=StudentId)
        except Students.DoesNotExist:
            return Response(f'Student with Id {StudentId} Not Found',status=status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializer(students)
        return Response(serializer.data)
    
    


# Edit Students.
class editstudent(APIView):
    def get(self,request,StudentId):
        try:
            students=Students.objects.get(StudentId=StudentId)
        except Students.DoesNotExist:
            return Response(f'Student with Id {StudentId} Not Found',status=status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializer(students)
        return Response(serializer.data)

    def put(self,request,StudentId):
        student=Students.objects.get(StudentId=StudentId)
        if not student:
            return Response(f'Could not find a Student with id {StudentId}',status=status.HTTP_400_BAD_REQUEST)
        data={
            'StudentId':request.data.get('StudentId'),
            'StudentName':request.data.get('StudentName'),
            'StudentMob':request.data.get('StudentMob'),
            'StudentEmail':request.data.get('StudentEmail'),
            'Course': request.data.get('Course'),
            'SelectedBatch': request.data.get('SelectedBatch'),
            'DOJ': request.data.get('DOJ'),
            'Fees': request.data.get('Fees'),
            'PaidFees': request.data.get('PaidFees'),
            'LastFeesPaidOn': request.data.get('LastFeesPaidOn'),
            'ModeOfPayment': request.data.get('ModeOfPayment'),
            'PendingFees': request.data.get('PendingFees'),
            'LeadSource': request.data.get('LeadSource'),
            'LeadLocation': request.data.get('LeadLocation'),
            'Executive': request.data.get('Executive')
        }
        serializer = StudentSerializer(student, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete Student Details.
class deletestudent(APIView):
    def get(self,request,StudentId):
        try:
            students=Students.objects.get(StudentId=StudentId)
        except Students.DoesNotExist:
            return Response(f'Student with Id {StudentId} Not Found',status=status.HTTP_404_NOT_FOUND)
        students.delete()
        return Response(f'Details of student with Id {StudentId} deleted',status=status.HTTP_200_OK)





# View all courses.
class courselist(APIView):
    def get(self,request):
        courses=Courses.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data)


# Add new Courses.
class addcourse(APIView):
    def post(self,request):
        course_serializer = CourseSerializer(data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(course_serializer.data,status=status.HTTP_400_BAD_REQUEST)



# Get Course Details.
class coursedetail(APIView):
    def get(self,request,CourseId):
        try:
            courses=Courses.objects.get(CourseId=CourseId)
        except Courses.DoesNotExist:
            return Response(f'Course with Id {CourseId} Not Found',status=status.HTTP_404_NOT_FOUND)
        serializer=CourseSerializer(courses)
        return Response(serializer.data)
    
    


# Edit Course.
class editcourse(APIView):
    def get(self,request,CourseId):
        try:
            courses=Courses.objects.get(CourseId=CourseId)
        except Courses.DoesNotExist:
            return Response(f'Course with Id {CourseId} Not Found',status=status.HTTP_404_NOT_FOUND)
        serializer=CourseSerializer(courses)
        return Response(serializer.data)

    def put(self,request,CourseId):
        course=Courses.objects.get(CourseId=CourseId)
        if not course:
            return Response(f'Could not find a Course with id {CourseId}',status=status.HTTP_400_BAD_REQUEST)
        data={
            'CourseId':request.data.get('CourseId'),
            'CourseName':request.data.get('CourseName'),
            'CourseRate':request.data.get('CourseRate') 
        }
        serializer = CourseSerializer(course, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete Course Details.
class deletecourse(APIView):
    def get(self,request,CourseId):
        try:
            courses=Courses.objects.get(CourseId=CourseId)
        except Courses.DoesNotExist:
            return Response(f'Course with Id {CourseId} Not Found',status=status.HTTP_404_NOT_FOUND)
        courses.delete()
        return Response(f'Details of Course with Id {CourseId} deleted',status=status.HTTP_200_OK)
