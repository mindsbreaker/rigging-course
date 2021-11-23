---
title: Environment
---

## *Set Maya's Env*

### Variables

To customize Maya's behavior the best way is [Environment Variables](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-925EB3B5-1839-45ED-AA2E-3184E3A45AC7).  
The most commons and usefuls to define your environment are [File Path](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-228CCA33-4AFE-4380-8C3D-18D23F7EAC72) variables.

List of most used, notably to share resources over the network:

| Variable                          | Description               
| -----------------------           | --------------------------
| `MAYA_APP_DIR`                    | Main path for all user prefs ::: `c:\Users\<username>\Documents\Maya`
| `MAYA_ENV_DIR`                    | Path to source Maya's env file ::: `Maya.env`
| `MAYA_PLUG_IN_PATH`               | Paths to source plug-ins ::: `.py` / `.mll` / `.so`
| `MAYA_MODULE_PATH`                | Paths to source modules definitions ::: `.mod` / `.txt` / ...
| `MAYA_SCRIPT_PATH`                | Paths to source mel & python scripts ::: `.mel` / `.py`
| `PYTHONPATH`                      | Paths to source python scripts & modules dir ::: `.py` / `__init__.py`
| `XBMLANGPATH`                     | Paths to source icons ::: `.png` / `.svg` / ...
| `MAYA_SHELF_PATH`                 | Paths to source shelves definitions ::: `.mel`
| `MAYA_PRESET_PATH`                | Paths to source presets definitions ::: `.mel`
| `MAYA_CUSTOM_TEMPLATE_PATH`       | Paths to source Attribute & Node Editors templates ::: `.mel` / `.xml`
| `MAYA_CUSTOM_TEMPLATE_WRITE_PATH` | Paths to write [Node Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-C1E02C84-8CCF-4B3D-B080-F4A379AD1FCB) templates ::: `.xml`
| `MAYA_PROJECTS_DIR`               | Path to projects folder ::: `%USERPROFILE%\Documents\Maya\projects`
| `MAYA_PROJECT`                    | Path to startup project ::: `%MAYA_PROJECTS_DIR%\default`
| `MAYA_CMD_FILE_OUTPUT`            | Path to write Maya output to an external file ::: `maya_output.log`
| `TEMP or TMPDIR`                  | Path to write various temporary files ::: `Crash Files`

>:information_source: **Note:** Some variables supports multiple paths ::: separated with **`;`** on Windows and **`:`** on Linux. 

<br>

Examples of variables more specifics:

| Variable                  | Description               
| -----------------------   | --------------------------
| `MAYA_DISABLE_CLIC_IPM`   | Cloud login utilities
| `MAYA_DISABLE_CIP`        | Avoid fatal crash on start-up ::: `WTF`
| `MAYA_DISABLE_CER`        | Customer Error Reporting

> :information_source: **Note:** These variables take a boolean value **`0 | 1`** ::: default value = **`0`**.  

<br>

### Set Variables

There are two methods to set variables before Maya's startup:

1. Using the file ::: [Maya.env](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-8EFB1AC1-ED7D-4099-9EEE-624097872C04)
2. Using OS commands ::: [set | setenv | export](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-1D8B1A57-6FA3-4494-8FEC-87DA2A38FD35)

The second method is better for at least two reasons:
- The variables set in the OS take priority over any settings in the Maya.env file.
- Could be used in custom app launchers with more control.

<br>

### App Launchers

A custom app launcher could be a simple **`.bat`** file on Windows and **`.sh`** on Linux.  

