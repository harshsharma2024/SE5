from django.contrib import admin

from .models import User,Student,Teacher,Room,Message,Files,Lectures

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Files)
admin.site.register(Lectures)



