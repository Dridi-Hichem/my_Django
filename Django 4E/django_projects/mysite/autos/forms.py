from django.forms import ModelForm

from .models import Make


class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = "__all__"
