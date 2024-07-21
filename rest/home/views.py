from rest_framework.views import APIView
from rest_framework.response import Response
from .wether import get_weather_forecast


# Create your views here.


class Home(APIView):
    def get(self, request):
        return Response({"name": "abtin"})

    def post(self, request):
        name = request.data["name"]
        return Response({"name": name})
        pass


class WetherInfo(APIView):
    # def get(self, request):
    #     sanandaj_latitude = 35.3119
    #     sanandaj_longitude = 46.9964

    #     forecast = get_weather_forecast(sanandaj_latitude, sanandaj_longitude)
    #     return Response({"wether": forecast})

    def post(self, request):
        sanandaj_latitude = 35.3119
        sanandaj_longitude = 46.9964

        forecast = get_weather_forecast(sanandaj_latitude, sanandaj_longitude)
        return Response({"wether": forecast})
