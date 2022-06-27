from django.forms import ModelForm
from django import forms

from ordenamiento.models import Parroquia, Barrio

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        field = ['nombre', 'tipo']

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        field = ['nombre', 'numero_vivien', 'numero_parq', 'numero_edif', 'parroquia']
                
class BarrioParroquiaForm(ModelForm):
    def __init__(self, parroquia, *args, **kwargs):
        super(BarrioParroquiaForm, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(parroquia)

    class Meta:
        model = Barrio
        field = ['nombre', 'numero_vivien','numero_parq', 'numero_edif', 'parroquia']    
                        