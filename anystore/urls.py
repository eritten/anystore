from django.contrib import admin
from django.urls import path, include
from store.views import home, signup, profile
urlpatterns = [
    path('admin/', admin.site.urls),
path('account/', include('django.contrib.auth.urls')),
path('signup/', signup, name='signup'),
path('', home, name='home'),
path('profile/', profile, name='profile'),
]
