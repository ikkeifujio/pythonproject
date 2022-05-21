from django.contrib import admin
from django.urls import path, include
from app.views import frontpage, frontpages

urlpatterns = [
    path('blog/', include('app.urls'), name="blog"),
    path('admin/', admin.site.urls),
    path("", frontpages.as_view(), name="frontpage"),
    path("<int:year>/<int:month>/<int:day>/", frontpages.as_view(), name="frontpage")
]
