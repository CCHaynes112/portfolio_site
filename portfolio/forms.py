from django import forms

class EmailForm(forms.Form):
	name = forms.CharField(required="True", label="Name", max_length="30", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
	email = forms.EmailField(required="True", label="Email", max_length="50", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your_Email@Email.com'}))
	body = forms.CharField(required="True", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '. . .'}))