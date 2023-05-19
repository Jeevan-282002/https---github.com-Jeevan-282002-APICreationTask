from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")

    frds = [
        "Jeevan","jagu","rima"
    ]


    return JsonResponse(frds, safe=False)
