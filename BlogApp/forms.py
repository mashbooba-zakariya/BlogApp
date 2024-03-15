from django import forms
from django.contrib.auth.forms import UserCreationForm

from BlogApp.models import Audience, Blogger, Login, CreateBlog


class LoginRegister(UserCreationForm):

    class Meta:
        model = Login
        fields = ('username','password1','password2')



#------------- Form for Customer register------------
class BloggerRegister(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = '__all__'
        exclude = ('user',)


#------------- Form for Manager register------------
class AudienceRegister(forms.ModelForm):
    class Meta:
        model =Audience
        fields = '__all__'
        exclude = ('user',)




# -----------Blog Creation-----------


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = CreateBlog
        fields = ['title', 'content', 'image']



