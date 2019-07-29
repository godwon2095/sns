from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import User


class UserChangeForm(forms.UserChangeForm):
    # password = None

    class Meta:
        model = User
        fields = ['image', 'username', 'info']
        labels = {
            'image': "프로필 이미지",
            'username': "사용자 닉네임",
            'info': "자기소개",
        }


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])
