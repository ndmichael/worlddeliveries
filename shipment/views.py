from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from shipment.forms import (
    ItemTrackForm, ContactForm, EditStatusForm,
    EditSenderForm, EditClientForm, EditItemForm
)
from shipment.models import ItemDetail
from django.core.mail import send_mail, BadHeaderError

# Create your views here.


def index (request):
    return render(request, 'shipment/index.html', {'title': 'home'})

def track_item (request):
    
    item=None
    if 'q' in request.POST:
        form = ItemTrackForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['q']
            item = ItemDetail.objects.filter(item_code=q).first()
            form = ItemTrackForm() 
    else:
        form = ItemTrackForm()       
    context = {
        'form': form,
        'item': item,
        'title': 'tracking'
    }
    return render(request, 'shipment/track.html', context)

def services (request):
    return render(request, 'shipment/services.html', {'title': 'services'})

def contact (request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['sdelivery@biz.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header')
            messages.success(request, f"message have been sent successfully")
            return redirect("contact")
        else:
            print("Failed form submission")
    

    context = {
        'form': form,
        'title': 'contact Us'
    }                           
    return render(request, 'shipment/contact.html', context)

def editSender(request, slug, id):
    item = ItemDetail.objects.get(slug=slug, id=id)
    sender = item.item_sender
    if request.method == "POST":
        form = EditSenderForm(request.POST, instance=sender)
        if form.is_valid():
            form.save()
            messages.success(request, f"Sender details updated successfully.")
            return redirect("client-dashboard", request.user.username)
    else:
        form = EditSenderForm(instance=sender)
    context = {
        'title': "targe-editor",
        's_form': form
    }
    return render(request, 'shipment/editsender.html', context)

def editClient(request, slug, id):
    item = ItemDetail.objects.get(slug=slug, id=id)
    receiver = item.item_receiver
    if request.method == "POST":
        form = EditClientForm(request.POST, instance=receiver)
        if form.is_valid():
            form.save()
            messages.success(request, f"Client details updated successfully.")
            return redirect("client-dashboard", request.user.username)
    else:
        form = EditClientForm(instance=receiver)
    context = {
        'title': "targe-editor sender",
        'form': form
    }
    return render(request, 'shipment/editclient.html', context)  

def editItem(request, slug, id):
    item = ItemDetail.objects.get(slug=slug, id=id)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Item updated successfully.")
            return redirect("client-dashboard", request.user.username)
        else:
            print("form not valid.")
    else:
        form = EditItemForm(instance=item)
    context = {
        'title': "targe-editor sender",
        'form': form
    }
    return render(request, 'shipment/edititem.html', context)      

def editStatus(request, id):
    item = ItemDetail.objects.get(id=id)
    if request.method == "POST":
        form = EditStatusForm(request.POST, instance=item.item_status)
        if form.is_valid():
            s_form = form.save(commit=False)
            s_form.item = item
            s_form.save()
            messages.success(request, f"Status set successfully.")
            return redirect("client-dashboard", request.user.username)
    else:
        form = EditStatusForm(instance=item.item_status)
    context = {'form': form}
    return render(request, 'shipment/editstatus.html', context)