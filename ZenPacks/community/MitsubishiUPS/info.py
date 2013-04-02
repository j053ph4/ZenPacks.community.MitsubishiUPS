from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.MitsubishiUPS.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class MitsubishiUPSBypassInfo(ComponentInfo):
    implements( IMitsubishiUPSBypassInfo )


