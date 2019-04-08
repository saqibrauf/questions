
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sm_views
from questions.sitemap import QuestionSitemap, CategorySitemap

sitemaps = {
	'question' : QuestionSitemap(),
    'category' : CategorySitemap(),
}

urlpatterns = [
	#Sitemap
	path('sitemap-index.xml/', sm_views.index, {'sitemaps' : sitemaps }, name='django.contrib.sitemaps.views.sitemap'),
	path('sitemap-<section>.xml/', sm_views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('admin/', admin.site.urls),
    path('', include('questions.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)