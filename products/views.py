from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import BaseListView, MultipleObjectTemplateResponseMixin

from basket.models import Basket, BasketItem
from products.models import Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Get specific product"""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products:product-detail')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])


class AddToBasketView(LoginRequiredMixin, View):
    """add to logic to add item to basket"""
    def post(self, request, pk):
        basket, _ = Basket.objects.get_or_create(user=request.user, is_active=True)
        product = get_object_or_404(Product, id=pk)
        basket_item, created = basket.items.get_or_create(product=product)
        if not created:
            basket_item.quantity += 1
            basket_item.save()
            messages.info(request, "This item quantity was updated.")
        else:
            messages.info(request, "This item was added to your basket.")
            pass
        return redirect("products:product-detail", pk)


class ProductListView(LoginRequiredMixin, MultipleObjectTemplateResponseMixin, BaseListView):
    """Get list of products"""
    model = Product
    # list_filter_class = 'put here some Filter class you created in filter.py'
    template_name = 'products/product_list.html'
    success_url = reverse_lazy('products:product-list')

    def get_queryset(self):
        return self.model.objects.all()
