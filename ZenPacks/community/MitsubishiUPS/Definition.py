from ZenPacks.community.ConstructionKit.Construct import *
from Products.ZenModel.migrate.Migrate import Version
import os

class DefinitionInput():
    """
    """
    version = Version(1, 0, 0)
    zenpackroot = "ZenPacks.community" # ZenPack Root
    zenpackbase = "MitsubishiUPS" # ZenaPack Name
    #dictionary of components
    component = 'MitsubishiUPSInput'
    componentData = {
                  'singular': 'Input',
                  'plural': 'Inputs',
                  'displayed': 'id', # component field in Event Console
                  'primaryKey': 'id',
                  'properties': {},
                  }
    
    packZProperties = []
    #dictionary of datasources
    addManual = False
    createDS = False
    provided = False
    cycleTime = 300
    timeout = 60
    cmdFile = None
    datapoints = []
    cwd = os.path.dirname(os.path.realpath(__file__)) # ZenPack files directory
    
class DefinitionBypass():
    """
    """
    version = Version(1, 0, 0)
    zenpackroot = "ZenPacks.community" # ZenPack Root
    zenpackbase = "MitsubishiUPS" # ZenaPack Name
    #dictionary of components
    component = 'MitsubishiUPSBypass'
    componentData = {
                  'singular': 'Bypass',
                  'plural': 'Bypasses',
                  'displayed': 'id', # component field in Event Console
                  'primaryKey': 'id',
                  'properties': {},
                  }
    
    packZProperties = []
    #dictionary of datasources
    addManual = False
    createDS = False
    provided = False
    cycleTime = 300
    timeout = 60
    cmdFile = None
    datapoints = []
    cwd = os.path.dirname(os.path.realpath(__file__)) # ZenPack files directory

class DefinitionOutput():
    """
    """
    version = Version(1, 0, 0)
    zenpackroot = "ZenPacks.community" # ZenPack Root
    zenpackbase = "MitsubishiUPS" # ZenaPack Name
    #dictionary of components
    component = 'MitsubishiUPSOutput'
    componentData = {
                  'singular': 'Output',
                  'plural': 'Outputs',
                  'displayed': 'id', # component field in Event Console
                  'primaryKey': 'id',
                  'properties': {},
                  }
    
    packZProperties = []
    #dictionary of datasources
    addManual = False
    createDS = False
    provided = False
    cycleTime = 300
    timeout = 60
    cmdFile = None
    datapoints = []
    cwd = os.path.dirname(os.path.realpath(__file__)) # ZenPack files directory
