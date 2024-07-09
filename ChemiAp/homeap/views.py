from django.shortcuts import render
from django.http import HttpResponse
from homeap.models import BookTable
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def book_table(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        date = request.POST.get("date")

        if name != "" and email != "" and number != "" and date != "":
            data = BookTable(name=name,email=email,number=number,date=date)
            data.save()

            subject = 'Table Booking'
            message = f'Name: {name}\nEmail: {email}\nPhone Number: {number}\nDate: {date}'
            from_email = email 
            recipient_list = [settings.EMAIL_HOST_USER, from_email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    return render(request, 'book_table.html')

def contact(request):
    return render(request, 'contact.html')

