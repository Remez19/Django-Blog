
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def starting_page(request):
    # accessing the database , here we filter by the field "date" in decending order by adding "-".
    # this line is just along query !
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    the_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": the_post,
        "post_tags": the_post.tags.all(),
    })
