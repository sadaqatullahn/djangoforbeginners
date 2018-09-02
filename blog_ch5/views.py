from django.views.generic import ListView

from .models import BlogPost
# Create your views here.

class BlogListView(ListView):
    """This is Blog HomePage View"""

    model = BlogPost
    template_name = 'blog_ch5/bloghome.html'
