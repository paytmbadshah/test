from django.db import models

# Create your models here.

class website_settings(models.Model):
    web_name = models.CharField(max_length=500)
    def __str__(self):
        return self.web_name


class website_menu(models.Model):
    menu_item = models.CharField(max_length=500)
    web_name = models.ForeignKey(website_settings, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.menu_item)


class website_banner_image(models.Model):
    ban_image1 = models.ImageField(upload_to='banner',blank=True,null=True,default='banner/download.jpg')
    ban_image2 = models.ImageField(upload_to='banner',blank=True,null=True,default='banner/download.jpg')
    ban_image3 = models.ImageField(upload_to='banner', blank=True, null=True, default='banner/download.jpg')
    web_name = models.ForeignKey(website_settings,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.web_name)

class website_content_image(models.Model):
    ban_image1 = models.ImageField(upload_to='content_image',blank=True,null=True,default='banner/download.jpg')
    ban_image2 = models.ImageField(upload_to='content_image',blank=True,null=True,default='banner/download.jpg')
    ban_image3 = models.ImageField(upload_to='content_image',blank=True,null=True,default='banner/download.jpg')
    ban_image4 = models.ImageField(upload_to='content_image',blank=True,null=True,default='banner/download.jpg')
    ban_image5 = models.ImageField(upload_to='content_image',blank=True,null=True,default='banner/download.jpg')
    ban_image6 = models.ImageField(upload_to='content_image',blank=True,null=True,default='banner/download.jpg')
    web_name = models.ForeignKey(website_settings,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.web_name)

class website_footer_settings(models.Model):
    contact_number = models.CharField(max_length=500)
    email_id = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    web_name = models.ForeignKey(website_settings,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.web_name)


