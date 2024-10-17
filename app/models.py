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



class CloudMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cloud Main"
        verbose_name_plural = "Cloud Main"


class CloudPlans(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=40, blank=True, null=True)
    duration = models.CharField(max_length=255)
    space = models.CharField(max_length=255)
    transfer = models.CharField(max_length=255)
    panel = models.CharField(max_length=255)
    support = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    upgrading = models.CharField(max_length=255)
    button_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cloud Plan"
        verbose_name_plural = "Cloud Plans"



class FeaturesMain(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Feutares Main"
        verbose_name_plural = "Feutares Main"



class FeaturesBlocks(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="features_blocks", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Features Blocks"
        verbose_name_plural = "Features Blocks"



class Testimonials(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"



class TestimonialsBlocks(models.Model):
    name= models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255, blank=True, null=True)
   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonials Blocks"
        verbose_name_plural = "Testimonials Blocks"




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


class About(models.Model):
    tag = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
     
               


class Background(models.Model):
    tag = models.CharField(max_length=55, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Background"
        verbose_name_plural = "Background"     

        
class WorkTabs(models.Model):
    link_url = models.CharField(max_length=200, blank=True, null=True) 
    link_name = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.link_name}"

    class Meta:
        verbose_name = "Work Tabs"
        verbose_name_plural = "Work Tabs"     


class OurWork(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Our Work"
        verbose_name_plural = "Our Work"    


class OurTeam(models.Model):
    tag = models.CharField(max_length=55, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Our Team"
        verbose_name_plural = "Our Team"   


class Members(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    position = models.CharField(max_length=55)
    img = models.ImageField(upload_to="member")

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.position}"

    class Meta:
        verbose_name = "Members"
        verbose_name_plural = "Members"     


class Contact(models.Model):
    tag = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    
    def __str__(self):
         return f"{self.tag}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"   

        
class ContactMain(models.Model):
    tag = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "Contact Main"
        verbose_name_plural = "Contact Main"        


class ContactInfo(models.Model):
    title1 = models.CharField(max_length=255, blank=True, null=True)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    html_class1 = models.CharField(max_length=255, blank=True, null=True)
    html_class2 = models.CharField(max_length=255, blank=True, null=True)
    html_name1 = models.CharField(max_length=255, blank=True, null=True)
    html_name2 = models.CharField(max_length=255, blank=True, null=True)
   
    
    def __str__(self):
        return f"{self.title1} , {self.title2}"

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"


class Services(models.Model):
    tag = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    
    def __str__(self):
         return f"{self.tag}"

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services" 


        
class ServicesMain(models.Model):
    tag = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "Services Main"
        verbose_name_plural = "Services Main"  


class ServicesBlocks(models.Model):
    class_name = models.CharField(max_length=55)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Services Blocks"
        verbose_name_plural = "Services Blocks" 