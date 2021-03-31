from django.shortcuts import render
from blog.models import Article
from blog.forms import EmailForm
# Create your views here.

def index(request):
    blog_posts = Article.objects.all()
    return render(request, "index.html", { "blog_posts": blog_posts })

def article_list(request):
    blog_posts = Article.objects.all()

    return render(request, "blog.html", { "blog_posts": blog_posts })

def contact(request):
    form = EmailForm
    return render(request, "contact.html", {"form": form})

def article(request, article_id):
    context = {
        "article": Article.objects.get(id=article_id)
    }
    return render(request, "article.html", context=context)

def email(request):
    if request.method == "POST":
        data = dict(request.POST)
        
        email_body = f"""
            You received an email from {data.get("first_name")} {data.get("last_name")} at {data.get("email_address")}
            <br><br>
            {message}
        """