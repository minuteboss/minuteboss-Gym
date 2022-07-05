from django.urls import path
from .views import home,page_detail,checkout,signup,enquiry,gallery,faq_list,gallery_detail,pricing
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('enquiry/',enquiry,name='enquiry'),
    path('faq/',faq_list,name='faq_list'),
    path('detail/<int:id>/',page_detail,name='page_detail'),
    path('home/',home,name='home'),
    path('accounts/signup',signup,name='signup'),
    path('gallery/',gallery,name='gallery'),
    path('pricing/',pricing,name='pricing'),
    path('checkout/<int:plan_id>/',checkout,name='checkout'),
    path('gallerydetail/<int:id>/',gallery_detail,name='gallery_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)