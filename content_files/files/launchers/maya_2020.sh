# - MAYA VERSION -
export VERSION=2020

# - SHARED PATHS -
export ROOT=$HOME/maya
export MODULES=$ROOT/modules
# export SHARED=<your>/<shared>/<path>

# - FILE PATHS -
export MAYA_MODULE_PATH=
export PYTHONPATH=
export MAYA_SCRIPT_PATH=
export MAYA_PLUG_IN_PATH=
export XBMLANGPATH=
export MAYA_PRESET_PATH=
export MAYA_SHELF_PATH=
export MAYA_PROJECTS_DIR=
export MAYA_PROJECT=
export MAYA_CUSTOM_TEMPLATE_PATH=
export MAYA_CUSTOM_TEMPLATE_WRITE_PATH=
export MAYA_CMD_FILE_OUTPUT=$ROOT/$VERSION/maya_output.log
export TMPDIR=$HOME/temp

# - SPECIFICS -
export MAYA_DISABLE_CLIC_IPM=1
export MAYA_DISABLE_CIP=1
export MAYA_DISABLE_CER=1
export MAYA_NO_WARNING_FOR_MISSING_DEFAULT_RENDERER=1

# - CREATE DIRECTORY -
if [ ! -d "$HOME/temp" ]; then
  mkdir -p $HOME/temp
fi

# - START MAYA -
/usr/autodesk/maya$VERSION/bin/maya -noAutoloadPlugins
