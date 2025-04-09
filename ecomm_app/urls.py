
from django.urls import path
from ecomm_app import views
from django.conf.urls.static import static
from ecomm import settings

urlpatterns = [
    
    path('home1',views.home),
    path('home',views.home),
    path('about',views.about),
    path('pdetails/<pid>',views.pdetails),
    path('viewcart',views.viewcart),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('range',views.range),
    path('sort/<sv>',views.sort),
    path('addtocart/<pid>',views.addtocart),
    path('remove/<cid>',views.remove),
    path('remove1/<oid>',views.remove1),
    path('placeorder',views.placeorder),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('makepayment',views.makepayment),
    path('sendmail',views.sendmail),
    path('verify_payment/', views.verify_payment, name='verify_payment'),


    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
