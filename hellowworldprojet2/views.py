from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>Hello World</h1>')
    return returnedobject

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'
