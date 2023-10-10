from django.contrib import admin
from django.urls import path, include
from store.views import home, signup, profile, privacy, terms, deactivate


urlpatterns = [
    path('admin/', admin.site.urls),
path('account/', include('django.contrib.auth.urls')),
path('signup/', signup, name='signup'),
path('', home, name='home'),
path('profile/', profile, name='profile'),
path('privacy/', privacy, name='privacy'),
path('terms/', terms, name='terms'),
path('deactivate/', deactivate, name='deactivate'),
]
