from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class the CreateView to pass the request to the form.
    """


class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    Sub-class the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """

    def form_valid(self, form):
        model_object = form.save(commit=False)
        model_object.owner = self.request.user
        model_object.save()
        return super().form_valid(form)


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)
