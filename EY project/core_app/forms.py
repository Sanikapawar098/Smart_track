from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CitizenProfile

from .models import Complaint


class CreateComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('description',)


class CustomerRegistrationForm(UserCreationForm):
    area_address = forms.CharField(widget=forms.Textarea, required=False)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_citizen = True
        if commit:
            user.save()
            CitizenProfile.objects.create(
                user=user,
                area_address=self.cleaned_data.get('area_address', ''),
                phone_number=self.cleaned_data.get('phone_number', ''),
            )
        return user
