from django.urls import path, include

urlpatterns = [
    path("phones/", include("apps.Phones.urls"))
]