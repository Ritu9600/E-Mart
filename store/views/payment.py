from .orders import Order
from store.templatetags.custom_filter import currency
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
keyid = 'rzp_test_7EVKMKdtLNB2Tm'
keySecret = 'MnTN377Ey5AtfD7XIDkgvpH3'
import razorpay


def payment(request):
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_7EVKMKdtLNB2Tm', 'MnTN377Ey5AtfD7XIDkgvpH3'))
        payment = client.order.create({
            'amount': amount, 'currency': 'INR', 'payment_capture': '1'
        })
    return render(request, 'success.html')


@csrf_exempt
def success(request):
    return render(request, 'success.html')

class Payment(View):
   def get(self, request):
        return render(request, 'success.html')


