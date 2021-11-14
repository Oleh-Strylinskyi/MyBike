from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import BaseListView, MultipleObjectTemplateResponseMixin

from basket.models import Basket, BasketItem


class RemoveBasketItemView(LoginRequiredMixin, View):
    def post(self, request, pk):
        basket, _ = Basket.objects.get_or_create(user=request.user, is_active=True)
        basket_item = get_object_or_404(BasketItem, id=pk)
        basket_item.delete()
        messages.info(request, "Товар було вилучено з кошика.")
        return redirect("basket:basket-list")


class BasketListView(LoginRequiredMixin, MultipleObjectTemplateResponseMixin, BaseListView):
    model = BasketItem
    template_name = 'basket/basket_list.html'
    success_url = reverse_lazy('basket:basket-items-list')

    def get_queryset(self):
        basket, _ = Basket.objects.get_or_create(user=self.request.user, is_active=True)
        return self.model.objects.filter(basket=basket.pk)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BasketListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['basket'] = Basket.objects.get(user=self.request.user, is_active=True)
        return context
