from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User,Student,Teacher


#for StudentLoginForm in html file itself


#for registration
class StudentRegisterForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['name','email','password1', 'password2']


class TeacherRegisterForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ['name','email','password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'students']

class StudentUpdateForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class TeacherUpdateForm(ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'




