from django.shortcuts import render
from django.views import View

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
        cushion = Cushion.objects.all()
        ctx = {
            'cushion': cushion
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
