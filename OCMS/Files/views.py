from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User ,Teacher,Student,Room,Message
from base import models
from .forms import StudentRegisterForm,TeacherRegisterForm,StudentUpdateForm,TeacherUpdateForm,UserForm,CreateRoomForm

@login_required(login_url='check')
def portal(request):
    return render(request,'base/portal.html',{})

def LandingPage(request):
    return render(request,'base/landingpage.html',{})

def check(request):
    return render(request,'base/check.html',{})

def StudentLogin(request):
    # if request.user.is_authenticated:
    #     return redirect('portal')
    
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user=User.objects.get(email=email)
        # except:
        #     messages.error(request, 'User does not exist!!')
        
        # user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('portal')
        # else:
        #     messages.error(request, 'Username OR password does not exit')

        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('portal')

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('student-login')
    return render(request,'base/login_student.html',{})

#TeacherLogin

def LogOutStudent(request):
    logout(request)
    return redirect('landingpage')

def LogOutTeacher(request):
    logout(request)
    return redirect('landingpage')


def StudentRegister(request):
    user_type="student"
    # form = StudentRegisterForm()

    if request.method == 'POST':
        student_form = StudentRegisterForm(request.POST)
        user_form=UserForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            # if user_form.DoesNotExist:
                user=user_form.save(commit=False)
                user.is_student=True
                user.save()

                profile=student_form.save(commit=False)
                profile.user=user
                profile.save()
                return redirect('portal')
            # else:
                messages.error(request,'User already exists with this mailID')
        else:
            messages.error(request,'An error occured during Student Registration')
    else:
        user_form=UserForm()
        student_form=StudentRegisterForm()

    context={'user_form':user_form,'student_form':student_form}

    return render(request,'base/student_register.html',context)

def TeacherRegister(request):
    user_type="student"
    # form = StudentRegisterForm()

    if request.method == 'POST':
        Teacher_form = TeacherRegisterForm(request.POST)
        user_form=UserForm(request.POST)
        if user_form.is_valid() and Teacher_form.is_valid():
            # if user_form.DoesNotExist:
                user=user_form.save(commit=False)
                user.is_teacher=True
                user.save()

                profile=Teacher_form.save(commit=False)
                profile.user=user
                profile.save()
                return redirect('portal')
            # else:
                messages.error(request,'User already exists with this mailID')
        else:
            messages.error(request,'An error occured during Teacher Registration')
    else:
        user_form=UserForm()
        Teacher_form=TeacherRegisterForm()

    context={'user_form':user_form,'teacher_form':Teacher_form}

    return render(request,'base/teacher_register.html',context)








#     user_type="teacher"
#     form = TeacherRegisterForm()

#     if request.method == 'POST':
#         form = TeacherRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_teacher=True
#             user.save()
#             login(request,user)
#             return redirect('portal')
#         else:
#             messages.error(request,'An error occured during Teacher Registration')

#     return render(request,'base/teacher_register.html',{'form':form,'user_type':user_type})


def TeacherLogin(request):
    # if request.user.is_authenticated:
    #     return redirect('portal')
    
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user=User.objects.get(email=email)
        # except:
        #     messages.error(request, 'User does not exist!!')
        
        # user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('portal')
        # else:
        #     messages.error(request, 'Username OR password does not exit')

        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('portal')

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('teacher-login')
    return render(request,'base/login_teacher.html',{})





# def room(request,pk):
#     room=Room.objects.get(id=pk)
#     room_messages=room.message_set.all()
#     # students=room.students.all()
#     students=std(room)

#     if request.method == 'POST':
#         message=Message.objects.create(
#             user=request.user,
#             room=room,
#             body=request.POST.get('body')
#         )
#         #adding students to be sorted
#         return redirect('room',pk=room.id)
    
#     context={'room':room,'room_messages':room_messages,'students':students}

#     return render(request,'base/room.html',context)

# def std(self,request):
#     rooms=request.GET.get('rooms')

#     result = Student.objects.filter(
#         rooms=rooms
#     )
#     return result


