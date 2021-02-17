from django.shortcuts import render,redirect
from .models import anoshort
from django.http import HttpResponse
from django.contrib import messages
import random
import string
from django.template import RequestContext
from urlhandler.models import  shorturl
from django.urls import get_resolver
# Create your views here.

def randomgen():
     ran = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
     ran +='1'
     return ran







def anourlgen(request):
    short=None
    if request.method == "POST":
        # generate
        pass
        if request.POST['original'] and request.POST['short']:
            # generate based on user input
            restrict = ['admin','admin/','login','login/','signup','signup/','logout/','logout','dashboard/','dashboard','generate/','generate','deleteurl/','deleteurl','anogen/','anogen']
            original = request.POST['original']
            short = request.POST['short']
            for i in restrict:
                if(i==short):
                    messages.error(request, "Already Exists")
                    return redirect(anourlmain)
                else:
                    check = anoshort.objects.filter(short_query=short) or shorturl.objects.filter(short_query=short)
            if not check:
                newurl = anoshort(
                    
                    original_url=original,
                    short_query=short,
                )
                request.session['orignal_url']=original
                request.session['short_url']=short
                request.session.set_expiry(0)
                newurl.save()
                return redirect(anourlmain)
            else:
                messages.error(request, "Already Exists")
                return redirect(anourlmain)
        elif request.POST['original']:
            # generate randomly
            
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomgen()
                check = anoshort.objects.filter(short_query=short)
                if not check:
                    newurl = anoshort(
                        
                        original_url=original,
                        short_query=short,
                    )
                    request.session['orignal_url']=original
                    request.session['short_url']=short
                    request.session.set_expiry(0)
                    x=get_resolver().reverse_dict.keys()
                    print(x)
                    print('hey')
                    newurl.save()
                    return redirect(anourlmain)
                else:
                    continue
            
            the_id = request.session['anoshort_id']
        else:
            messages.error(request, "Empty Fields")
            return redirect(anourlmain)
    else:
        return redirect("/ano/anourl")




def anoredirect(request, query=None):
    if not query or query is None:
        return render(request, 'main.html')
    else:
        try:
            check = anoshort.objects.get(short_query=query)
            check.save()
            url_to_redirect = check.original_url
            return redirect(url_to_redirect)
        except shorturl.Meta:
            return render(request, '404.html', {'error': "error"})


def anourlmain(request):
    return render(request, 'main.html')







