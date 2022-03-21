from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        print('Enquiry Checking ---')

        # If user had made enquiry already

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                lisitng_id=listing_id, user_id=user_id)
            print("New Enquiry Sent ")
            if has_contacted:
                messages.error(
                    request, 'You have Already made an inquiry for this listing')
                print("Error has been sended")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, lisitng_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        print("Request been checked")
        contact.save()
        print("Request Saved")

        send_mail(
            'Property listing Enquiry',
            'There has been an enquiry for ' + listing + '.Sign into the admin pannel for more info',
            'shivamrvgupta@gmail.com',
            [realtor_email, 'rvshivamsahu.1222@gmail.com'],
            fail_silently=False,
        )

        messages.success(
            request, 'Your request have been submitted, A realtor will get back to you soon ')
        print("Message has been Sent")
        return redirect('/listings/'+listing_id)