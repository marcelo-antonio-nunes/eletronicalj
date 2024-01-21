@echo off
setlocal enabledelayedexpansion

rem Define o caminho da pasta e a imagem para o ícone
set "pasta=C:\eletronicalj\static\foto"
set "icone=C:\eletronicalj\caixa.ico"

rem Cria o atalho na área de trabalho
set "atalho=%userprofile%\Desktop\FotoPlacas.lnk"
echo Set WshShell = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo Set link = WshShell.CreateShortcut("%atalho%") >> CreateShortcut.vbs
echo link.TargetPath = "%pasta%" >> CreateShortcut.vbs
echo link.IconLocation = "%icone%" >> CreateShortcut.vbs
echo link.Save >> CreateShortcut.vbs
cscript /nologo CreateShortcut.vbs
del CreateShortcut.vbs

rem Cria o atalho na área de trabalho para a pasta de fotos
set "atalhoFoto=%userprofile%\Desktop\FotoPlacas.lnk"
echo Set WshShell = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo Set link = WshShell.CreateShortcut("%atalhoFoto%") >> CreateShortcut.vbs
echo link.TargetPath = "%pastaFoto%" >> CreateShortcut.vbs
echo link.IconLocation = "%iconeFoto%" >> CreateShortcut.vbs
echo link.Save >> CreateShortcut.vbs
cscript /nologo CreateShortcut.vbs
del CreateShortcut.vbs

rem Define o caminho do executável e a imagem para o ícone do segundo atalho
set "executavelStart=C:\eletronicalj\start.exe"
set "iconeStart=C:\eletronicalj\EletronicaLj.ico"

rem Cria o atalho na área de trabalho para o executável start.exe
set "atalhoStart=%userprofile%\Desktop\StartEletronica.lnk"
echo Set WshShell = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo Set link = WshShell.CreateShortcut("%atalhoStart%") >> CreateShortcut.vbs
echo link.TargetPath = "%executavelStart%" >> CreateShortcut.vbs
echo link.IconLocation = "%iconeStart%" >> CreateShortcut.vbs
echo link.WorkingDirectory = "C:\eletronicalj" >> CreateShortcut.vbs
echo link.Save >> CreateShortcut.vbs
cscript /nologo CreateShortcut.vbs
del CreateShortcut.vbs

rem Define o caminho do executável e a imagem para o ícone do segundo atalho
set "executavelStart=C:\eletronicalj\start.exe"
set "iconeStart=C:\eletronicalj\EletronicaLj.ico"

rem Cria o atalho na área de trabalho para o executável start.exe
set "atalhoStart=%userprofile%\Desktop\StartEletronica.lnk"
echo Set WshShell = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo Set link = WshShell.CreateShortcut("%atalhoStart%") >> CreateShortcut.vbs
echo link.TargetPath = "%executavelStart%" >> CreateShortcut.vbs
echo link.IconLocation = "%iconeStart%" >> CreateShortcut.vbs
echo link.WorkingDirectory = "C:\eletronicalj" >> CreateShortcut.vbs
echo link.Save >> CreateShortcut.vbs
cscript /nologo CreateShortcut.vbs
del CreateShortcut.vbs

rem Define o caminho do executável e a imagem para o ícone do terceiro atalho
set "executavelBackup=C:\eletronicalj\backup.exe"
set "iconeBackup=C:\eletronicalj\backup.ico"

rem Cria o atalho na área de trabalho para o executável backup.exe
set "atalhoBackup=%userprofile%\Desktop\BackupEletronica.lnk"
echo Set WshShell = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo Set link = WshShell.CreateShortcut("%atalhoBackup%") >> CreateShortcut.vbs
echo link.TargetPath = "%executavelBackup%" >> CreateShortcut.vbs
echo link.IconLocation = "%iconeBackup%" >> CreateShortcut.vbs
echo link.WorkingDirectory = "C:\eletronicalj" >> CreateShortcut.vbs
echo link.Save >> CreateShortcut.vbs
cscript /nologo CreateShortcut.vbs
del CreateShortcut.vbs

echo Atalhos criados com sucesso!
pause