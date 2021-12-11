---
title: Environment
media_order: 'prefs_structure.jpg,module_structure.jpg'
---

___
### Preferences Files

Default structure for Maya user preferences:  
![Preferences files & folders](environment/prefs_structure.jpg "prefs_structure")

By default some useful directories are missing: `plug-ins` & `modules`  
Creating these directories in the root folder *'maya'* allow the different versions of Maya to load their content.  
In the same way, these directories inside the version folder *'2020'* can only be discovered by this version.

___
### Startup File

To load tools & execute commands at Maya startup, simply create a [userSetup](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-F3D60949-2372-47F5-B8D6-78D73F78D587) **Mel** (`.mel`) or **Python** (`.py`) file.  
Drop this file in a **scripts** directory sourced by Maya.

!!!! Maya will only evaluate the first *userSetup* found in the scripts paths, but each **module** could have its own *userSetup* file

Get examples files:  
- Python -> [userSetup.py](https://u.pcloud.link/publink/show?code=XZF44HXZcS6uu3ngbLFS0E8cMfUG4QjlfwIV) 
- Mel -> [userSetup.mel](https://u.pcloud.link/publink/show?code=XZJ44HXZDWLBtWdg4ImQ9i2lUGwDMRnRG6YV)

___
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

!!! Some variables supports multiple paths ::: separated with **`;`** on Windows and **`:`** on Linux. 

___
### Set Variables

There are two methods to set variables before Maya's startup:

1. Using the file ::: [Maya.env](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-8EFB1AC1-ED7D-4099-9EEE-624097872C04)
2. Using OS commands ::: [set | setenv | export](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-1D8B1A57-6FA3-4494-8FEC-87DA2A38FD35)

The second method is better for at least two reasons:
- The variables set in the OS take priority over any settings in the Maya.env file.
- Could be used in custom app launchers with more control.

___
### App Launchers

A custom app launcher could be a simple **`.bat`** file on Windows and **`.sh`** on Linux.  

Short example on Windows:  
```
set SHARED_PATH=%USERPROFILE%\Documents\maya\my_custom_modules
set MAYA_MODULE_PATH=%SHARED_PATH%\bonusTools\22.0.1;

start /MAX C:\PROGRA~1\Autodesk\Maya2020\bin\maya.exe -noAutoloadPlugins
```
!!! Start Maya from the command line with [arguments](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-2E5D1D43-DC3D-4CB2-9A35-757598220F22) ::: **`-hideConsole -nosplash -batch -command`**  

Launcher file examples:
- Windows [bat file](https://u.pcloud.link/publink/show?code=XZURRHXZMaoUOt5ejr8zmsTMq69QEFL2uBzk)
- Linux [sh file](https://u.pcloud.link/publink/show?code=XZE84HXZg91fYe7GWyVJsAtbsbbUAjTH9yeV)

