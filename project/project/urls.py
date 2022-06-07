from django.contrib import admin
from django.urls import path, include
from app.views import frontpages, LoginPage

urlpatterns = [
    path('loginpage/', LoginPage, name='loginpage'),
    path('', include('app.urls'), name="app"),
    path('admin/', admin.site.urls),
    path("", frontpages.as_view(), name="frontpage"),
    path("<int:year>/<int:month>/<int:day>/", frontpages.as_view(), name="frontpage")
]
