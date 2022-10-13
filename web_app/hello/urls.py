from django.urls import path

from web_app.hello import views

urlpatterns = (
    path("", views.index, name = "index"),
    path("brian", views.brian, name = "brian"),
    path("david", views.david, name = "david")
)