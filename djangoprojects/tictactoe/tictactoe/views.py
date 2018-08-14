from django.http import HttpResponse

#function redirect from page url 
def welcome(request):
    return HttpResponse("Hello,World!")