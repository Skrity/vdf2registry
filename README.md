# vdf2registry
Extract Registry entries from .vdf file.
Use case: Steam Games that won't work without Reg entries from .vdf file.
  e.g. Muv-Luv, Muv-Luv Alternative.

Dependencies:
  * VC++ 2015 redist (may or may not be needed to run)
  * https://pypi.python.org/pypi/vdf (required to freeze)
  * PyInstaller used to build

Usage:
  1. Put vdf2registry.exe to game folder
  2. Make sure .vdf file exist within this folder
  3. Run vdf2registry.exe (This will reset your in-game settings)
  
Tested with Windows 10 Creators Update.

License: MIT (inherited from vdf).

No support will be provided whatsoever.
