from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


urlpatterns = [
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'v1/jwt/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh',
    ),
    path(
        'v1/jwt/verify/',
        TokenVerifyView.as_view(),
        name='token_verify',
    ),
    path(
        'v1/posts/',
        PostViewSet.as_view({'get': 'list', 'post': 'create'}),
    ),
    path(
        'v1/posts/<int:pk>/',
        PostViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
    ),
    path(
        'v1/groups/',
        GroupViewSet.as_view({'get': 'list'}),
    ),
    path(
        'v1/groups/<int:pk>/',
        GroupViewSet.as_view({'get': 'retrieve'}),
    ),
    path(
        'v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:comment_id>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
    ),
    path(
        'v1/follow/',
        FollowViewSet.as_view({'get': 'list', 'post': 'create'}),
    ),
]
