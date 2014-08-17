from django import forms
from django.forms import ModelForm
from structure.models import User

# From django forms.py
class LIITRegistrationForm(ModelForm):

  password1 = forms.CharField(label="Password",
                              widget=forms.PasswordInput)
  password2 = forms.CharField(label="Password confirmation",
                              widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('username',)

  def clean_password2(self):
    # Check that the two password entries match
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
        msg = "Passwords don't match"
        raise forms.ValidationError(
          _("The two password fields didn't match."),
          code='password_mismatch',
        )
    return password2

  def save(self, commit=True):
    user = super(LIITRegistrationForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit: 
      user.save()
    return user
