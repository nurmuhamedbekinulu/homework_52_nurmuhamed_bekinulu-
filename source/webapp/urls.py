from django.urls import path
from webapp.views.base import index_view, cat_stats_view


urlpatterns = [
    path('', index_view),
    path('cat_stats.html', cat_stats_view)
]