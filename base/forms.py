from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room #for what model do we create the form
        fields = '__all__' #with what field - here inheritance of all Room model form --> if not all, list of str
        

