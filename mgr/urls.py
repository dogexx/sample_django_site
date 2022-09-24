from django.urls import path

from mgr import customer, sign_in_out

urlpatterns = [

    path('customers', customer.dispatcher),
    path('signin', sign_in_out.signin),
    path('signin', sign_in_out.signout),
]
