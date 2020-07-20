REM Simple script to generate .kml and thumbnails. 
set imagedir=%CD%
@echo off
call conda activate abtools
call python -m imse.tools.cli -i %imagedir% 
