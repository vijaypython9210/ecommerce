from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home' ),
    path('reg',views.register,name='register'),
    path('login',views.loginPage,name='loginPage'),
    path('logout',views.logoutPage,name='logoutPage'),
    path('collection',views.collections,name='collections'),
    path('collection/<str:name>',views.collectionView,name='collectionView'),
    path('collection/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('addtocart',views.add_to_cart,name='addtocart'),
    path('viewcart',views.view_cart,name='viewcart'),
    path('removecart/<str:cid>',views.remove_cart,name='removecart'),
    path('fav',views.fav,name='fav'),
    path('viewfav',views.view_fav,name='viewfav'),
    path('removefav/<str:fid>',views.remove_fav,name='removefav')
]
