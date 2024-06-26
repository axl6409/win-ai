[Setup]
AppName=MyChatGPTApp
AppVersion=1.0
DefaultDirName={pf}\MyChatGPTApp
DefaultGroupName=MyChatGPTApp
OutputDir=.
OutputBaseFilename=MyChatGPTAppInstaller

[Files]
Source: "dist\ChatGPTAPP.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{userdesktop}\ChatGPTApp"; Filename: "{app}\ChatGPTAPP.exe"
Name: "{group}\ChatGPTApp"; Filename: "{app}\ChatGPTAPP.exe"

