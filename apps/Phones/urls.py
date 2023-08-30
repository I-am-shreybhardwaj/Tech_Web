from django.urls import path, include

from apps.Phones.views import SavePhoneInfo

urlpatterns = [
    path("save/", SavePhoneInfo.as_view({'post':"save"})),
    path("data/", SavePhoneInfo.as_view({'get':"data"}))
]