# # from django.urls import path
# # from . import views

# # app_name = "base"

# # urlpatterns = [

# #     path("", views.home, name="home"),
# #     path("signup/", views.authView, name="authView"),
# #     # path("cart/", views.cart_view, name="cart"),
# #     # path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
# #     # path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
# #     # path("cart/clear/", views.clear_cart, name="clear_cart"),
# #     # path("api/cart/", views.cart_api_view, name="cart_api"),
# #     # path("api/cart/add/<int:product_id>/", views.add_to_cart_api, name="add_to_cart_api"),
# #     # path("api/cart/remove/<int:product_id>/", views.remove_from_cart_api, name="api_remove_from_cart"),
# #     # path("api/cart/update/<int:product_id>/", views.update_cart_quantity, name="api_update_cart"),
# #     # path("api/cart/clear/", views.clear_cart_api, name="api_clear_cart"),
# #     path('cart/', views.cart_view, name='cart'),
# #     path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
# #     path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
# #     path('clear/', views.clear_cart, name='clear_cart'),
# #     path('update/<int:product_id>/<str:action>/', views.update_cart, name='update_cart'),
# # ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.home, name="home" ),
#     path("signup/", views.authView, name="authView"),
#     path("cart/", views.cart_view, name="cart_view"),
#     path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
#     path("cart/update/<int:product_id>/<str:action>/", views.update_quantity, name="update_quantity"),
#     path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
#     path("cart/clear/", views.clear_cart, name="clear_cart"),
# ]
# from django.urls import path
# from . import views

# app_name = "base"  

# urlpatterns = [
#     path("", views.home, name="home"),
#     path("signup/", views.authView, name="authView"),
#     path("products/", views.product_list, name="product_list"),
#     path("cart/", views.cart_view, name="cart_view"),
#     path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
#     path("cart/update/<int:product_id>/<str:action>/", views.update_quantity, name="update_quantity"),
#     path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
#     path("cart/clear/", views.clear_cart, name="clear_cart"),
# ]
# base/urls.py
from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.product_list, name="product_list"),
    path("signup/", views.authView, name="authView"),
    path("cart/", views.cart_view, name="cart_view"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("update-quantity/<int:product_id>/<str:action>/", views.update_quantity, name="update_quantity"),
    path("remove-from-cart/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("clear-cart/", views.clear_cart, name="clear_cart"),
]

