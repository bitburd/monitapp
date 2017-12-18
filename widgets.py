from django.conf import settings
import checks

#populate widget div with status box
def statusBox(status,host):
    statusstr = "<img src=http://10.0.0.244/monitapp/images/sidewaystrafficnomonitor.png border=0>"
    if status == 'online':
            statusstr = "<img src=http://10.0.0.244/monitapp/images/sidewaystrafficgreen.png border=0>"
    else:
        statusstr = "<img src=http://10.0.0.244/monitapp/images/sidewaystrafficred.png border=0>"

    return statusstr
    
