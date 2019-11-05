from django.shortcuts import render
from .models import Produto
from django.http import HttpResponse

def index(request):
    html = """
    <html>
      <body>
        <h1>!!!</h1>
      </body>
    </html>
    """
    return HttpResponse(html)


# Create your views here.
