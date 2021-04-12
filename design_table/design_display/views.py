from django.template import loader
from django.http import HttpResponse

from .models import CurrentImage

# Create your views here.

def index(request):
    current_image = CurrentImage.objects.all().first()
    template = loader.get_template('display/index.html')
    context = {
        'current_image': current_image,
    }
    return HttpResponse(template.render(context,request))
    