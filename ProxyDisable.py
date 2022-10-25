import os

os.system("reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /d 0 /t "
          "REG_DWORD /f")
