from .views import Autolist


urlpatterns = [
    path('autolist', Autolist.as_view()),
]
