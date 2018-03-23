"""handicraft_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from shop_app.forms import LoginForm
from shop_app.views import StartView, MainView, PicturesOfferView, CushionsOfferView, AboutDescriptionView, \
    ContactView, PictureView, CushionView, RegistrationView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', StartView.as_view(), name='start'),
    url(r'^main_page/$', MainView.as_view(), name='main'),
    url(r'^offer/pictures/$', PicturesOfferView.as_view(), name='pictures'),
    url(r'^offer/cushions/$', CushionsOfferView.as_view(), name='cushions'),
    url(r'^about/description/$', AboutDescriptionView.as_view(), name='desc'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^picture/(?P<id>\d+)/$', PictureView.as_view(), name='picture'),
    url(r'^cushion/(?P<id>\d+)/$', CushionView.as_view(), name='cushion'),
    url(r'^login/', auth_views.LoginView.as_view(template_name="login.html",
                                                 form_class=LoginForm), name='login'),
    url(r'^register/$', RegistrationView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
