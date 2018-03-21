from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from shop_app.forms import LoginForm, RegistrationForm
from shop_app.models import Picture, Cushion


class StartView(View):
    def get(self, request):
        return render(request,
                      template_name='start_page.html')


class MainView(View):
    def get(self, request):
        return render(request,
                      template_name='main_page.html')


class OfferView(View):
    def get(self, request):
        return render(request,
                      template_name='offer.html')


class PicturesOfferView(View):
    def get(self, request):
        pictures = Picture.objects.all()
        ctx = {
            'pictures': pictures
        }
        return render(request,
                      template_name='pictures_offer.html',
                      context=ctx)


class CushionsOfferView(View):
    def get(self, request):
        cushions = Cushion.objects.all()
        ctx = {
            'cushions': cushions
        }
        return render(request,
                      template_name='cushions_offer.html',
                      context=ctx)


class AboutView(View):
    def get(self, request):
        return render(request,
                      template_name='about.html')


class AboutDescriptionView(View):
    def get(self, request):
        return render(request,
                      template_name='about_desc.html')


class ContactView(View):
    def get(self, request):
        return render(request,
                      template_name='contact.html')


class PictureView(View):
    def get(self, request, id):
        picture = get_object_or_404(Picture, id=id)
        ctx = {
            'picture': picture
        }
        return render(request,
                      template_name='picture.html',
                      context=ctx)


class CushionView(View):
    def get(self, request, id):
        cushion = get_object_or_404(Cushion, id=id)
        ctx = {
            'cushion': cushion
        }
        return render(request,
                      template_name='cushion.html',
                      context=ctx)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        ctx = {
            'form': form
        }
        return render(request,
                      template_name='login.html',
                      context=ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            nick = form.cleaned_data['nick']
            password = form.cleaned_data['password']
            user = authenticate(nick=nick, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('main'))
        ctx = {
            'form': form
        }
        return render(request,
                      template_name='login.html',
                      context=ctx)


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        ctx = {
            'form': form
        }
        return render(request,
                      template_name='register.html',
                      context=ctx)

    def post(self, request):
        form = RegistrationForm(request.POST)



