
from django.contrib import admin
from django.urls import path, include
admin.site.site_header= "OSMS"
admin.site.site_title="OSMS Admin"
admin.site.index_title="Welocome to OSMS"
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),

]
