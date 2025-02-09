@echo off
 rem MAYA

 rem --- Path ---
set "PROJECT_ROOT=//bigfoot/breakingpoint"
set "PIPELINE_PATH=%PROJECT_ROOT%/_pipeline"
set "LIBRARY_PATH=%PIPELINE_PATH%/lib"
set "SOFTWARE_PATH=%PIPELINE_PATH%/_sandbox/maya"

set "SCRIPT_PATH=%SOFTWARE_PATH%/scripts"
set "PLUGINS_PATH=%SOFTWARE_PATH%/plugins"
set "ARNOLD_PATH=%PLUGINS_PATH%/arnold"
set "ARNOLD_SHADER_PATH=%ARNOLD_PATH%/alShader"

set "MAYA_VERSION=2015"


 rem --- Python ---
set "PYTHONPATH=%SOFTWARE_PATH%;%PYTHONPATH%"
set "PYTHONPATH=%PIPELINE_PATH%;%PYTHONPATH%"
set "PYTHONPATH=%LIBRARY_PATH%;%PYTHONPATH%"


 rem --- Plugin ---
set "MAYA_PLUG_IN_PATH=%PLUGINS_PATH%/SOuP/plug-ins/win_maya2015;%MAYA_PLUG_IN_PATH%"


 rem --- Shelf ---
set "MAYA_SHELF_PATH=%PLUGINS_PATH%/SOuP/shelves;%MAYA_SHELF_PATH%"
set "MAYA_SHELF_PATH=%SOFTWARE_PATH%/shelf;%MAYA_SHELF_PATH%"


 rem --- Icon ---
set "XBMLANGPATH=%PLUGINS_PATH%/SOuP/icons;%B%XBMLANGPATH%"


 rem --- Arnold ---
set "MtoA=%ARNOLD_PATH%/%MAYA_VERSION%"
set "MAYA_MODULE_PATH=%MtoA%;%MAYA_MODULE_PATH%"
set "PATH=%MtoA%/bin;%PATH%"
set "ARNOLD_PLUGIN_PATH=%MtoA%/shaders;%ARNOLD_PLUGIN_PATH%;%ARNOLD_PLUGIN_PATH%"
set "ARNOLD_PLUGIN_PATH=%ARNOLD_PATH%/bin;%ARNOLD_PLUGIN_PATH%;%ARNOLD_PLUGIN_PATH%"
set "ARNOLD_PLUGIN_PATH=%ARNOLD_SHADER_PATH%/bin;%ARNOLD_PLUGIN_PATH%"
set "MTOA_TEMPLATES_PATH=%ARNOLD_SHADER_PATH%/ae;%MTOA_TEMPLATES_PATH%"

set "ARNOLD_LICENSE_HOST=blue"


 rem --- Disable Report ---
set "MAYA_DISABLE_CIP=1"
set "MAYA_DISABLE_CER=1"


 rem --- MayaEnvVars ---
 rem set "MAYA_PROJECT=%PROJECT_ROOT%/2_production"
 rem cd %MAYA_PROJECT%


 rem --- SplashScreen ---
 rem File: MayaEDUStartupImage.png
set "XBMLANGPATH=%PIPELINE_PATH%/img/logo;%XBMLANGPATH%"


 rem --- Call Maya ---
set "MAYA_DIR=C:/Program Files/Autodesk/Maya%MAYA_VERSION%"
set "PATH=%MAYA_DIR%/bin;%PATH%"
start maya

exit