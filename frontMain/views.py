from django.shortcuts import render, get_object_or_404, redirect
from frontMain.models import Product
from django.core.paginator import Paginator
from django.core.mail import send_mail
from frontMain.forms import EmailContactForm
from frontMain.models import User_feedback
from django.contrib import messages


def index(request):
    return render(request, template_name='frontMain/index.html', context={
        'products' : Product.objects.all()
    })

def about(request):
    return render(request, template_name='frontMain/about.html')

# TODO: Тут будет передаваться форма для обратной связи
def contact(request):
    sent = False
    if request.method == 'POST':
        form = EmailContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} sent feedback "
            message = f"{cd['text_body']} \nTo contact me:\n{cd['phone_number']}\n{cd['email']}"
            send_mail(subject, message, cd['email'], ["pkuslin9@gmail.com"])
            sent = True

            feedback = User_feedback(
                name=cd['name'],
                email=cd['email'],
                phone_number=cd['phone_number'],
                text_body=cd['text_body']
            )
            feedback.save()
            return redirect("test/")
    else:
        form = EmailContactForm()
    return render(request, template_name='frontMain/contact.html', context={'form': form,
                                                                            'sent': sent,
                                                                            })

def test(request):
    return render(request, template_name='frontMain/feedback_result.html')


# def contact_form_submit(request):
#     if request.method == 'POST':
#         form = EmailContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             subject = f"{cd['name']} sent feedback "
#             message = f"{cd['text_body']} \nTo contact me:\n{cd['phone_number']}\n{cd['email']}"
#             send_mail(subject, message, cd['email'], ["pkuslin9@gmail.com"])
#
#             feedback = User_feedback(
#                 name=cd['name'],
#                 email=cd['email'],
#                 phone_number=cd['phone_number'],
#                 text_body=cd['text_body']
#             )
#             feedback.save()
#             return redirect('feedback_result')
#     return redirect('contact')
#
# def feedback_result(request):
#     return render(request, 'frontMain/feedback_result.html')




def house(request):
    post_list = Product.objects.all()
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page', 1)
    houses = paginator.page(page_number)

    return render(request, template_name='frontMain/house.html', context={
        'houses' : houses
    })

def price(request):
    return render(request, template_name='frontMain/price.html')
