from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView

# Create your views here.


def index(request):
    return render(request, 'BossGrappling/index.html')


def aboutus(request):
    return render(request, 'BossGrappling/about_us.html')


def schedule(request):
    return render(request, 'BossGrappling/schedule.html')


def freetrial(request):
    return render(request, 'BossGrappling/appointment_confirm.html')


class GalleryView(TemplateView):
    template_name = 'BossGrappling/gallery.html'


def handler404(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 4040)
