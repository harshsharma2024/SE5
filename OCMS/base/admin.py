from django.contrib import admin

from .models import User,Student,Teacher,Room,Message,Files,Lectures,Tassignments,Meeting

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Files)
admin.site.register(Lectures)
admin.site.register(Tassignments)
admin.site.register(Meeting)



