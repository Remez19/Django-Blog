import imp
from django.urls import path

from . import views

urlpatterns = [
    # An empty path - basically the first page we load
    path('', view=views.StartingPageView.as_view(), name='starting-page'),
    path('posts', view=views.AllPostsView.as_view(), name='posts-page'),
    # We name the var 'slug' because thats a convetion for this kind of paths
    # The slug identifier is unique symbole which will check if the var contains only numbers and characters that
    # are not special in this case wee expect paths to be of kind -> 'posts/my-first-post
    path('posts/<slug:slug>', view=views.SinglePostView.as_view(),
         name='post-detail-page'),
    path("read-later", views.ReadLaterView.as_view(), name='read-later')
]
