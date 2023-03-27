from django.db import models
from django.contrib.auth.models import AbstractUser

# class Room:
#     pass

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    
    # email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS=[]
    

    

class Room(models.Model):
    # host = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    course_id=models.IntegerField(primary_key=True)
    teacher=models.CharField(max_length=100)
    name = models.CharField(max_length=200) #set it to host.subject_name during declaration by default
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=False)
    avatar = models.ImageField(null=True, default="avatar.svg")

    #assignment
    #lectures

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Student')
    roll_no = models.CharField(max_length=50, null=True)
    name=models.CharField(max_length=250)
    email = models.EmailField(null=False)
    department=models.CharField(max_length=250 ,null=True)
    rooms=models.ManyToManyField(Room,related_name="student_rooms",blank=True)
    bio = models.TextField(null=True)
    phone = models.IntegerField(null=True)

    

    avatar = models.ImageField(null=True, default="avatar.svg")
    #something with reverse absolutr url not written

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['roll_no']



class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Teacher')
    name=models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250,null=True)
    rooms=models.ManyToManyField(Room,related_name="teacher_rooms",blank=True)
    bio = models.TextField(null=True)
    phone = models.IntegerField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    #something with reverse absolutr url not writte

    def __str__(self):
        return self.name

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class ClassRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(
        Room, related_name='classroom_rooms', blank=True)
    
    




