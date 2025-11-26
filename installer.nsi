!include "MUI2.nsh"

Name "Calculator"
OutFile "CalculatorSetup.exe"
InstallDir "$PROGRAMFILES\Calculator"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "Russian"

Section "Main Application"
    SetOutPath $INSTDIR
    
    File "README.md"
    File "requirements.txt"
    File "calculator.bat"
    File "calculator-icon_34473.ico"
    
    SetOutPath "$INSTDIR\src"
    File /r "src\*"
    
    SetOutPath "$INSTDIR\icon"
    File "icon\calculator-icon_34473.png"
    
    CreateDirectory "$SMPROGRAMS\Calculator"
    CreateShortCut "$SMPROGRAMS\Calculator\Calculator.lnk" "$INSTDIR\calculator.bat" "" "$INSTDIR\calculator-icon_34473.ico"
    
    CreateShortCut "$DESKTOP\Calculator.lnk" "$INSTDIR\calculator.bat" "" "$INSTDIR\calculator-icon_34473.ico"
    
    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Uninstall"
    Delete "$SMPROGRAMS\Calculator\Calculator.lnk"
    Delete "$DESKTOP\Calculator.lnk"
    RMDir "$SMPROGRAMS\Calculator"
    
    RMDir /r "$INSTDIR"
SectionEnd
