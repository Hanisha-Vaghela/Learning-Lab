from django.contrib import admin
from sample.models import User, Tutorials, Certificate, VideoTutorial

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username","email","password")

class TutorialsAdmin(admin.ModelAdmin):
    list_display = ("title","details")

class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name","course","completion_date")

class VideoTutorialAdmin(admin.ModelAdmin):
    list_display = ("language","page")

admin.site.register(User,UserAdmin)
admin.site.register(Tutorials,TutorialsAdmin)
admin.site.register(Certificate,CertificateAdmin)
admin.site.register(VideoTutorial,VideoTutorialAdmin)