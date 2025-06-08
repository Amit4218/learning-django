from django.urls import path
from . import views

urlpatterns = [
    path("",views.app_2_home, name="app_2_home"),
    path("chai/",views.chai, name="chai"),
    path("<int:chai_id>/", views.chai_details, name='chai_details')

]
