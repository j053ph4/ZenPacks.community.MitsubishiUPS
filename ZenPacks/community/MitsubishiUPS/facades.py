import os,re
import logging
log = logging.getLogger('zen.MitsubishiUPSFacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from MitsubishiUPSBypass import *
from .interfaces import *

class MitsubishiUPSFacade(ZuulFacade):
    implements(IMitsubishiUPSFacade)
 

    def addMitsubishiUPSBypass(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.MitsubishiUPS.MitsubishiUPSBypass import MitsubishiUPSBypass
        import re
        cid = 'mitsubishiupsbypass' 
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = MitsubishiUPSBypass(id)
        relation = target.os.mitsubishiUPSBypasss
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
    
    
    

    	return True, _t("Added Bypass for device " + target.id)

