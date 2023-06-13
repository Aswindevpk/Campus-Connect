from django.forms import ModelForm
from .models import BloodDonation, Bloodreq 
from django.contrib.auth.models import User


class BloodDonationForm(ModelForm):
    class Meta:
        model = BloodDonation
        fields = '__all__'

    

class Bloodreqform(ModelForm):
    class Meta:
        model = Bloodreq
        fields = '__all__'

class UserForm(ModelForm):
     class Meta:
          model = User
          fields = ['username','password']
