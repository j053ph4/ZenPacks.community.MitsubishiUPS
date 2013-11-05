from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "MitsubishiUPS"
VERSION = Version(1, 1, 0)

DATA = {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'MitsubishiUPSInput',
        'componentData' : {
                           'singular': 'Input',
                           'plural': 'Inputs',
                           },
        }
DefinitionInput = type('DefinitionInput', (BasicDefinition,), DATA)


DATA = {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'MitsubishiUPSBypass',
        'componentData' : {
                           'singular': 'Bypass',
                           'plural': 'Bypasses',
                           },
        }
DefinitionBypass = type('DefinitionBypass', (BasicDefinition,), DATA)

DATA = {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'MitsubishiUPSOutput',
        'componentData' : {
                           'singular': 'Output',
                           'plural': 'Outputs',
                           },
        }
DefinitionOutput = type('DefinitionOutput', (BasicDefinition,), DATA)


