---
title: Environment
media_order: 'prefs_structure.jpg,module_structure.jpg'
---

___
### Preferences Files

By default, Maya stores preferences files in the following path:  
- Windows --> `C:\Users\<username>\Documents\maya\<version>\prefs`  
- Linux --> `/home/<username>/maya/<version>/prefs`  
- MacOS --> `/Users/<username>/Library/Preferences/Autodesk/maya/<version>/prefs`  

Initial structure for Maya user preferences:  
<img src="environment/prefs_structure.jpg" style="align:left;margin:5px 5px">  

!!! You could create the missing folder **modules** in the preferences root folder **maya**.  
!!! Creating this directory allow all installed versions of Maya to discover & load the content.  

___
### Modules
A [module](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=__developer_Maya_SDK_MERGED_Distributing_Maya_Plug_ins_DistributingUsingModules_Maya_module_paths_folders_and_html) is a simple directory with sub folders, it's defined to Maya by a description file ::: **`.mod`** or **`.txt`**  
The module folder could contain scripts, plug-ins, icons & custom files related to a complex tool.

Default module structure:  
<img src="environment/module_structure.jpg" style="align:left;margin:5px 5px">  

Get a module example: [Module Template](https://github.com/mindsbreaker/rigging-course/raw/main/content_files/files/tools/moduleTemplate.zip) 

___
### Startup File

To load tools & execute custom commands at Maya startup, simply create a file named [userSetup](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-F3D60949-2372-47F5-B8D6-78D73F78D587) with a `.mel` or `.py` extension.  
Drop this file in a *scripts* directory sourced by Maya.  

!!!! Maya will only evaluate the first **userSetup** file found in the scripts paths, but each **module** could have its own *userSetup*.  

Startup file examples:  
- Python --> [userSetup.py](https://github.com/mindsbreaker/rigging-course/raw/main/content_files/files/startups/userSetup.py) 
- Mel --> [userSetup.mel](https://github.com/mindsbreaker/rigging-course/raw/main/content_files/files/startups/userSetup.mel)

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
| `PYTHONPATH`                      | Paths to source python files & folders (module) ::: `.py` / `__init__.py`
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
- The variables set in the OS take priority over any settings in the *Maya.env* file.
- Could be used in custom app launchers with more control.

___
### App Launcher

A custom app launcher could be a simple **`.bat`** file on Windows and **`.sh`** on Linux.  

Short example on Windows:  
```
set MAYA_MODULE_PATH=<modules_custom_path>\bonusTools\22.0.1;

start /MAX C:\PROGRA~1\Autodesk\Maya2020\bin\maya.exe -noAutoloadPlugins
```
!!! Start Maya from the command line with [**arguments**](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-2E5D1D43-DC3D-4CB2-9A35-757598220F22) ::: **`-hideConsole -nosplash -batch -command`**  

Launcher file examples:
- Windows --> [bat file](https://github.com/mindsbreaker/rigging-course/raw/main/content_files/files/launchers/maya_2020.bat)
- Linux --> [sh file](https://github.com/mindsbreaker/rigging-course/raw/main/content_files/files/launchers/maya_2020.sh)

