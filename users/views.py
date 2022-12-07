from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import *
import pdfkit


class SignIn(LoginView):
    form_class = AuthenticationForm
    template_name = "sign_in.html"

    def get_success_url(self):
        return reverse_lazy('profile')


class SignOut(LogoutView):
    template_name = 'sign_out.html'

    def get_success_url(self):
        return reverse_lazy('sign_out')


def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    else:
        form = UserRegisterForm()
    return render(request, 'sign_up.html', {'form': form})


def access_denied(request):
    return render(request, 'access_denied.html')


class Home(TemplateView):
    template_name = "home.html"

    def post(self, request):
        if 'btn sign in' in request.POST.keys():
            return redirect('sign_in')
        elif 'btn sign up' in request.POST.keys():
            return redirect('sign_up')
        elif 'btn sign out' in request.POST.keys():
            return redirect('sign_out')
        elif 'btn go to profile' in request.POST.keys():
            if request.user.is_authenticated:
                return redirect('profile')
            return redirect('access_denied')


def cv(request, **kwargs):
    name = kwargs['name']
    surname = kwargs['surname']
    email = kwargs['email']
    address = kwargs['address']
    phone_number = kwargs['phone_number']
    education_level = kwargs['education_level']
    educational_institutions = kwargs['educational_institutions']
    work_experience = kwargs['work_experience']
    skills = kwargs['skills']
    with open('created_cv.html', 'w') as f:
        f.write('<html lang="en">')
        f.write(f"<h1>  {name} {surname} </h1>")
        f.write(f"<h3> Phone number: </h3> <font size='4'> {phone_number} </font>")
        f.write(f"<h3> Address: </h3> <font size='4'> {address} </font>")
        f.write(f"<h3> Email-address: </h3> <font size='4'> {email} </font>")
        f.write(f"<h3> Education level: </h3> <font size='4'> {education_level} </font>")
        f.write(f"<h3> Accomplished educational institutions: </h3> <font size='4'> {educational_institutions} </font>")
        f.write(f"<h3> Skills: </h3> <font size='4'> </font> {skills}")
        f.write(f"<h3> Work experience: </h3> <font size='4'> </font> {work_experience})")
    pdfkit.from_file('created_cv.html', 'out.pdf')

    return render(request, 'cv.html',
                  {'name': name,
                   'surname': surname,
                   'email': email,
                   'address': address,
                   'phone_number': phone_number,
                   'education_level': education_level,
                   'educational_institutions': educational_institutions,
                   'work_experience': work_experience,
                   'skills': skills
                   }
                  )


def download(request, **kwargs):
    with open('out.pdf', 'rb') as pdf:
        return HttpResponse(
            pdf,
            headers={
                'Content-Type': 'pdf',
                'Content-Disposition': 'attachment; filename="cv.pdf"',
            })


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            return cv(request,
                      name=request.POST['name'],
                      surname=request.POST['surname'],
                      email=request.POST['email'],
                      address=request.POST['address'],
                      phone_number=request.POST['phone_number'],
                      education_level=request.POST['education_level'],
                      educational_institutions=request.POST['educational_institutions'],
                      work_experience=request.POST['work_experience'],
                      skills=request.POST['skills'],
                      )

    else:
        form = ProfileForm()

    return render(request, 'profile.html', {'form': form})
