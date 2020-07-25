from . import views
from django.urls import path, include
from BossWebpage.views import GalleryView

urlpatterns = [
    path('', views.index, name='index'),
    path('BossGrappling/about-us', views.aboutus, name='about-us'),
    path('BossGrappling/schedule', views.schedule, name='schedule'),
    path('BossGrappling/gallery', GalleryView.as_view(), name='gallery'),
    path('BossGrappling/appointment-confirm',
         views.freetrial, name="appointment-confirm"),
]
