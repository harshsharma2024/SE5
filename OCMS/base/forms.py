from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User,Student,Teacher


#for StudentLoginForm in html file itself
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']

#for registration
class StudentRegisterForm(ModelForm):
    class Meta():
        model = Student
        fields = ['name','email','roll_no','department']


class TeacherRegisterForm(ModelForm):
    class Meta():
        model = Teacher
        fields = ['name','email','subject_name']



class StudentUpdateForm(ModelForm):
    class Meta():
        model=Student
        fields='__all__'

class TeacherUpdateForm(ModelForm):
    class Meta():
        model=Teacher
        fields='__all__'


class CreateRoomForm(ModelForm):
    class Meta():
        model=Room
        fields=['avatar','course_id','name','description','room_code']



