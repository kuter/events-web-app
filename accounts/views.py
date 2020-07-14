from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, FormView, UpdateView

from .forms import UserCreationForm
from .models import User


class SignUpView(CreateView):
    """Registration view page."""

    model = User
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/user_form.html'

    def form_valid(self, form):
        """Send email confirmation message."""  # noqa: DAR101, DAR201
        form.instance.is_active = False
        return super().form_valid(form)


class EmailConfirmView(FormView):
    """Registration email confirmation view."""

    def dispatch(self, *args, **kwargs):
        """Check given token.

        Returns:
            HttpResponseRedirect: login page if *True* otherwise index page

        """  # noqa: DAR101
        user = self.get_user(kwargs.get('uidb64'))
        token = kwargs.get('token')

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponseRedirect(reverse('login'))
        return HttpResponseRedirect('/')

    def get_user(self, uidb64):
        """Get user for given uidb64.

        Args:
            uidb64: base64 encoded user pk

        Returns:
            User: user object

        Raises:
            Http404: on any exception

        """
        try:  # noqa: WPS229
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, ObjectDoesNotExist, ValidationError):  # noqa: E501
            raise Http404()
        return user


class ProfileView(LoginRequiredMixin, UpdateView):
    """Participant profile edit view."""

    model = User
    fields = ['email', 'username', 'first_name', 'last_name']

    def get_object(self, queryset=None):
        """Get object for the currently logged-in user."""  # noqa: DAR101, DAR201, E501
        if queryset is None:
            queryset = self.get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        return queryset.get()
