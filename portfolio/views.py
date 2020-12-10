from django.shortcuts import render
from .models import home_page, showcase, about
from django.core.paginator import Paginator
from django.core.mail import send_mail

# Create your views here.

def home(request):
    page_obj = home_page.objects.all().order_by('-date_posted')
    show = showcase.objects.all()
    paginator = Paginator(page_obj, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'showcase':show, 'page_obj':page_obj}
    return render(request, 'portfolio/index.html', context)

def about_me(request):
    context = {'about':about.objects.all()}
    return render(request, 'portfolio/about.html', context)

def contact(request):
    if request.method == "POST":
        msg_name = request.POST['msg-name']
        msg_email = request.POST['msg-email']
        msg_phone = request.POST['msg-phone']
        message = request.POST['message']
        full_msg = f'{message} \n Phone: {msg_phone} \n Email: {msg_email}'

        send_mail(
            msg_name, # Subject
            full_msg, # message
            msg_email, # from email
            ['frank.pythonmail@gmail.com', 'lightfree8@gmail.com'], #To email
            fail_silently=False,
        )
        return render(request, 'portfolio/contact.html', {'name':msg_name})

    else:
        return render(request, 'portfolio/contact.html')

def portfolio(request):
    return render(request, 'portfolio/coming.html')

def blog(request):
    return render(request, 'portfolio/coming.html')
