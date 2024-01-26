from django.urls import path, include

from apps.Phones.views import SavePhoneInfo,MobileBrandViewset,MobilePhoneViewset

urlpatterns = [
    # This API Give all the brand list
    path("all-brands-list/", MobileBrandViewset.as_view({'get':"brandList"})),
    path("all-series-list/", MobileBrandViewset.as_view({'get':"seriesList"})),

    # These API are related to Phone
    path("list-by-brands/", MobilePhoneViewset.as_view({'get':"phoneListWithBrand"})),
    path("list-by-series/", MobilePhoneViewset.as_view({'get':"phoneListWithSeries"})),
    path("specs/", MobilePhoneViewset.as_view({'get':"phoneSpecs"})),
    path("recent-added/", MobilePhoneViewset.as_view({'get':"recentPhoneAdded"})),

    # Mobile Data Save Using This API
    path("mobile-data-save/", SavePhoneInfo.as_view({'post':"save"}))
    
]