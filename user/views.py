from django.shortcuts import render
from django.shortcuts import redirect
from .models import Patient,Doctor,User
from django.views.generic import CreateView
from .forms import PatientSignUpForm,DoctorSignUpForm,Loginform
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request,'index.html')
class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return redirect('index')

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return redirect('index')


# def login_view(request):
#     form = Loginform(request.POST or None)
#     msg= None
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 msg= 'Invalid Credentials'
#         else:
#             msg= 'Error validating form'
#     return render(request,'login.html',{'form':form,'msg':msg})