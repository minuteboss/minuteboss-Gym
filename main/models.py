from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

#banners
class Banners(models.Model):
    img=models.ImageField(upload_to="banners/")
    alt_text=models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))

class Service(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    img=models.ImageField(upload_to="services/",null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))

#pages
class Page(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField()

    def __str__(self):
        return self.title  

#FAQ
class Faq(models.Model):
    question=models.TextField()
    answer=models.TextField()

    def __str__(self):
        return self.question   

    def __str__(self):
        return self.answer\

   

#Enquiry
class Enquiry(models.Model):
    full_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    detail=models.TextField()
    send_time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

#Gallery model
class Gallery(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    img=models.ImageField(upload_to="gallery/",null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))

#gallery images
class GalleryImage(models.Model):
    gallery=models.ForeignKey(Gallery,on_delete=models.CASCADE,null=True)
    alt_text=models.CharField(max_length=150)
    img=models.ImageField(upload_to="gallery_imgs/",null=True)

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))

#subscription plan
class SubPlan(models.Model):
    title=models.CharField(max_length=150)
    price=models.IntegerField()
    max_members=models.IntegerField(null=True)
    highlight_status=models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.title

#subscription plan features    
class SubPlanFeatures(models.Model):
    #subplan=models.ForeignKey(SubPlan,on_delete=models.CASCADE)
    subplan=models.ManyToManyField(SubPlan)
    title=models.CharField(max_length=150)
    
    def __str__(self):
        return self.title

#package discount
class PlanDiscount(models.Model):
    subplan=models.ForeignKey(SubPlan,on_delete=models.CASCADE)
    total_months=models.IntegerField()
    total_discount=models.IntegerField()

    def __str__(self):
        return str(self.total_months)

#subscriber
class Subscriber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    img=models.ImageField(upload_to="gallery_imgs/",null=True)
    
    
    def __str__(self):
        return str(self.subs)

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' % (self.img.url))

#subscription
class Subscription(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    plan=models.ForeignKey(SubPlan,on_delete=models.CASCADE)
    price=models.CharField(max_length=50)
    