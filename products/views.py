from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import BaseListView, MultipleObjectTemplateResponseMixin

from products.models import Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Get specific product"""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products:product-detail')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])


class ProductListView(LoginRequiredMixin, MultipleObjectTemplateResponseMixin,  BaseListView):
    """Get list of products"""
    model = Product
    # list_filter_class = 'put here some Filter class you created in filter.py'
    template_name = 'products/product_list.html'
    success_url = reverse_lazy('products:product-list')

    def get_queryset(self):
        return self.model.objects.all()
