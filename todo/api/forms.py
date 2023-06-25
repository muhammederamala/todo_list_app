from django import forms
from .models import TodoItem_model


# add class form references the add_class model

class TodoItem_form(forms.ModelForm):
    class Meta:
        model = TodoItem_model
        fields = ('task','description','deadline')