from django.contrib import admin
from django.urls import path
from .views import home, signup
from .views.home import Store
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView, PlaceOrder
from .views.profile import Profile
from .views.comments import Comments
from .middlewares.auth import auth_middleware
from .views.payment import Payment

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='check-out'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('profile', Profile.as_view(), name='profile'),
    path('comments', Comments.as_view(), name='comments'),
    path('store', Store.as_view(), name='store'),
    path('place_order', PlaceOrder.as_view(), name='place_order'),
    path('success', Payment.as_view(), name = 'success')

]
