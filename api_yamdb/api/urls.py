from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (
    UsersViewSet,
    SignUp,
    token,
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    CommentViewSet,
    ReviewViewSet,
)

app_name = 'api'

v1_router = SimpleRouter()
v1_router.register(
    'users',
    UsersViewSet,
    basename='users'
)


v1_router.register(r'categories', CategoryViewSet, basename='categories')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'titles', TitleViewSet, basename='titles')
v1_router.register(
    r"titles/(?P<title_id>\d+)/reviews",
    ReviewViewSet,
    basename="reviews"
)
v1_router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comments",
)

urlpatterns = [
    path('v1/auth/token/', token, name='token'),
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', SignUp.as_view(), name='signup'),
]
