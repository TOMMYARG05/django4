from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre_usuario',
                'email',
                'contraseña',
                ]
        widgets={'nombre_usuario':forms.TextInput(attrs={ 'class': 'form-control' }),
                'email':forms.EmailInput(attrs={ 'class': 'form-control' }),
                'contraseña':forms.TextInput(attrs={ 'class': 'form-control' }),
            }        
