from django import forms
from jean.models import learners

class learners_form(forms.ModelForm) :
    class Meta:
        model = learners
        fields = "__all__"
#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 token