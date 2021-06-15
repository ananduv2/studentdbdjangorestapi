from django.db import models

# Student Model.
class Students(models.Model):
    StudentId=models.AutoField(primary_key=True)
    StudentName=models.CharField(max_length=100)
    StudentMob=models.CharField(max_length=10)
    StudentEmail=models.EmailField(max_length=100)
    Course = models.CharField(max_length=100, default="", editable=False)
    SelectedBatch = models.CharField(max_length=100, default="", editable=False)
    DOJ = models.DateField(blank=True, null=True)
    Fees = models.IntegerField(null=True)
    PaidFees = models.IntegerField(null=True)
    LastFeesPaidOn = models.DateField(blank=True, null=True)
    ModeOfPayment = models.CharField(max_length=100, default="GooglePay", editable=False)
    PendingFees = models.IntegerField(null=True)
    LeadSource = models.CharField(max_length=100, default="", editable=False)
    LeadLocation = models.CharField(max_length=100, default="", editable=False)
    Executive = models.CharField(max_length=100, default="", editable=False)
    class Meta:
        db_table="students"
    def __str__(self):
        return self.StudentName

# Course Model.
class Courses(models.Model):
    CourseId=models.AutoField(primary_key=True)
    CourseName=models.CharField(max_length=100)
    CourseRate=models.IntegerField()
    class Meta:
        db_table="courses"
    def __str__(self):
        return self.CourseName
