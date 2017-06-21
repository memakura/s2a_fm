# s2a_fm Installer
Control Arduino from Scratch 2 offline editor

![s2a_fm](https://github.com/memakura/s2a_fm/blob/develop/images/ScratchArduino.png)
- Use MrYsLab s2a_fm
- Python is not required to be installed

## Installation
1. Install FirmataPlus: Download library.zip from https://github.com/MrYsLab/PyMata/tree/master/ArduinoSketch, and extract it under your Arduino library folder (e.g., c:\users\<username>\Documents\Arduino)
1. Install dist/s2a_fm-1.5-amd64.msi (e.g., "C:\Program Files\s2a_fm")
1. Set COM port number
    1. Check your COM port for Arduino using Arduino IDE or Device Manager (assume the port is COM7 in what follows)
    1. Set "Target" of the property of "s2a_fm" shortcut on the desktop to `"C:\Program Files\s2a_fm\s2a_fm.exe" COM7` (default is COM5)

## How to use
1. Arduino Setting
    - Open StandardFirmataPlus and write it to Arduino
1. Scratch2 Setting
    1. Start Scratch2 offline editor
    1. Click "File" by pressing "Shift" key, and select HTTP extension
    1. Select "C:\Program Files\s2a_fm\work\s2a_fm_ja2.s2e" (other language are available under ScratchFiles/ExtensionDescriptor folder)
1. Start s2a_fm by clicking the shortcut on the desktop

## Troubleshooting
- In case the window closes suddenly
    - Check COM port again.
    - Check if other s2a_fm window is still open.
    - If the problem cannot be solved, change the "Target" of the shortcut to `cmd /k "C:\Program Files\s2a_fm\s2a_fm.exe" COM7` and check the message. If the message "Could not instantiate PyMata - is your Arduino plugged in?" is shown, check the COM port again.
 
