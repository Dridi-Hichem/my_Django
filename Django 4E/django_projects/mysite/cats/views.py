from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import BreedForm
from .models import Breed, Cat


class CatList(LoginRequiredMixin, ListView):
    model = Cat
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breed_count"] = Breed.objects.count()

        return context


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")


class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()
        return render(
            request, "cats/breed_list.html", {"breed_list": breed_list}
        )


class BreedCreate(LoginRequiredMixin, View):
    template_name = "cats/breed_form.html"
    success_url = reverse_lazy("cats:all")

    def get(self, request):
        form = BreedForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})

        form.save()
        return redirect(self.success_url)


class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    template_name = "cats/breed_form.html"
    success_url = reverse_lazy("cats:all")

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=breed)

        if not form.is_valid():
            return render(request, self.template_name, {"form": form})

        form.save()
        return redirect(self.success_url)


class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    template_name= "cats/breed_confirm_delete.html"
    success_url = reverse_lazy("cats:all")

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        return render(request, self.template_name, {"breed": breed})

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)
