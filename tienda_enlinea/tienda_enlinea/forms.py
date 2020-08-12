from django import forms

from django.contrib.auth.models import User

# clase de registros
class RegisterForm(forms.Form):
    """ form register. """
    
    # Atributos > input en nuestro formulario
    username = forms.CharField(required=True,
                                min_length=4,
                                max_length=50,
                                # Agregando estilos # attrs diccionario para class, id, placeholder
                                widget=forms.TextInput(attrs={ 
                                   'class':'form-control',
                                   'id': 'username',
                                   'placeholder': 'Username'
                                }))
    
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class' : 'form-control',
                                 'id':'email',
                                 'placeholder':'example@mibus.com.pa'
                             }))
    
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class':'form-control',
                               }))

    #prefijo clean_username   
    def clean_username(self):
        
        # username = campo que queremos validar
        username = self.cleaned_data.get('username')
        
        # saber si existe o no un usuaario
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya se encuentra en uso')
        return username
    
    def clean_email(self):
        
        # username = campo que queremos validar
        email = self.cleaned_data.get('email')
        
        # saber si existe o no un usuaario
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya se encuentra en uso')
        return email
    
      