from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.MitsubishiUPS.Definition import *

class MitsubishiUPSInputMap(SnmpPlugin):
    ''''''
    compname = "os"
    constr = Construct(DefinitionInput)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpGetTableMaps = (
        GetTableMap('upsInputTable', '.1.3.6.1.4.1.13891.101.3.3.1', {
            '.1' : 'inputindex',
            '.2' : 'inputfreq',
            '.3' : 'inputvoltage',
            '.4' : 'inputcurrent',
            '.5' : 'inputpower',
            }),
        )

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        snmptable = tabledata.get("upsInputTable")
        for key,value in snmptable.items():
            value['snmpindex'] = key
            om = self.objectMap(value)
            name = "%s_%s" % (self.baseid, str(key))
            om.id = self.prepId(name)
            om.title = name
            rm.append(om)
        maps.append(rm)
        return maps

