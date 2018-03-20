from django.shortcuts import render
from django.views import View


class StartView(View):
    def get(self, request):
        return render(request,
                      template_name='start_page.html')


class MainView(View):
    def get(self, request):
        return render(request,
                      template_name='main_page.html')
