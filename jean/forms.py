from django import forms
from models import learners

class learners_form(forms.ModelForm) :
    class Meta:
        model = learners
        fields = "__all__"
