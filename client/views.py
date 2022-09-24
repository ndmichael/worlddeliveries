from django.shortcuts import render, redirect
from .forms import SenderForm, ItemForm, ReceiverForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shipment.models import ItemDetail, Status

# Create your views here.

def dashboard(request, username):
    items = ItemDetail.objects.all()
    context = {
        "items": items,
        "title": "dashboard-targe"
    }
    return render(request, 'account/user/dashboard.html', context)


@login_required
def create_shipment(request):
    if request.method == "POST":
        i_form = ItemForm(request.POST, request.FILES)
        s_form = SenderForm(request.POST, request.FILES, prefix="sender")
        r_form = ReceiverForm(request.POST, request.FILES, prefix="receiver")

        if i_form.is_valid() and s_form.is_valid() and r_form.is_valid():
            sender_obj = s_form.save(commit=False)
            sender_obj.user = request.user
            sender_obj.save()
            
            receiver_obj = r_form.save(commit=False)
            receiver_obj.sender = sender_obj
            receiver_obj.save()

            item_obj = i_form.save(commit=False)
            item_obj.item_sender = sender_obj
            item_obj.item_receiver =receiver_obj
            item_obj.paid  = True
            item_obj.save()

            Status.objects.create(item=item_obj) # create status when creating items

            messages.success(request, f"Logistics Created Successfully.")
            return redirect("client-dashboard", request.user.username)

    else:
        i_form = ItemForm()
        s_form = SenderForm(prefix="sender") 
        r_form = ReceiverForm(prefix="receiver")
    context = {
        "i_form": i_form,
        "s_form": s_form,
        "r_form": r_form
    }
    return render(request, 'account/user/create_shipment.html', context)


