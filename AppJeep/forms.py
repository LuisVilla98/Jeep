from django import forms
from AppJeep.models import Jeeps

class Registrojeep(forms.ModelForm):
    class Meta:
        model = Jeeps
        fields = '__all__'