from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import MakeForm
from .models import Auto, Make


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        auto_list = Auto.objects.all()
        make_count = Make.objects.count()

        context = {"make_count": make_count, "auto_list": auto_list}
        return render(request, "autos/auto_list.html", context)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        make_list = Make.objects.all()
        return render(
            request, "autos/make_list.html", {"make_list": make_list}
        )


class MakeCreate(LoginRequiredMixin, View):
    template = "autos/make_form.html"
    success_url = reverse_lazy("autos:all")

    def get(self, request):
        form = MakeForm()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, {"form": form})

        form.save()
        return redirect(self.success_url)


class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = "autos/make_form.html"
    success_url = reverse_lazy("autos:all")

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        return render(request, self.template, {"form": form})

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)

        if not form.is_valid():
            return render(request, self.template, {"form": form})

        form.save()
        return redirect(self.success_url)


class MakeDelete(LoginRequiredMixin, View):
    model = Make
    template = "autos/make_confirm_delete.html"
    success_url = reverse_lazy("autos:all")

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        return render(request, self.template, {"make": make})

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")
