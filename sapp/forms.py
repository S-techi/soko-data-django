from django.forms import ModelForm  
from . models import shop

class shopform(ModelForm):
    class Meta:
        model = shop
        fields = '__all__'