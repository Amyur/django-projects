from django import forms

class CustomerForm(forms.Form):
    Fresh = forms.IntegerField()
    Milk = forms.IntegerField()
    Grocery = forms.IntegerField()
    Frozen = forms.IntegerField()
    Detergents_Paper = forms.IntegerField()
    Delicassen = forms.IntegerField()
    Channel_1 = forms.IntegerField()
    Channel_2 = forms.IntegerField()
    Region_1 = forms.IntegerField()
    Region_2 = forms.IntegerField()
    Region_3 = forms.IntegerField()