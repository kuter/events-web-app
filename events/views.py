# flake8: noqa: DAR201
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.http.response import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Event


@login_required
def sign_up(request, pk):
    """Sign up for event."""
    event = get_object_or_404(Event, pk=pk)
    event.eventparticipant_set.get_or_create(event=event, user=request.user)
    return redirect(event.get_absolute_url())


@login_required
def withdraw(request, pk):
    """Withdraw from event."""
    event = get_object_or_404(Event, pk=pk)
    event.eventparticipant_set.filter(user=request.user).delete()
    return redirect(event.get_absolute_url())


class EventCreate(LoginRequiredMixin, CreateView):
    """Event create view."""

    model = Event
    fields = ['title', 'description', 'date']
    template_name = 'events/event_form_create.html'

    def form_valid(self, form):
        """Set Event owner."""  # noqa: DAR101, DAR201
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventUpdate(LoginRequiredMixin, UpdateView):
    """Event update view."""

    model = Event
    fields = ['title', 'description', 'date']
    template_name = 'events/event_form_update.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)


class EventDetail(DetailView):
    """Event detail view."""

    model = Event

    def is_user_participate(self):
        """Check if logged user is a participant."""
        if self.request.user.is_anonymous:
            return False
        return self.object.eventparticipant_set.filter(
            user=self.request.user,
        ).exists()

    def get_context_data(self, **kwargs):
        """Add some extra data to context."""
        context = super().get_context_data(**kwargs)
        context.update({'is_user_participate': self.is_user_participate()})
        return context


class EventList(ListView):
    """Index view."""

    queryset = Event.objects.incoming()
    paginate_by = 12
