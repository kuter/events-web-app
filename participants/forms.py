from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.forms.fields import EmailField
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCreationForm(BaseUserCreationForm):
    """Custom UserCreationForm with email as a userfield."""

    confirmation_email_template_name = 'registration/confirmation_email.html'

    class Meta:
        model = User
        fields = ('email', )
        field_classes = {'email': EmailField}

    def send_mail(self, user):
        """Send a django.core.mail.EmailMultiAlternatives to user.

        Args:
            user: registered user

        """
        subject = _('Confirm your email')
        context = {
            'token': default_token_generator.make_token(user),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        }
        body = loader.render_to_string(
            self.confirmation_email_template_name, context,
        )

        email_message = EmailMultiAlternatives(subject, body, to=[user.email])

        email_message.send()

    def save(self, commit=True):
        """Send confirmation email on save."""  # noqa: DAR101, DAR201
        user = super().save(commit)
        context = {
            'user': user,
        }
        self.send_mail(**context)
        return user
