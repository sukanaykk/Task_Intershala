# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index),
#     path('patient', views.PatientSignUpView, name='patient_signup'),
#     path('doctor', views.DoctorSignUpView, name='doctor_signup'),
#     path('login/',views.login_view,name='login_view'),
# ]
from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='index'),
    path('patient', PatientSignUpView.as_view(), name='patient_signup'),
    path('doctor', DoctorSignUpView.as_view(), name='doctor_signup'),
    # path('login/', DoctorLoginView.as_view(), name='doctor_login'),
]
