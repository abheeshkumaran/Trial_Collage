from  django import forms
from .models import Register,Signup,Admission

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'
