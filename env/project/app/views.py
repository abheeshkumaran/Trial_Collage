from django.shortcuts import render
from.models import Register,Signup
from .forms import RegisterForm,SignupForm,AdmissionForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        form = RegisterForm
    return render(request, 'register.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        form = SignupForm
    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Signup.objects.filter(username=username,password1=password)
        if user:
            return render(request, 'index.html')
    return render(request, 'loginn.html')

def admission(request):
    if request. method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
        form = AdmissionForm
    return render(request, 'admission.html')

def details(request):
    return render(request, 'details.html')

def connect(request):
    return render(request,'connect.html')