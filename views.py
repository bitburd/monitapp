# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import RedirectView
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import urllib2
from django.conf import settings
from django.template import Template, Context
import httplib
import logging
import checks 
import widgets
from django.contrib.auth.models import User

loginusername = 'guest'

def home(request):
    return render_to_response('index.htm',{},RequestContext(request))

def monit(request):
    return render_to_response('monit.htm',{},RequestContext(request))



#renders a status page and section for each monit host avaliable
def status(request):
    if request.user.is_authenticated():
        loginusername = request.user.username
    hosts = settings.MONIT_HOSTS
    host = '' 
    divtext = ''

    #setup python loging
    logger = logging.getLogger(__name__)

    #using templates from the filesystem.
    fp = open(settings.PROJECT_PATH + '/monitapp/templates/monit.htm')
    t = Template(fp.read())
    fp.close()
    i = 0

    #add opened template file to the renderer
    templtext = t.render(Context({'hosts': hosts[i]}))

    #try except for all hosts in array
    try:
        for host in hosts:
	    print 'host: ' + host
 
            #render to view results from MONIT_HOSTS array
            url = 'http://'
            url = url + hosts[i]
            url = url + ':2812/_status'

            response = checks.checkMonitAlive(url)

            #render this html for each host div:
            hidebtn = '<div><input id="hide'+host+'" type="button" width=50px height=15px onClick="reloadWindow(\'host'+host+'\'); hideShowDiv(\''+host+'\');"> Host '+host

	    if (response != None) or (response > 0):
		divtext = divtext + '<hr width=100% noshade></hr><br>'
		divtext = divtext + hidebtn
		divtext = divtext + widgets.statusBox('online',host)+'</div><br>'
                divtext = divtext + '<div id="host'+host+'"><pre>'
		#insert the monit API reponse text to a div..
                divtext = divtext + response.read()
                divtext = divtext + '</pre>'
                divtext = divtext + '</div>'
            else:
                divtext = divtext + '<hr width=100% noshade></hr><br>'
		divtext = divtext + hidebtn
                divtext = divtext + widgets.statusBox('offline', host)+'</div><br>'
                divtext = divtext + '<div id="host'+host+'"><pre>'
		#machine or monit was offline so add that to the div..
                divtext = divtext + 'Offline or not monitored'
                divtext = divtext + '</pre>'
                divtext = divtext + '</div>'

	    i = i+1

    except IndexError:
        hosts = 'null'
        print 'WARNING: no hosts found to check! please add them to MONIT_HOSTS in settings.py'

    #finish the page and the divs section..
    divtext = divtext +  '</div>'
    templtext = templtext + divtext
    templtext = templtext + '<script>hideShowAll("show");</script>'
    templtext = templtext + '</body></html>'

    return HttpResponse(templtext)


 
#this index page is not really used 
def index(request):
    return render_to_response('index.htm',{},RequestContext(request))



def dashboard(request):
    pagetext = 'dashboard.htm';

    return HttpResponse(pagetext)

def loginapp(request):
    return render_to_response('login.htm',{},RequestContext(request))

def adm(request):
    return render_to_response('monit-adm.htm',{},RequestContext(request))
