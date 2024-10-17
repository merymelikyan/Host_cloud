from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    TrustedMain,
    Trusted,
    HostingMain,
    HostingServices,
    HostingService1,
    CloudMain,
    CloudPlans,
    FeaturesMain,
    FeaturesBlocks,
    Testimonials,
    TestimonialsBlocks,
    AboutUs,
    FooterNames,
    HostingPlans,
    UsefulLinks,
    MoreInformation,
    About,
    Background,
    WorkTabs,
    OurWork,
    OurTeam,
    Members,
    Contact,
    ContactMain,
    ContactInfo,
    Services,
    ServicesMain,
    ServicesBlocks

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
          "cloud_main":  CloudMain.objects.all().first(),
          "cloud_plans": CloudPlans.objects.all(),
          "features_main": FeaturesMain.objects.all().first(),
          "features_blocks": FeaturesBlocks.objects.all(),
          "testimonials": Testimonials.objects.all().first(),
          "testimonials_blocks": TestimonialsBlocks.objects.all(),
          "footer_names": FooterNames.objects.all(),
          "about_us": AboutUs.objects.all().first(),
          "hosting_plans": HostingPlans.objects.all(),
          "useful_links": UsefulLinks.objects.all(),
          "more_information": MoreInformation.objects.all()
          
      }      

    return render(request,"home.html" , context)


def about(request):
    context = {
        "about": About.objects.all().first(),
        "body": About.objects.all(),
        "background": Background.objects.all().first(),
        "work_tabs": WorkTabs.objects.all(),
        "our_work": OurWork.objects.all(),
        "our_team": OurTeam.objects.all().first(),
        "members": Members.objects.all(),
        "testimonials": Testimonials.objects.first(),
        "testimonials_blocks": TestimonialsBlocks.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "footer_names": FooterNames.objects.all(),
        "about_us": AboutUs.objects.all().first(),
        "hosting_plans": HostingPlans.objects.all(),
        "useful_links": UsefulLinks.objects.all(),
        "more_information": MoreInformation.objects.all()
    }
    return render(request, "about.html", context)


def contact(request):
    context = {
        "contact": Contact.objects.all().first(),
        "contact_main": ContactMain.objects.all().first(),
        "contact_info": ContactInfo.objects.all(),
        "testimonials": Testimonials.objects.first(),
        "testimonials_blocks": TestimonialsBlocks.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "footer_names": FooterNames.objects.all(),
        "about_us": AboutUs.objects.all().first(),
        "hosting_plans": HostingPlans.objects.all(),
        "useful_links": UsefulLinks.objects.all(),
        "more_information": MoreInformation.objects.all()
    }
    return render(request, "contact.html", context)
             

def services(request):
    context = {
        "services": Services.objects.all().first(),
        "services_main": ServicesMain.objects.all().first(),
        "services_blocks": ServicesBlocks.objects.all(),
        "testimonials": Testimonials.objects.first(),
        "testimonials_blocks": TestimonialsBlocks.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "footer_names": FooterNames.objects.all(),
        "about_us": AboutUs.objects.all().first(),
        "hosting_plans": HostingPlans.objects.all(),
        "useful_links": UsefulLinks.objects.all(),
        "more_information": MoreInformation.objects.all()
    }
    return render(request, "services.html", context)
        
