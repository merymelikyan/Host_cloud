from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    TrustedMain,
    Trusted,
    HostingMain,
    HostingServices,
    HostingService1,
    AboutUs,
    FooterNames,
    HostingPlans,
    UsefulLinks,
    MoreInformation
     
)    
 
def index(request):
    context = {
          "header_text": HeaderText.objects.all(),
          "footer_text": FooterText.objects.all().first(),
          "trusted_main": TrustedMain.objects.all().first(),
          "trusted": Trusted.objects.all(),
          "hosting_main": HostingMain.objects.all().first(),
          "hosting_services": HostingServices.objects.all(),
          "hosting_service1": HostingService1.objects.all().first(),
          "footer_names": FooterNames.objects.all(),
          "about_us": AboutUs.objects.all().first(),
          "hosting_plans": HostingPlans.objects.all(),
          "useful_links": UsefulLinks.objects.all(),
          "more_information": MoreInformation.objects.all()
          
      }      

    return render(request,"base.html" , context)