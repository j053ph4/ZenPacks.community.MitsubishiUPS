from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "MitsubishiUPS"
VERSION = Version(1, 1, 1)

DefinitionInput = type('DefinitionInput', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'MitsubishiUPSInput',
        'componentData' : {
                           'singular': 'Input',
                           'plural': 'Inputs',
                           },
        'componentMethods' : [],                                    
        }
)


DefinitionBypass = type('DefinitionBypass', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'MitsubishiUPSBypass',
        'componentData' : {
                           'singular': 'Bypass',
                           'plural': 'Bypasses',
                           },
        'componentMethods' : [],                               
        }
)

DefinitionOutput = type('DefinitionOutput', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'MitsubishiUPSOutput',
        'componentData' : {
                           'singular': 'Output',
                           'plural': 'Outputs',
                           },
        'componentMethods' : [],                                               
        }
)


