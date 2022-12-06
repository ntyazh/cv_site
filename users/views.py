from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib import messages
from .forms import *
from .models import *


class SignIn(LoginView):
    form_class = AuthenticationForm
    template_name = "sign_in.html"

    def get_context_data(self, **kwargs):
        context = super(SignIn, self).get_context_data(**kwargs)
        return context


class SignUp(CreateView):
    form_class = UserRegisterForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('sign_in')

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        #form = UserRegisterForm(request.POST)
        print('fffffffffff')
        user = form.save()
        #username = form.cleaned_data.get('username')
        #messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
        return redirect('sign_in')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            print('fffffffffff')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('sign_in')
    else:
        form = UserRegisterForm()
    return render(request, 'sign_up.html', {'form': form})


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        #context.update(self.get_context_mixin(request=self.request, **kwargs))
        return context

    def post(self, request):
        if 'btn sign in' in request.POST.keys():
            return redirect('sign_in')
        elif 'btn sign up' in request.POST.keys():
            return redirect('sign_up')


class Profile(DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
