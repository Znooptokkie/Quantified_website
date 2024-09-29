from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import Test
from .forms import FooterVragenForm

def home(request):

    test_data = Test.objects.all()

    context = {
        "header_background_image": "images/firefly_sensor_buiten.webp",
        "test_posts": test_data

    }
    return render(request, "home.html", context)

def producten(request):
    return render(request, "producten.html")

def footer_vragen_form_submit(request):
    if request.method == "POST":
        form = FooterVragenForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Get the form data to use in the email
            category = form.cleaned_data['category']  # This will be the email subject
            question = form.cleaned_data['question']  # This will be the email body

            # Send an email with the form data
            send_mail(
                subject=f"Form Submission: {category}",  # Email subject
                message=question,  # The message content (textarea content)
                from_email=settings.DEFAULT_FROM_EMAIL,  # Sender's email
                recipient_list=['recipient-email@example.com'],  # Replace with the recipient's email address
                fail_silently=False,
            )

            messages.success(request, 'Je formulier is succesvol verzonden!')

        else:
            # Add error message
            messages.error(request, 'Er is een fout opgetreden bij het verzenden van je formulier.')

    # Redirect to the previous page (using HTTP_REFERER)
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to the referring page, or home if not found