def create_room(request):
    form=CreateRoomForm()
    # Teacher_User=request.user.Teacher
    Teacher_User=get_object_or_404(models.Teacher, pk=request.user.id)
    if request.method == 'POST':

        new_room=Room.objects.create(
            avatar=request.POST.get('avatar'),
            course_id=request.POST.get('course_id'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            # room=request.POST.get('room_id'),
            teacher=Teacher_User.name,
        )
        Teacher_User.rooms.add(new_room)
        return redirect('portal')

    context={'form':form}

    return render(request, 'base/create_room.html',context)

#Student Profile
# def studentProfile(request):
#     Student_User=get_object_or_404(Student,user=request.user)
#     dict={'img':Student_User.avatar,
#           'roll_no':Student_User.roll_no,
#           'name':Student_User.name,
#           'Dep':Student_User.department,
#           'mail_id':Student_User.email,
#           'bio':Student_User.bio,
#           'phone':Student_User.phone
#           }
#     return render(request,'base\studentProfile.html',dict)

# def ProfessorProfile(request):
#     Teacher_User=get_object_or_404(Teacher,user=request.user)
    
#     dict={'img':Teacher_User.avatar,
#           'website':Teacher_User.websitelink,
#           'name':Teacher_User.name,
#           'Dep':Teacher_User.subject_name,
#           'mail_id':Teacher_User.email,
#           'bio':Teacher_User.bio,
#           'phone':Teacher_User.phone,
          
#           }

    
    
#     return render(request,'base\ProfessorProfile.html',dict)


def Professorprofileupdate(request):
    Teacher_User=get_object_or_404(Teacher,user=request.user)
    dict={}
    dict={'img':Teacher_User.avatar,'website':Teacher_User.websitelink,'name':Teacher_User.name,'Dep':Teacher_User.subject_name,'mail_id':Teacher_User.email,'bio':Teacher_User.bio,'phone':Teacher_User.phone}
    if request.method=="POST":
         
         
         image_=request.FILES.get('img')
         Teacher_User.name=request.POST.get('name')
         Teacher_User.websitelink=request.POST.get('website')
         if image_==None:
                Teacher_User.avatar=dict['img']
                
                
                
         else:
                Teacher_User.avatar=request.FILES.get('img')
                
                  
              
         Teacher_User.subject_name=request.POST.get('dep')
         Teacher_User.bio=request.POST.get('bio')
         
         Teacher_User.phone=request.POST.get('phone')
         Teacher_User.email=request.POST.get('email')
         Teacher_User.save()
         
       
     
    return render(request,'base\Professorprofileupdate.html',dict)
# def reload(request):
#     Professorprofileupdate(request)
#     return redirect()('Professorprofileupdate.html')
def studentProfile(request):
    Student_User=get_object_or_404(Student,user=request.user)
    dict={'img':Student_User.avatar,
          'roll_no':Student_User.roll_no,
          'name':Student_User.name,
          'Dep':Student_User.department,
          'mail_id':Student_User.email,
          'bio':Student_User.bio,
          'phone':Student_User.phone
          }
    return render(request,'base\studentProfile.html',dict)

def ProfessorProfile(request):
    Teacher_User=get_object_or_404(Teacher,user=request.user)
    
    dict={'img':Teacher_User.avatar,
          'website':Teacher_User.websitelink,
          'name':Teacher_User.name,
          'Dep':Teacher_User.subject_name,
          'mail_id':Teacher_User.email,
          'bio':Teacher_User.bio,
          'phone':Teacher_User.phone,
          
          }

    
    
    return render(request,'base\ProfessorProfile.html',dict)


def studentprofileupdate(request):
    Teacher_User=get_object_or_404(Student,user=request.user)
    dict={}
    dict={'img':Teacher_User.avatar,'roll_no':Teacher_User.roll_no,'name':Teacher_User.name,'Dep':Teacher_User.subject_name,'mail_id':Teacher_User.email,'bio':Teacher_User.bio,'phone':Teacher_User.phone}
    if request.method=="POST":
         
         
         image_=request.FILES.get('img')
         Teacher_User.name=request.POST.get('name')
         Teacher_User.roll_no=request.POST.get('roll_no')
         if image_==None:
                Teacher_User.avatar=dict['img']
                
                
                
         else:
                Teacher_User.avatar=request.FILES.get('img')
                
                  
              
         Teacher_User.subject_name=request.POST.get('dep')
         Teacher_User.bio=request.POST.get('bio')
         
         Teacher_User.phone=request.POST.get('phone')
         Teacher_User.email=request.POST.get('email')
         Teacher_User.save()
       
     
    return render(request,'base\studentprofileupdate.html',dict)










