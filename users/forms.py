from django.contrib.auth import get_user_model
from django.forms import ModelForm, widgets
from django import forms

class SignupForm(ModelForm):
    first_name = forms.CharField(widget=widgets.TextInput(attrs={'placeholder':'Firstname'}))
    last_name = forms.CharField(widget=widgets.TextInput(attrs={'placeholder':'Lastname'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email',)
    
    def signup(self,request,user):
        self.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()



