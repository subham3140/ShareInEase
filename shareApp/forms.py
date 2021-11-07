from django.contrib.auth.forms import UserCreationForm

from shareApp.models import User


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type' : "text",
            'class' : "form-control",
            'id' : "username" 
        })
        self.fields['email'].widget.attrs.update({
            'type' : "text",
            'class' : "form-control",
            'id' : "email" 
        })
        self.fields['password1'].widget.attrs.update({
            'type' : "text",
            'class' : "form-control",
            'id' : "password1" 
        })
        self.fields['password2'].widget.attrs.update({
            'type' : "text",
            'class' : "form-control",
            'id' : "password2" 
        })
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')