
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

def index(request):
    now = datetime.datetime.now()
    return render(request, 'newyear/index.html', {
    "newyear": now.month == 1 and now.day == 1
    })
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('HELLO/', include('HELLO.urls'))
# ]