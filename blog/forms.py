from pyexpat import model
from django.forms import ModelForm
from .models import Blog,User

class blogForm(ModelForm):
    class Meta:
     model=Blog
     fields='__all__'
     
     
# ModelForm has no model class specified.
# beacuse of the typo in the blogform that is not writing the class meta and keeping the m small and large in the model 


class Add_UserForm(ModelForm):
    class Meta:
     model=User
     fields='__all__'