from django.shortcuts import render, redirect
from django.contrib import messages
from . models import TuberContact


def tuber_contact(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']

        tuber_contact = TuberContact(full_name=full_name, phone=phone, email=email, company=company, subject=subject, message=message)
        tuber_contact.save()
        messages.success(request, 'Thanks for Reaching Out Us')
        return redirect('youtubers')

