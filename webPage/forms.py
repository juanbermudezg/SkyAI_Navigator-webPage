from django import forms

class CreateNewUser(forms.Form):
    username = forms.CharField(max_length=35, widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Nombre de usuario',
        'id':'user'
    }))
    password = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type':'password',
        'placeholder':'Contraseña',
        'id':'pass'
    }))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type':'email',
        'placeholder':'Correo electrónico',
        'id':'email'
    }))