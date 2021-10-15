"""online_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from buyer import views as buyer_view
from seller import views as seller_view
from Admin import views as admin_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',admin_view.index,name='index'),
    url(r'^register/',seller_view.register, name='register'),
    url(r'^registerAction/',seller_view.registerAction, name='registerAction'),
    url(r'^register1/',buyer_view.register1, name='register1'),
    url(r'^registerAction1/',buyer_view.registerAction1, name='registerAction1'),
    url(r'^login/',admin_view.login, name='login'),
    url(r'^loginAction/',admin_view.loginAction, name='loginAction'),
    url(r'^catagory/',admin_view.catagory, name='catagory'),
    url(r'^catagoryAction/',admin_view.catagoryAction, name='catagoryAction'),
    url(r'^ViewSellers/',admin_view.ViewSellers, name='ViewSellers'),
    url(r'^approve/(?P<uid>\d+)/$',admin_view.approve, name='approve'),
    url(r'^deny/(?P<uid>\d+)/$',admin_view.deny, name='deny'),
    url(r'^deleteUser/(?P<uid>\d+)/$',admin_view.deleteUser, name='deleteUser'),
    url(r'addProduct/',seller_view.addProduct, name='addProduct'),
    url(r'^addProductAction/',seller_view.addProductAction, name='addProductAction'),
    url(r'^myProducts/',seller_view.myProducts, name='myProducts'),
    url(r'^delete/(?P<uid>\d+)/$',seller_view.delete, name='delete'),
    url(r'^update/(?P<uid>\d+)/$',seller_view.update, name='update'),
    url(r'^updateAction/',seller_view.updateAction, name='updateAction'),
    url(r'^productsAvailable/',buyer_view.productsAvailable, name='productsAvailable'),
    url(r'^add_to_cart/(?P<uid>\d+)/$',buyer_view.add_to_cart, name='add_to_cart'),
    url(r'^add_to_cart_action/',buyer_view.add_to_cart_action, name='add_to_cart_action'),
    url(r'^viewCart/',buyer_view.viewCart, name='viewCart'),
    url(r'^cartAction/',buyer_view.cartAction, name='cartAction'),
    url(r'^ordered/',buyer_view.ordered, name='ordered'),
    url(r'^viewOrders/',seller_view.viewOrders, name='viewOrders'),
    url(r'^approveOrder/(?P<uid>\d+)/$',seller_view.approveOrder, name='approveOrder'),
    url(r'^denyOrder/(?P<uid>\d+)/$',seller_view.denyOrder, name='denyOrder'),
    url(r'^cancelOrder/(?P<uid>\d+)/$',buyer_view.cancelOrder, name='cancelOrder'),
    url(r'^cancelVerification/(?P<uid>\d+)/$',seller_view.cancelVerification, name='cancelVerification'),
    url(r'^deleteCart/(?P<uid>\d+)/$',buyer_view.deleteCart, name='deleteCart'),
    url(r'^searchProduct/',buyer_view.searchProduct,name='searchProduct'),
    url(r'^productResults/',buyer_view.productResults,name='productResults'),
    url(r'^sortProducts/',buyer_view.sortProducts, name='sortProducts'),
    url(r'^sortAction/',buyer_view.sortAction,name='sortAction'),
    url(r'^updateBuyerProfile/',buyer_view.updateBuyerProfile,name='updateBuyerProfile'),
    url(r'^updateProfileAction/',buyer_view.updateProfileAction,name='updateProfileAction'),
    url(r'^updateSellerProfile/',seller_view.updateSellerProfile,name='updateSellerProfile'),
    url(r'^updateSellerProfileAction/',seller_view.updateSellerProfileAction,name='updateSellerProfileAction'),
    url(r'^forgotPassword/',admin_view.forgotPassword,name='forgotPassword'),
    url(r'^forgotPasswordAction/',admin_view.forgotPasswordAction,name='forgotPasswordAction'),
    url(r'^buyerRecoveryPasswordAction/',admin_view.buyerRecoveryPasswordAction,name='buyerRecoveryPasswordAction'),
    url(r'^sellerRecoveryPasswordAction/',admin_view.sellerRecoveryPasswordAction,name='sellerRecoveryPasswordAction'),
    url(r'^adminRecoveryPasswordAction/',admin_view.adminRecoveryPasswordAction,name='adminRecoveryPasswordAction'),
    url(r'^buyerChangePasswordAction/',admin_view.buyerChangePasswordAction,name='buyerChangePasswordAction'),
    url(r'^sellerChangePasswordAction/',admin_view.sellerChangePasswordAction,name='sellerChangePasswordAction'),
    url(r'^trackingDetailsPage/(?P<uid>\d+)/$',seller_view.trackingDetailsPage,name='trackingDetailsPage'),
    url(r'^trackingDetailsfun/',seller_view.trackingDetailsfun,name='trackingDetailsfun'),
    url(r'^buyerTrackingDetails/(?P<uid>\d+)/$',buyer_view.buyerTrackingDetails,name='buyerTrackingDetails'),
    url(r'^logOut/',admin_view.logOut,name='logOut'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
