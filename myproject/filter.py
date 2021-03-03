import django_filters
from django_filters import CharFilter
from django import forms
from.models import *



class ExploreProjectFilter(django_filters.FilterSet):
    title=CharFilter(field_name='title',lookup_expr='icontains',label='title')
    type=django_filters.ModelMultipleChoiceFilter(queryset=Type.objects.all(),
                                                  widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=ExploreProject
        fields=['title','type']