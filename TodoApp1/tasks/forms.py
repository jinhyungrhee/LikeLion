from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        FormHelper.form_show_labels = False

    class Meta:
        model = Task
        fields = '__all__'