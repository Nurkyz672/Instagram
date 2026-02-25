from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( UserProfileListAPIView, UserProfileDetailAPIView,
                     FollowViewSet,HashtagViewSet,LocationViewSet,PostListAPIView,
                     PostDetailAPIView,PostContentViewSet,PostLikeListAPIView,PostLikeDetailAPIView,
                     CommentViewSet,CommentLikeViewSet,FavoriteViewSet,FavoriteItemViewSet,RegisterView,
                     LoginView, LogoutView)

router = DefaultRouter()
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'hashtag', HashtagViewSet, basename='hashtag')
router.register(r'location', LocationViewSet, basename='location')
router.register(r'postContent', PostContentViewSet, basename='postContent')
router.register(r'comment',CommentViewSet, basename='comment')
router.register(r'commentLike', CommentLikeViewSet, basename='commentLike')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'favoriteItem', FavoriteItemViewSet, basename='favoriteItem')

urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('post/', PostListAPIView.as_view(), name='post_list'),
    path('post/<int:pk>/',PostDetailAPIView.as_view(), name='post_detail'),
    path('postlike/', PostLikeListAPIView.as_view(), name='postlike_list'),
    path('postlike/<int:pk>/', PostLikeDetailAPIView.as_view(), name='postlike_detail'),
    path('register/', RegisterView.as_view(), name='register-list'),
    path('login/', LoginView.as_view(), name='login-list'),
    path('logout/', LogoutView.as_view(), name='logout-list'),

]