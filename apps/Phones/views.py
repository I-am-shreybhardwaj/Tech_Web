import requests

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.Phones.constant import EXCEPTION_MESSAGE

from apps.Phones.models import MobileBrands, MobilePhone

from bs4 import BeautifulSoup
from apps.Phones.serializer import BrandInfoSerializer, MobileInfo

from apps.Phones.utils import html_tables_to_json


# Create your views here.

class MobileBrandViewset(ViewSet):
    def brandList(self,request):
        try:
            brand = MobileBrands.objects.all()
            serializer = BrandInfoSerializer(brand, many=True).data
            return Response({"data":serializer,"message":"Mobile Phone Details Save Successfully","success":True},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":EXCEPTION_MESSAGE,"exception":e,"success":False},status=status.HTTP_206_PARTIAL_CONTENT)
        
class MobilePhoneViewset(ViewSet):
    def phoneListWithBrand(self,request):
        try:
            series_params = request.GET.get("series_id",'')
            if series_params:
                mobile = MobilePhone.objects.filter(series=series_params)
                serializer = MobileInfo(mobile, many=True).data
                return Response({"data":serializer,"message":"Mobile Phone With Series Fetch Successfully","success":True},status=status.HTTP_200_OK)
            return Response({"message":"Mobile Brand Not Found","success":False},status=status.HTTP_206_PARTIAL_CONTENT)
        except Exception as e:
            return Response({"message": EXCEPTION_MESSAGE,"exception":e,"success":False},status=status.HTTP_206_PARTIAL_CONTENT)
        
    def phoneListWithSeries(self,request):
        try:
            brand_params = request.GET.get("brand_id",'')
            if brand_params:
                mobile = MobilePhone.objects.filter(brand=brand_params)
                serializer = MobileInfo(mobile, many=True).data
                return Response({"data":serializer,"message":"Mobile Phone With Brand Fetch Successfully","success":True},status=status.HTTP_200_OK)
            return Response({"message":"Mobile Brand Not Found","success":False},status=status.HTTP_206_PARTIAL_CONTENT)
        except Exception as e:
            return Response({"message": EXCEPTION_MESSAGE,"exception":e,"success":False},status=status.HTTP_206_PARTIAL_CONTENT)
                
    def phoneSpecs(self, request):
        try:
            phone_id = request.GET.get("phone_id")
            mobile_phone = MobilePhone.objects.filter(id=phone_id).first()
            if mobile_phone:
                serializer = MobileInfo(mobile_phone).data
                return Response({"data":serializer,"message":"Mobile Phone Details Fetch Successfully","success":True},status=status.HTTP_200_OK)
            return Response({"message":"Mobile Phone Details Not Found","success":False},status=status.HTTP_206_PARTIAL_CONTENT)
        except Exception as e:
            return Response({"message": EXCEPTION_MESSAGE,"exception":e,"success":False},status=status.HTTP_206_PARTIAL_CONTENT)
            
    def recentPhoneAdded(self, request):
        try:
            mobile_phone = MobilePhone.objects.all().order_by("-created_at")
            if mobile_phone:
                serializer = MobileInfo(mobile_phone).data
                return Response({"data":serializer,"message":"Mobile Phone Details Fetch Successfully","success":True},status=status.HTTP_200_OK)
            return Response({"message":"Mobile Phone Details Not Found","success":False},status=status.HTTP_206_PARTIAL_CONTENT)
        except Exception as e:
            return Response({"message": EXCEPTION_MESSAGE,"exception":e,"success":False},status=status.HTTP_206_PARTIAL_CONTENT)


class SavePhoneInfo(ViewSet):
    def save(self,request):
        try:
            data = request.data.copy()
            brand_check = MobileBrands.objects.filter(brand_name=data.get('brand')).first()
            if brand_check:
                url = data.get("url")
                payload = {}
                session = requests.session()
                session.headers.update({
                  'Host': 'www.gsmarena.com',
                  'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                  'Referer' : "www.gsmarena.com"
                })
                response = session.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    tables = soup.find_all('table')
                    json_output = html_tables_to_json(tables)

                    mobile_phone = MobilePhone.objects.create(
                        brand = brand_check,
                        phone_name = data.get("model"),
                        specs = json_output
                    )
                    serializer = MobileInfo(mobile_phone).data
                    return Response({"data":serializer,"message":"Mobile Phone Details Save Successfully","success":True},status=status.HTTP_200_OK)
                else:
                    return Response({"message":response.text,"success":False},status=status.HTTP_206_PARTIAL_CONTENT)
            else:
                return Response({"message":"Brand Not Found","success":False},status=status.HTTP_206_PARTIAL_CONTENT)
        except Exception as e:
            return Response({"message":EXCEPTION_MESSAGE,"exception":e,"success":False},status=status.HTTP_206_PARTIAL_CONTENT)          
        
