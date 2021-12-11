"""
========================================================================
        STARTUP SETTINGS
========================================================================
"""

from maya import cmds, utils, mel


if not cmds.about(batch=True):
    # Plugins
    # -----------------------------------------------------------------
    cmds.loadPlugin("matrixNodes", quiet=True)
    cmds.loadPlugin("meshReorder", quiet=True)
    cmds.loadPlugin("invertShape", quiet=True)
    cmds.loadPlugin("curveWarp", quiet=True)

    # Settings
    # -----------------------------------------------------------------
    cmds.help(popupMode=True, popupSimpleMode=False)
    cmds.optionVar(intValue=("inViewMessageEnable", 1))
    cmds.optionVar(intValue=("inViewMessageAssistEnable", 1))
    cmds.optionVar(intValue=("inViewMessageStatusEnable", 1))

    cmds.selectPref(trackSelectionOrder=1)
    cmds.evalDeferred("cmds.currentUnit(linear=\"meter\", angle=\"degree\", time=\"film\")")

    cmds.animDisplay(refAnimCurvesEditable=False)
    cmds.playbackOptions(playbackSpeed=0, by=1, maxPlaybackSpeed=1, view="active", loop="once")
    cmds.evalDeferred("cmds.keyTangent(g=True, inTangentType=\"auto\", outTangentType=\"auto\", weightedTangents=False)")
    cmds.evalDeferred("cmds.autoKeyframe(state=False)")
    
    cmds.evaluationManager(mode="parallel")
    cmds.optionVar(intValue=("gpuOverride", 1))
    cmds.optionVar(intValue=("prepopulateController", 1))

    cmds.evalDeferred("cmds.evaluator(name=\"cache\", enable=0)")
    
    # Tools
    # -----------------------------------------------------------------
    cmds.evalDeferred("mel.eval('source MayaBonusTools_load.mel; bt_displayControl;')")
