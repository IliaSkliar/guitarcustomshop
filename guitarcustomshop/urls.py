"""guitarcustomshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

from customers.views import SignUp, Profile
from orders.views import orders_list, create_order, order_details, \
    accept_order, order_done

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', Profile.as_view(), name='profile'),
    path('orders/', orders_list, name='orders'),
    path('orders/new/', create_order, name='create_order'),
    path('orders/<int:order_id>/', order_details, name='order_details'),
    path('orders/<int:order_id>/accept', accept_order, name='accept_order'),
    path('orders/<int:order_id>/done', order_done, name='order_done'),

]
admin.site.site_header = "Guitar Custom Shop Administration"
admin.site.site_title = "Guitar Custom Shop Admin Portal"
admin.site.index_title = "Welcome to Guitar Custom Shop Researcher Portal"