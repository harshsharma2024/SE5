from django.contrib import admin

from .models import User,Student,Teacher,Room,Message

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Message)

