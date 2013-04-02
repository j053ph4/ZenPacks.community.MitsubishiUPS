from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.MitsubishiUPS.Definition import *

class MitsubishiUPSBypassMap(SnmpPlugin):
    ''''''
    compname = "os"
    constr = Construct(DefinitionBypass)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpGetTableMaps = (
        GetTableMap('upsBypassTable', '.1.3.6.1.4.1.13891.101.5.3.1', {
            '.1' : 'bypassindex',
            '.2' : 'bypassvoltage',
            }),
        )
    
    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        snmptable = tabledata.get("upsBypassTable")
        for key,value in snmptable.items():
            value['snmpindex'] = key
            om = self.objectMap(value)
            name = "%s_%s" % (self.baseid, str(key))
            om.id = self.prepId(name)
            om.title = name
            rm.append(om)
        maps.append(rm)
        return maps
