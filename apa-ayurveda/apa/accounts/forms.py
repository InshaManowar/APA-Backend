from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import Account


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

	class Meta:
		model = Account
		fields = ("first_name","last_name","designation","qualification","email","phone","address","username", "password1", "password2","profile_image")
  
#class ProfilePicForm(forms.ModelForm):
   # class Meta:
     #   model=Account
      #  fields=['username','profile_pic']

class AccountAuthenticationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("invalid login")

class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'username', 'profile_image', 'first_name', 'last_name', 'qualification', 'designation', 'phone', 'address')

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data ['email']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use.' % email)

	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use.' % username)


