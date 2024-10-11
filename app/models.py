from django.db import models

class HeaderText (models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    
 
    def __str__(self):
        return self.title

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
