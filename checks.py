# checks.py - this module will be where to place python to monit checks code
# Jason Graham 9/28/2017
import sys
import os
from django.conf import settings
import urllib
import urllib2
import httplib
import logging

logger = logging.getLogger(__name__)

#check if monit site is up on 'hosturl'
def checkMonitAlive(url):
    if url:
	#print 'checking: '+url
	response = None
        username = settings.MONIT_USER
        password = settings.MONIT_PASSWORD

        p = urllib2.HTTPPasswordMgrWithDefaultRealm()

        p.add_password(None, url, username, password)

        handler = urllib2.HTTPBasicAuthHandler(p)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)

        try: 
            response = urllib2.urlopen(url)
            #divtext = divtext + '<div><b>Host '
            #divtext = divtext + hosts[i]
            #divtext = divtext + '</b><p><pre>'
            #divtext = divtext + response.read()
            #divtext = divtext + '</pre>'
            #divtext = divtext + '</div>'

        except urllib2.HTTPError, e:
            logger.error('HTTPError = ' + str(e.code))
        except urllib2.URLError, e:
            logger.error('URLError = ' + str(e.reason))
        except httplib.HTTPException, e:
            logger.error('HTTPException')
        except Exception:
            import traceback
            logger.error('generic exception: ' + traceback.format_exc())
            #divtext = '<div>'
            #divtext = divtext + '<b>Host '
            #divtext = divtext + hosts[i]
            #divtext = divtext + '</b><p><pre>'
            #divtext = divtext + "<b>status: Login denied, unmonitored or DOWN"
            #divtext = divtext + '</pre>'
            #divtext = divtext + '</div>'
	    return 0

        return response 

#check host pings on the network..
def checkPing(hostip):
    response = os.system("ping -c 1 -w2 " + hostip + " > /dev/null 2>&1")

    #check the response...
    if response == 0:
        return 1
    else:
        return 0
