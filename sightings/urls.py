from django.urls import path

from . import views

app_name='sightings'

urlpatterns = [
        path('',views.index),
        #path('<int:unique_id>/',views.detail,name='detail'),
        path('/map',views.map,name='map'),
        #path('sightings/stats/',views.stats,name="stats"),
        ]
