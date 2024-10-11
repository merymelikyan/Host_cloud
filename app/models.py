from django.db import models

class HeaderText (models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    
 
    def __str__(self):
        return f"{self.title1} {self.title2}"

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Texts"

 
class FooterText(models.Model):
    title = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
      return self.title

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"


class TrustedMain(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Trusted Main"
        verbose_name_plural = "Trusted Main"


class Trusted(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="trusted")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Trusted"
        verbose_name_plural = "Trusted"


class HostingMain(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Hosting Main"
        verbose_name_plural = "Hosting Main"


class HostingServices(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hosting Services"
        verbose_name_plural = "Hosting Services"


class HostingService1(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255)
    description2 = models.CharField(max_length=255)
    description3 = models.CharField(max_length=255)
    link_url = models.URLField(max_length=200, blank=True, null=True) 


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hosting Service1"
        verbose_name_plural = "Hosting Service1"



class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class FooterNames(models.Model):
    title = models.CharField(max_length=55)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer Names"
        verbose_name_plural = "Footer Names"


class HostingPlans(models.Model):
    link_url = models.CharField(max_length=200, blank=True, null=True) 
    link_name = models.CharField(max_length=255, blank=True, null=True)
  

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name = "Hosting Plans"
        verbose_name_plural = "Hosting Plans"



class UsefulLinks(models.Model):
    link_url = models.CharField(max_length=200, blank=True, null=True) 
    link_name = models.CharField(max_length=255, blank=True, null=True)
  

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name = "Useful Links"
        verbose_name_plural = "Useful Links"



class MoreInformation(models.Model):
    title = models.CharField(max_length=255)
    link_url = models.CharField(max_length=200, blank=True, null=True) 
    link_name = models.CharField(max_length=255, blank=True, null=True)
  

    def __str__(self):
       return self.title

    class Meta:
        verbose_name = "More Information"
        verbose_name_plural = "More Information"


