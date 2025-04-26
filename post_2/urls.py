from django.urls import path
from .views import PostCreateView, PostListView, PostDetailsView, PostUpdateView, PostDeleteView  #aqui se importan las vistas que se van a usar en el html


urlpatterns = [
    path('post_create/', PostCreateView.as_view(), name='post_create'),              #aqui se registra la vista del html post_create
    path('', PostListView.as_view(), name='post_list'),                              #aqui se registra la vista del html post_list
    path('post_2/details/<int:pk>/', PostDetailsView.as_view(), name='post_details'),  #aqui se registra la vista del html post_details
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]



