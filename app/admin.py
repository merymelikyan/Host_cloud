from django.contrib import admin


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
    MoreInformation
    
 
) 
  
admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(TrustedMain)
admin.site.register(Trusted)
admin.site.register(HostingMain)
admin.site.register(HostingServices)
admin.site.register(HostingService1)
admin.site.register(CloudMain)
admin.site.register(CloudPlans)
admin.site.register(FeaturesMain)
admin.site.register(FeaturesBlocks)
admin.site.register(Testimonials)
admin.site.register(TestimonialsBlocks)
admin.site.register(AboutUs)
admin.site.register(FooterNames)
admin.site.register(HostingPlans)
admin.site.register(UsefulLinks)
admin.site.register(MoreInformation)



