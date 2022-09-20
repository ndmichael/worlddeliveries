from django import forms
from shipment.models import Status, ItemSender, ItemReciever, ItemDetail


class DateInput(forms.DateInput):
    input_type = 'date'


class ItemTrackForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'Track Items'
        self.fields['q'].widget.attrs.update({
            'class': 'form-control form-control-lg'
        })

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': '7'}))


class EditSenderForm(forms.ModelForm):
    class Meta:
        model = ItemSender
        fields = ["fullname", "company", "postal_code", "city", "country"]


class EditClientForm(forms.ModelForm):
    class Meta:
        model = ItemReciever
        fields = ["fullname", "email", "postal_code", "city", "country"]


class EditItemForm(forms.ModelForm):
    date_sent = forms.DateField(widget=DateInput)
    date_recieved = forms.DateField(widget=DateInput)
    date_shipped = forms.DateField(widget=DateInput)
    def __init__(self, *args, **kwargs):
        super(EditItemForm, self).__init__(*args, **kwargs)
        self.fields["item_code"].disabled = True
    class Meta:
        model = ItemDetail
        fields = [
                    "item_name", "quantity", "weight", 
                    "image", "shipped", "item_code", 
                    "date_sent", "date_recieved", "date_shipped","item_code"
                ]


class EditStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["status", "problem_type", "country"]