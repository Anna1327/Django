from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class LoginView(View):

    def get(self, request):
        return render(request, 'lab1/index.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            # html += "(): {}<br>".format(key, value)
            html += f'{key}: {value}<br>'
        html += '</body></html>'
        return HttpResponse(html)