Short example on Windows:  
```batch
set SHARED_PATH=%USERPROFILE%\Documents\maya\modules
set MAYA_MODULE_PATH=%SHARED_PATH%\bonusTools\20.0.1;
set TMPDIR=%USERPROFILE%\temp

if not exist "%USERPROFILE%\temp" mkdir %USERPROFILE%\temp

start /MAX C:\PROGRA~1\Autodesk\Maya2020\bin\maya.exe -noAutoloadPlugins
```
>:information_source: **Note:** The missing *'temp'* folder is created with system commands ::: [windows](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands) | [linux](https://ss64.com/bash/)  
>:bulb: **Tip:** Start Maya from the command line with [arguments](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-2E5D1D43-DC3D-4CB2-9A35-757598220F22) ::: **`-hideConsole -nosplash -batch -command`**

<br>

:rocket: Get template files:  

| Windows               | Linux               
| --------------------  | --------------------
| [:cloud: bat file](https://u.pcloud.link/publink/show?code=XZURRHXZMaoUOt5ejr8zmsTMq69QEFL2uBzk)  | [:cloud: sh file](https://u.pcloud.link/publink/show?code=XZE84HXZg91fYe7GWyVJsAtbsbbUAjTH9yeV)

<br>

### Deploy Tools

Minimal / default structure for Maya user preferences:  
![Preferences default structure](resources/images/prefs_structure.jpg)

Get a clean Maya prefs structure ::: [:cloud: maya_clean.zip](https://u.pcloud.link/publink/show?code=XZz44HXZ9IsT5TAPFnVV7XNvOUKngk81APo7)

By default some useful directories are missing: `plug-ins` & `modules`  
Creating these directories in the root folder *'maya'* allow the different versions of Maya to load their content.  
In the same way, these directories inside the version folder *'2020'* can only be discovered by this version.

> :warning: **Attention:** The plugins files **`.mll`** & **`.so`** are compiled for specific Maya version.  
> Drop them in the *'plug-ins'* folder inside the version directory.

<br>

Modules are so **:cool:** ...  
A [module](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=__developer_Maya_SDK_MERGED_Distributing_Maya_Plug_ins_DistributingUsingModules_Maya_module_paths_folders_and_html) is a simple directory with sub folders, it's defined to Maya by a description file ::: **`.mod`** | **`.txt`**

Default module structure:  
![Module default structure](resources/images/module_structure.jpg)

<br>


Some lines from a description file content:
```shell
+ MAYAVERSION:2020 PLATFORM:win64 bonusTools 20.0.1 ./bonusTools/20.0.1
scripts: scripts-2020/
PYTHONPATH +:= python-2020/
plug-ins: plug-ins/win64-2020

+ MAYAVERSION:2020 PLATFORM:linux bonusTools 20.0.1 ./bonusTools/20.0.1
scripts: scripts-2020/
PYTHONPATH +:= python-2020/
plug-ins: plug-ins/linux-2020
```
> :information_source: **Note:** Scripts & plug-ins default paths are overrided for specific context :::`MAYAVERSION` & `PLATFORM`.  
> A path is added to the environment variable `PYTHONPATH` with these operators ::: **`+:=`**

<br>

Get modules archives:  

| Module                | Description         
| --------------------  | --------------------
| [:cloud: Bonus Tools](https://u.pcloud.link/publink/show?code=XZQ44HXZGRp3myMYEhkh1H7mbXnlG4wow2uX)  | Official collection of useful Maya scripts and plug-ins ::: [Autodesk Apps](https://apps.autodesk.com/MAYA/fr/Detail/Index?id=8115150172702393827&os=Win64&appLang=en) & [Overview](https://www.youtube.com/watch?v=JX6CBJXErQE&list=PLRhyUhUvvnOTWQP527tK_msQwDgstzIc_)
| [:cloud: Security Tools](https://u.pcloud.link/publink/show?code=XZm44HXZQj7dJGEUb1z4R8pU1q6EyXF2TLJX)  | Official tools to removes malicious scripts from `.ma` & `.mb` files ::: [Autodesk Apps](https://apps.autodesk.com/MAYA/fr/Detail/Index?id=8637238041954239715&os=Win64&appLang=en)
| [:cloud: Module Template](https://u.pcloud.link/publink/show?code=XZb44HXZEaCwRg7AsX0fvSVEGHp0i4r7qfuX)  | A minimal module example with some custom scripts.

<br>

### Startup Settings

To load tools & execute commands at Maya startup, simply create a [userSetup](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-F3D60949-2372-47F5-B8D6-78D73F78D587) file ::: `.mel` / `.py`  
Drop this file in a *'scripts'* directory sourced by Maya.

>:bulb: **Tip:** Maya will only evaluate the first userSetup found in the scripts paths, but ...  
Each module could have its own userSetup file ... YES so **:cool:** !

<br>


Short example from `userSetup.py`:  
```python
from maya import cmds, mel

if not cmds.about(batch=True):
    cmds.loadPlugin("matrixNodes", quiet=True)

    cmds.selectPref(trackSelectionOrder=1)
    
    cmds.evalDeferred("cmds.evaluator(name=\"cache\", enable=0)")

    mel.eval('source MayaBonusTools_load.mel; bt_displayControl;')
```
> :information_source: **Note:**  With the **`if not`** statement, commands will be executed only if Maya isn't in batch mode.  

<br>

Get template files:  

| Python                | Mel                 
| --------------------  | --------------------
| [:cloud: userSetup.py](https://u.pcloud.link/publink/show?code=XZF44HXZcS6uu3ngbLFS0E8cMfUG4QjlfwIV)  | [:cloud: userSetup.mel](https://u.pcloud.link/publink/show?code=XZJ44HXZDWLBtWdg4ImQ9i2lUGwDMRnRG6YV)
