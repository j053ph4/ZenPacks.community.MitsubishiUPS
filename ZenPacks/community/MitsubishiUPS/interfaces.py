from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version

if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class IMitsubishiUPSBypassInfo(IComponentInfo):
    ''''''



class IMitsubishiUPSFacade(IFacade):
    ''''''

    def addMitsubishiUPSBypass(self, ob, **kwargs):
        ''''''


