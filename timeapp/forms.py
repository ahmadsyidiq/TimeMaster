from django.forms import ModelForm, DateInput
from .models import Task, Project


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {'due_date': DateInput(format=('%Y-%m-%d'),
                    attrs={'type':'date'}),
                }
        