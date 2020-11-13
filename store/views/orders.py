from django.shortcuts import render

from django.views import View


class OrderView(View):

    @staticmethod
    def get(request):
        customer = request.session.get('customer')
        orders = OrderView.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders})

