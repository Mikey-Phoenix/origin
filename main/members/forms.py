from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'block w-full border-0 bg-[#1c1c1c] text-white rounded-sm focus:outline-red-700 focus:ring focus:ring-red-700'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'block w-full   border-0 bg-[#1c1c1c] text-white rounded-sm focus:outline-red-700 focus:ring focus:ring-red-700'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'block w-full border-0 bg-[#1c1c1c] text-white rounded-sm focus:outline-red-700 focus:ring focus:ring-red-700'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'block w-full  border-0 bg-[#1c1c1c] text-white rounded-sm focus:outline-red-700 focus:ring focus:ring-red-700'
        self.fields['username'].widget.attrs['id'] = 'user_name'
        self.fields['password1'].widget.attrs['class'] = 'block w-full  border-0 bg-[#1c1c1c] text-white rounded-sm focus:outline-red-700 focus:ring focus:ring-red-700'
        self.fields['password2'].widget.attrs['class'] = 'block w-full  border-0 bg-[#1c1c1c] text-white rounded-sm focus:outline-red-700 focus:ring focus:ring-red-700'