from django.urls import path
from . import views
urlpatterns=[
    path('',views.mob_login),
    path('home',views.home),
    path('mob_logout',views.mob_logout),
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete),
]