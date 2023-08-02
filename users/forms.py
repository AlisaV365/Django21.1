from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import EmailField

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ('email', 'password1', 'password2')
        fields = ('email',)
        field_classes = {'email':EmailField}


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()

    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         if form.data.get('need_generate', False):
    #             self.object.set_password(
    #                 self.object.make_random_password(12)
    #             )
    #         self.object.save()
    #         return super().form_valid(form)
