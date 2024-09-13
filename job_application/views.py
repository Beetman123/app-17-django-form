from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    if request.method == "POST":  # may not work if there are multiple things they can do
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            # Email message
            message_body = (f"Thank you for your job application submission, {first_name}. "
                            f"Here is what you sent: \n{first_name}\n"
                            f"{last_name}\n{date}\n"
                            f"Thank you!")
            email_message = EmailMessage("Form submission conformation",
                                         message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully")

    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')