from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import Article, Category

# Create your views here.
@login_required(login_url='login')
def articles(request):

    # Sacar artículos
    articles = Article.objects.all()
    
    # Paginar artículos
    paginator = Paginator(articles, 3)

    # Recoger número de página
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)


    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles,
    })


@login_required(login_url='login')
def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)

    return render(request, 'categories/category.html', {
        'category': category,
    })


@login_required(login_url='login')
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'article': article,
    })