from django.forms import ModelForm
from .models import BloodDonation, Bloodreq ,Program
from django.contrib.auth.models import User


class BloodDonationForm(ModelForm):
    class Meta:
        model = BloodDonation
        fields = '__all__'

    

class Bloodreqform(ModelForm):
    class Meta:
        model = Bloodreq
        fields = '__all__'



