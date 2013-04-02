from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul

'''
args: routername,adaptername,routerMethodName, createMethodName
'''

class MitsubishiUPSRouter(DirectRouter):
    def _getFacade(self):
    	return Zuul.getFacade('MitsubishiUPSAdapter', self.context)
    


    def addMitsubishiUPSBypassRouter(self, **kwargs):
    	from Products.ZenUtils.Ext import DirectResponse
    	facade = self._getFacade()
    	ob = self.context
    	success, message = facade.addMitsubishiUPSBypass(ob, **kwargs)
    	if success:
    		return DirectResponse.succeed(message)
    	else:
    		return DirectResponse.fail(message)

