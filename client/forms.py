from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm, LoginForm
from shipment.models import ItemDetail, ItemReciever, ItemSender, Status



class MyCustomSignupForm(SignupForm):

    field_order = ['first_name', 'last_name', 
                   'email', 'username', 'password1', 'password2']
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    def __init__(self, *args, **kwargs):

        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = ''
        self.fields["username"].label = ''
        self.fields["password1"].label = ''
        self.fields["password2"].label = ''
        self.fields["first_name"].label = ''
        self.fields["last_name"].label = ''
        self.fields["first_name"].widget.attrs["placeholder"] = "first name"
        self.fields["last_name"].widget.attrs["placeholder"] = "last name"

        self.fields["password1"].widget.attrs.update(
            {'class': 'form-control-lg '})
        self.fields["password2"].widget.attrs.update(
            {'class': 'form-control-lg '})
        self.fields["last_name"].widget.attrs.update(
            {'class': 'form-control-lg '})
        self.fields["first_name"].widget.attrs.update(
            {'class': 'form-control-lg '})
        self.fields["email"].widget.attrs.update(
            {'class': 'form-control-lg '})
        self.fields["username"].widget.attrs.update(
            {'class': 'form-control-lg '})


class SenderForm(forms.ModelForm):
    class Meta:
        model = ItemSender
        fields = ["fullname", "address", "company", "postal_code", "city", "country"]
        widgets = {
          'address': forms.Textarea(attrs={'rows':2}),
        }



class ReceiverForm(forms.ModelForm):
    class Meta:
        model = ItemReciever
        fields = ["fullname", "email", "address",  "postal_code", "city", "country"]
        widgets = {
          'address': forms.Textarea(attrs={'rows':2}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemDetail
        fields = ["item_name", "quantity", "description", "weight", "image"]
        widgets = {
          'description': forms.Textarea(attrs={'rows':2}),
        }

