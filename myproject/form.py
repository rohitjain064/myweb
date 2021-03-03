from django import forms
from django.forms import ModelForm
from.models import *





class ExploreProjectForm(ModelForm):
    class Meta:
        model=ExploreProject
        fields='__all__'

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }


