from django.urls import path
from .views import *

urlpatterns = [
    path('', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                               'delete': 'destroy'}), name='user_detail'),

    path('follow/', FollowViewSet.as_view({'get': 'list', 'post': 'create'}), name='follow_list'),
    path('follow/<int:pk>/', FollowViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                         'delete': 'destroy'}), name='follow_detail'),

    path('post/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post_list'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                   'delete': 'destroy'}), name='post_detail'),

    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                             'delete': 'destroy'}), name='comment_detail'),
]
