from django import forms
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User


class PokemonForm(forms.ModelForm):
    class Meta:
        model = someonesPokemon
        fields = ['pokemon', 'nickname', 'attack1', 'attack2', 'attack3', 'attack4', 'item', 'tera_type']
        widgets = {'pokemon':  forms.TextInput}
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pokemon'].widget.attrs['readonly']=True

        self.fields['nickname'].widget.attrs['class']="form-control"
        self.fields['nickname'].widget.attrs['placeholder']="Nickname"

        self.fields['pokemon'].widget.attrs['class']="form-control"
        self.fields['pokemon'].widget.attrs['placeholder']="Pokedex Number"

        self.fields['attack1'].widget.attrs['class']="form-select"
      
        
        self.fields['attack2'].widget.attrs['class']="form-select"
      
        self.fields['attack3'].widget.attrs['class']="form-select"
      

        self.fields['attack4'].widget.attrs['class']="form-select"
       
        self.fields['item'].widget.attrs['class']="form-select"
        

        self.fields['tera_type'].widget.attrs['class']="form-select"
        
      

  
class PasteForm(forms.ModelForm):
    class Meta:
        model = PokePaste
        fields = ['name', 'pokemon1', 'pokemon2', 'pokemon3', 'pokemon4', 'pokemon5', 'pokemon6', 'pokepaste_code']
        
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class']="form-control"
        self.fields['name'].widget.attrs['placeholder']="Name"

        self.fields['pokemon1'].widget.attrs['class']="form-select"
       

        self.fields['pokemon2'].widget.attrs['class']="form-select"
      
        
        self.fields['pokemon3'].widget.attrs['class']="form-select"
      
        self.fields['pokemon4'].widget.attrs['class']="form-select"
      

        self.fields['pokemon5'].widget.attrs['class']="form-select"
       
        self.fields['pokemon6'].widget.attrs['class']="form-select"
        

        self.fields['pokepaste_code'].widget.attrs['class']="form-select"
        self.fields['pokepaste_code'].widget.attrs['placeholder']="Code"


        self.fields['pokemon1'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon2'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon3'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon4'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon5'].queryset = someonesPokemon.objects.filter(user=user)
        self.fields['pokemon6'].queryset = someonesPokemon.objects.filter(user=user)
