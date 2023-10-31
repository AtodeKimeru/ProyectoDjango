from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug') # flat=True texto plano en vez de tupla

    return {
        'pages': pages
    }