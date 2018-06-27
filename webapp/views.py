# from urllib import quote

from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import Product


def index_view(request):
    queryset_list = Product.objects.all()[:3] # .order_by("-timestamp")
    # search query
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        "title": "Home",
        "object_list": queryset_list
    }
    return render(request, 'index.html', context)


def contacts(request):
    context = {
        "title": "Home"
    }
    return render(request, 'contacts.html', context)


def gallery(request):
    context = {
        "title": "Home"
    }
    return render(request, 'gallery.html', context)


def product_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "New Product",
        "form": form
    }
    return render(request, 'product_form.html', context)


def product_detail(request, pk):
    queryset_list = Product.objects.all()  # .order_by("-timestamp")
    # search query
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 4)  # Show 4 items per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    instance = get_object_or_404(Product, id=pk)
    # share_string = quote(instance.content)
    context = {
        "title": "Detail",
        "object_list": queryset,
        "page_request_var": page_request_var,
        "product": instance,
        # "share_string": share_string
    }
    return render(request, 'product_detail.html', context)


def product_list(request):
    queryset_list = Product.objects.all()  # .order_by("-timestamp")
    # search query
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 4)  # Show 4 items per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "title": "Shop",
        "object_list": queryset,
        "page_request_var": page_request_var
    }
    return render(request, 'shop.html', context)

# review this and debug

def product_category(request, cat):
    #     queryset_list = Product.objects.filter(tag=cat)  # .order_by("-timestamp")
    #     # search query
    #     query = request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(title__icontains=query) |
    #             Q(content__icontains=query)
    #         ).distinct()
    #     paginator = Paginator(queryset_list, 9)  # Show 9 items per page
    #     page_request_var = 'page'
    #     page = request.GET.get(page_request_var)
    #     try:
    #         queryset = paginator.page(page)
    #     except PageNotAnInteger:
    #         queryset = paginator.page(1)
    #     except EmptyPage:
    #         queryset = paginator.page(paginator.num_pages)
    #     instance = get_object_or_404(Product, tag=cat)
    #     # share_string = quote(instance.content)
        context = {
            "title": "Detail",
                # "object_list": queryset,
                # "page_request_var": page_request_var,
                # "product": instance,
                # # "share_string": share_string
        }
        return render(request, 'shop.html', context)


def product_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Product, id=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully updated")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "product": instance,
        "form": form,
        "title": "Update"
    }
    return render(request, 'product_form.html', context)


def product_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Product, id=pk)
    instance.delete()
    # context = {
    #     "title": "Delete product"
    # }
    messages.success(request, "Successfully deleted")
    return redirect("list")
