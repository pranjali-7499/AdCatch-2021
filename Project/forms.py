from django import forms

from Project.models import Upload_File


class TestUploadForm(forms.ModelForm):
    class Meta:
        model = Upload_File
        fields = ['videoname','videotype','filename']

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data