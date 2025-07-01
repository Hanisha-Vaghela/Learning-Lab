"""
URL configuration for LearningLab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LearningLab import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.code),
    path('about/',view.about),
    path('generate/', view.generate_certificate, name='generate_certificate'),
    path('preview/', view.preview_certificate, name='preview_certificate'),
    path('save/', view.save_certificate, name='save_certificate'),
    path('download/', view.download_certificate_pdf, name='download_certificate_pdf'),
    path('success/', view.success, name='success'),
    path('service/',view.service),
    path('f_course/',view.f_course),
    path('report/',view.report),
    path('contact_tutor/',view.contact_tutor),
    path('shradha_khapra/',view.shraddha_khapra),
    path('broh_code/',view.broh_code),
    path('codewith_mosh/',view.codewith_mosh),
    path('login/',view.login),
    path('signup/',view.signup),
    path('loginsubmit/',view.loginsubmit),
    path('logout/', view.logout_view),
    path('submit/',view.submit),
    path('profile/', view.profile, name='profile'),
    path('tutorials/<str:topic>/', view.tutorials, name='tutorials'),
    path('tutorials/', view.tutorials, name='tutorials_all'),
    path('video_tutorials/<str:language>/', view.video_tutorials, name='video_tutorials'),
    path('video_tutorials/', view.video_tutorials, name='video_tutorials_all'),
    
]
