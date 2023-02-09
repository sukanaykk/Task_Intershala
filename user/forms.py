from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Patient, Doctor, User

class Loginform(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


class PatientSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    age = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_patient = True
        user.save()
        student = Patient.objects.create(user=user)
        return user


class DoctorSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    age = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)

        doctor.save()

        return doctor