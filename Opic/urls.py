"""Opic URL Configuration

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
from django.contrib import admin
from django.urls import include, path, re_path
from rest_auth.registration.views import VerifyEmailView
from allauth.account.views import confirm_email
from users import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/',admin.site.urls),
    path('users/', include('users.urls')),
    path('auth/', include([
        path('', include('rest_auth.urls')),
        re_path(r'registration/account-confirm-email/', VerifyEmailView.as_view(),
            name='account_email_verification_sent'),

        ########################
        # TODO: return template where post request made to the url above with post paramer: 'key'
        re_path(r'registration/account-confirm-email/(?P<key>[-:\w]+)/', VerifyEmailView.as_view(),
            name='account_confirm_email'),
        ########################
        
        path('registration/', include('rest_auth.registration.urls')),
    ])),
    # path('accounts/', include('allauth.urls')),
]