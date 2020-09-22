from django import forms
values=[['python','python'],['django','Django']]

def check_for_w(n):#n=WARD
    if n[0].lower()=='w':#'W'.lower()=='w'
        raise forms.ValidationError('Name should not start with w')

def check_for_length(s):
    if len(s)<=5:
        raise forms.ValidationError('length is too small')


class Crispy_Form(forms.Form):
    #name=forms.CharField(max_length=36,required=True,validators=[check_for_w,check_for_length])
    name=forms.CharField(max_length=36)
    email=forms.EmailField()
    Reenteremail=forms.EmailField()

    def clean_name(self):
        i=self.cleaned_data.get('name')
        if i[0].lower()=='w':
            raise forms.ValidationError('name should not start with w')


    def clean(self):
        e=self.cleaned_data.get('email')
        r=self.cleaned_data.get('Reenteremail')
        
        if e!=r:
            raise forms.ValidationError('emails not matched')
























