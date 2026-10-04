from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    # Django form ki configuration
    class Meta:
        # Form ko Resume model ke saath connect karta hai
        model = Resume
        # Form mein sirf file field show karta hai
        fields = ["file"]

    # Uploaded file ko validate karta hai
    def clean_file(self):
        # User ki uploaded file ko get karta hai
        file = self.cleaned_data["file"]

        # Check karta hai ki file 5 MB se badi hai ya nahi
        if file.size > 5 * 1024 * 1024:
            # File badi hone par error show karta hai
            raise forms.ValidationError(
                "File size must be less than 5 MB"
            )

        # Check karta hai ki file PDF ya DOCX hai
        if not file.name.lower().endswith((".pdf", ".docx")):
            # Wrong file type hone par error show karta hai
            raise forms.ValidationError(
                "File must be .pdf or .docx"
            )

        # Validation successful hone par file return karta hai
        return file