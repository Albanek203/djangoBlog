from django.shortcuts import get_object_or_404, render


# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
