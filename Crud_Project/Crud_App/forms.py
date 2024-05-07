from django import forms
from .models import Student_info


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = Student_info
        fields = ["username", "email", "password", "image"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(
                render_value=True, attrs={"class": "form-control"}
            ),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
