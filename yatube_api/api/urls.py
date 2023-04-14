from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>[1-9]\d*)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path(
        'api/v1/api-token-auth/',
        views.obtain_auth_token,
        name='obtain_auth_token',
    ),
    path('api/v1/', include(router.urls)),
]
