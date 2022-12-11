echo off
chcp 65001
color 0f
title [+] - Dev by 3n3scan#6908 - [+]
mode con lines=16 cols=53
cls

set /p user=[40;35mUsername[40;37m: 
cls
set /p pass=[40;35mPassword[40;37m: 
if %user% == root if %pass% == root goto good
goto again

:again
color 0f
mode con lines=16 cols=53
cls
echo [40;31mYour Username or Password is incorrect!
set /p user=[40;35mUsername[40;37m: 
color 0f
cls
set /p pass=[40;35mPassword[40;37m: 
if %user% == root if %pass% == root goto good
echo [40;31mYour Username or Password is incorrect!
goto again

:good
color 0f
mode con lines=16 cols=77
cls
echo [40;35mPlease wait... Your credentials are being checked. [40;37m[[40;35mI[40;37m]
echo [42;37m [40;30m 
ping localhost -n 2 >nul
cls
echo [40;35mPlease wait... Your credentials are being checked. [40;37m[[40;35m/[40;37m]
echo [42;37m [40;30m 
ping localhost -n 2 >nul
cls
echo [40;35mPlease wait... Your credentials are being checked. [40;37m[[40;35m-[40;37m]
echo [42;37m [40;30m 
ping localhost -n 2 >nul
cls
echo [40;35mPlease wait... Your credentials are being checked. [40;37m[[40;35m/[40;37m]
echo [42;37m [40;30m 
ping localhost -n 2 >nul
cls
echo [40;35mPlease wait... Your credentials are being checked. [40;37m[[40;35m-[40;37m]
echo [42;37m [40;30m 
ping localhost -n 2 >nul
cls
goto reset

:reset
color 0f
cls
goto Tool

:Tool
color 0f
mode con lines=16 cols=53
cls
echo ----------------------------------------
echo [1]  Start the Discord Bot 
echo [2]  Informations to the Bot
echo [3]  Exit
echo ----------------------------------------
set /p ans="root@root ~ # "

if %ans%==1 (
goto start
)
if %ans%==2 (
goto credits
)
if %ans%==3 (
goto exit
)

:credits
color 0f
:: mode con lines=25 cols=144
mode con lines=16 cols=53
cls
echo -----------------------------------
echo    Developed by 3n3scan
echo              and
echo  Made by @3n3scan#6908 on Discord
echo -----------------------------------
pause
cls
goto Tool

:exit
color 0f
exit

:start
color 0f
mode con lines=20 cols=82
cls
py main.py