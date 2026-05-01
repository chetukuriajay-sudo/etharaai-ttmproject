from django import forms
from django.contrib.auth.models import User
from .models import Project, Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_select2.forms import Select2MultipleWidget

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=Select2MultipleWidget,
        required=False
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'members']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Refresh users every time, so deleted users won't show
        self.fields['members'].queryset = User.objects.all()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'assigned_to', 'status', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }