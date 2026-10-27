from django.forms import ModelForm  
from . models import clothes

class userform(ModelForm):
    class Meta:
        model = clothes
        fields = '__all__'