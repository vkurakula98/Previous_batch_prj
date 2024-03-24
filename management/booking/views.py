from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from management.booking.forms import BookingForm
from .models import Booking
from rest_framework import viewsets
from .serializers import BookingSerializer
from management.package.models import Package
from django.core.mail import send_mail
from django.conf import settings
from django.utils.dateformat import format


@login_required
def book_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, package=Package)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.Package = package
            booking.save()

            start_date_formatted = format(booking.start_Date, 'd-m-Y')
            end_date_formatted = format(booking.end_Date, 'd-m-Y')

            subject = 'Booking Confirmation'
            message = f"""Dear {booking.customer_name},

            Thank you for booking with us! Your trip from Montreal to {booking.Package.destination} from {start_date_formatted} to {end_date_formatted} is now confirmed.

            We wish you an incredible journey ahead. May your travel be filled with exciting adventures and unforgettable memories. Our goal is to provide you with the best experience possible, and we're here to assist with any part of your travel plans.

            Safe travels,
            Clumsy Coders"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [booking.customer_email]

            # Send the email
            send_mail(subject, message, email_from, recipient_list)

            return redirect('booking_success', booking_id=booking.id)  # Ensure this redirects to an existing view
    else:
        form = BookingForm(package=Package)
    return render(request, 'booking/bookingform.html', {'form': form, 'package': Package})  # Correct the template name as needed

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Corrected from 'booking' to 'Booking'
    serializer_class = BookingSerializer

def booking_success(request, booking_id):
    return HttpResponse(f"Booking with ID {booking_id} was successful.")