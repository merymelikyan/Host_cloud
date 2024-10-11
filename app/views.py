from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,

     
)    
 
def index(request):
    context = {
          "header_text": HeaderText.objects.all(),
          "footer_text": FooterText.objects.all().first(),
         
          
      }      

    return render(request,"base.html" , context)