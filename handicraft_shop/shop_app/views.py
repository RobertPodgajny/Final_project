from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from shop_app.forms import LoginForm, RegistrationForm
from shop_app.models import Picture, Cushion, Address


class StartView(View):
    def get(self, request):
        return render(request,
                      template_name='start_page.html')


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,
                      template_name='main_page.html')


# class OfferView(LoginRequiredMixin, View):
#     def get(self, request):
#         return render(request,
#                       template_name='offer.html')


class PicturesOfferView(LoginRequiredMixin, View):
    def get(self, request):
        pictures = Picture.objects.all()
        ctx = {
            'pictures': pictures
        }
        return render(request,
                      template_name='pictures_offer.html',
                      context=ctx)


class CushionsOfferView(LoginRequiredMixin, View):
    def get(self, request):
        cushions = Cushion.objects.all()
        ctx = {
            'cushions': cushions
        }
        return render(request,
                      template_name='cushions_offer.html',
                      context=ctx)


# class AboutView(LoginRequiredMixin, View):
#     def get(self, request):
#         return render(request,
#                       template_name='about.html')


class AboutDescriptionView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,
                      template_name='about_desc.html')


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,
                      template_name='contact.html')


class PictureView(LoginRequiredMixin, View):
    def get(self, request, id):
        picture = get_object_or_404(Picture, id=id)
        ctx = {
            'picture': picture
        }
        return render(request,
                      template_name='picture.html',
                      context=ctx)


class CushionView(LoginRequiredMixin, View):
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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Zalogowano')
            return HttpResponse('Podano błędny login lub hasło')
        return redirect(reverse('main'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('start'))


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
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['new_password']
            user = User.objects.create_user(username, email, password)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            address = Address()

            address.address = form.cleaned_data['address']
            address.user = user
            address.save()

            return redirect(reverse('login'))
        ctx = {'form': form}
        return render(request, template_name="register.html", context=ctx)


