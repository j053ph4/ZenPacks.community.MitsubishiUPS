from ZenPacks.community.ConstructionKit.ClassHelper import *

def MitsubishiUPSBypassgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class MitsubishiUPSBypassInfo(ClassHelper.MitsubishiUPSBypassInfo):
    ''''''

def MitsubishiUPSInputgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class MitsubishiUPSInputInfo(ClassHelper.MitsubishiUPSInputInfo):
    ''''''

def MitsubishiUPSOutputgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class MitsubishiUPSOutputInfo(ClassHelper.MitsubishiUPSOutputInfo):
    ''''''


