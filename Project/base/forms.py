from django import forms
from .models import Task, Category, Tag


class PositionForm(forms.Form):
    position = forms.CharField(widget=forms.HiddenInput())

    def clean_position(self):
        position_data = self.cleaned_data['position']
        if position_data:
            position_list = position_data.split(',')
            return position_list
        raise forms.ValidationError("Invalid position data.")


class TaskForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'category', 'tags']
