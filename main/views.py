from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Author, Book
from cart.forms import CartAddProductForm


def popular_list(request):
    books = Book.objects.filter(available=True)
    return render(request,
                  'main/index/index.html',
                  {'books': books})


def book_detail(request, slug):
    book = get_object_or_404(Book,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm
    return render(request,
                  'main/product/detail.html',
                  {'book': book,
                   'cart_product_form': cart_product_form})


def product_list(request, category_slug=None):
    page = request.GET.get('page', 1)
    author = None
    authors = Author.objects.all()
    books = Book.objects.filter(available=True)
    paginator = Paginator(books, 10)
    current_page = paginator.page(int(page))
    if category_slug:
        category = get_object_or_404(Book,
                                     slug=category_slug)
        products = books.filter(category=category)
        paginator = Paginator(products, 10)
        current_page = paginator.page(int(page))
    return render(request,
                  'main/product/list.html',
                  {'author': author,
                   'authors': authors,
                   'products': current_page,
                   'slug_url': category_slug})
