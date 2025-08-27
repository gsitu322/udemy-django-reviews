from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Please enter your name",
        "max_length": "Name must be less than 100 characters long"
    })