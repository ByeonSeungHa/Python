# Microsoft Windows [Version 10.0.19043.1526]
# (c) Microsoft Corporation. All rights reserved.
#
# C:\Users\User>python
# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> pip install virtualenv
#   File "<stdin>", line 1
#     pip install virtualenv
#         ^^^^^^^
# SyntaxError: invalid syntax
# >>> ^Z
#
#
# C:\Users\User>pip install virtualenv
# Collecting virtualenv
#   Downloading virtualenv-20.13.1-py2.py3-none-any.whl (8.6 MB)
#      ---------------------------------------- 8.6/8.6 MB 3.2 MB/s eta 0:00:00
# Collecting six<2,>=1.9.0
#   Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
# Collecting filelock<4,>=3.2
#   Downloading filelock-3.4.2-py3-none-any.whl (9.9 kB)
# Collecting platformdirs<3,>=2
#   Downloading platformdirs-2.5.0-py3-none-any.whl (14 kB)
# Collecting distlib<1,>=0.3.1
#   Downloading distlib-0.3.4-py2.py3-none-any.whl (461 kB)
#      ---------------------------------------- 461.2/461.2 KB 3.6 MB/s eta 0:00:00
# Installing collected packages: distlib, six, platformdirs, filelock, virtualenv
# Successfully installed distlib-0.3.4 filelock-3.4.2 platformdirs-2.5.0 six-1.16.0 virtualenv-20.13.1
#
# C:\Users\User>virtualenv myenv
# created virtual environment CPython3.10.2.final.0-64 in 1579ms
#   creator CPython3Windows(dest=C:\Users\User\myenv, clear=False, no_vcs_ignore=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\User\AppData\Local\pypa\virtualenv)
#     added seed packages: pip==22.0.3, setuptools==60.6.0, wheel==0.37.1
#   activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
#
# C:\Users\User>dir
#  C 드라이브의 볼륨에는 이름이 없습니다.
#  볼륨 일련 번호: 0806-0624
#
#  C:\Users\User 디렉터리
#
# 2022-02-15  오전 11:58    <DIR>          .
# 2022-02-15  오전 11:58    <DIR>          ..
# 2020-06-30  오후 09:20    <DIR>          .android
# 2022-02-15  오전 10:01             2,885 .bash_history
# 2020-06-30  오후 09:19    <DIR>          .BigNox
# 2021-04-17  오후 05:17    <DIR>          .config
# 2022-01-23  오후 04:38                60 .gitconfig
# 2020-07-19  오후 09:48    <DIR>          .prefs
# 2022-02-13  오후 10:34    <DIR>          .vscode
# 2020-12-12  오후 08:17    <DIR>          3D Objects
# 2020-01-29  오전 12:27         2,681,786 AMD_Chipset_IODrivers.log
# 2020-07-29  오후 10:41    <DIR>          ansel
# 2020-12-12  오후 08:13    <DIR>          AppData
# 2020-01-29  오전 12:27            57,400 ChipsetExtraction.log
# 2020-12-12  오후 08:17    <DIR>          Contacts
# 2022-02-15  오전 08:22    <DIR>          Creative Cloud Files
# 2020-06-30  오후 09:34               299 d4ac4633ebd6440fa397b84f1bc94a3c.7z
# 2022-02-13  오후 10:34    <DIR>          Desktop
# 2020-01-29  오전 12:26            81,149 Device_ID.log
# 2022-01-30  오후 09:58    <DIR>          Documents
# 2022-02-15  오전 11:50    <DIR>          Downloads
# 2022-01-02  오후 10:36    <DIR>          Favorites
# 2022-02-13  오후 11:00         2,609,803 get-pip.py
# 2020-06-30  오후 09:19                66 inittk.ini
# 2020-06-30  오후 09:19                41 inst.ini
# 2020-12-12  오후 08:17    <DIR>          Links
# 2021-12-12  오후 07:48    <DIR>          Music
# 2022-02-15  오전 11:58    <DIR>          myenv
# 2020-06-30  오후 09:19                45 nuuid.ini
# 2021-08-09  오후 10:20    <DIR>          OneDrive
# 2020-12-12  오후 08:17    <DIR>          Pictures
# 2022-01-23  오후 04:21    <DIR>          PycharmProjects
# 2020-12-12  오후 08:17    <DIR>          Saved Games
# 2020-12-12  오후 08:17    <DIR>          Searches
# 2020-08-14  오전 12:56           313,879 Untitled_1.12.1.drx
# 2020-08-14  오전 12:56           448,329 Untitled_1.12.1.jpg
# 2020-06-30  오후 09:19                53 useruid.ini
# 2022-01-09  오후 08:11    <DIR>          Videos
# 2020-06-30  오후 09:19    <DIR>          vmlogs
#               13개 파일           6,195,795 바이트
#               26개 디렉터리   2,103,681,024 바이트 남음
#
# C:\Users\User>cd myenv
#
# C:\Users\User\myenv>dir
#  C 드라이브의 볼륨에는 이름이 없습니다.
#  볼륨 일련 번호: 0806-0624
#
#  C:\Users\User\myenv 디렉터리
#
# 2022-02-15  오전 11:58    <DIR>          .
# 2022-02-15  오전 11:58    <DIR>          ..
# 2022-02-15  오전 11:58                42 .gitignore
# 2022-02-15  오전 11:58    <DIR>          Lib
# 2022-02-15  오전 11:58               406 pyvenv.cfg
# 2022-02-15  오전 11:58    <DIR>          Scripts
#                2개 파일                 448 바이트
#                4개 디렉터리   2,102,566,912 바이트 남음
#
# C:\Users\User\myenv>cd scripts
#
# C:\Users\User\myenv\Scripts>dir
#  C 드라이브의 볼륨에는 이름이 없습니다.
#  볼륨 일련 번호: 0806-0624
#
#  C:\Users\User\myenv\Scripts 디렉터리
#
# 2022-02-15  오전 11:58    <DIR>          .
# 2022-02-15  오전 11:58    <DIR>          ..
# 2022-02-15  오전 11:58             2,142 activate
# 2022-02-15  오전 11:58               982 activate.bat
# 2022-02-15  오전 11:58             3,019 activate.fish
# 2022-02-15  오전 11:58             1,283 activate.nu
# 2022-02-15  오전 11:58             1,758 activate.ps1
# 2022-02-15  오전 11:58             1,193 activate_this.py
# 2022-02-15  오전 11:58               510 deactivate.bat
# 2022-02-15  오전 11:58               333 deactivate.nu
# 2022-02-15  오전 11:58           106,861 pip-3.10.exe
# 2022-02-15  오전 11:58           106,861 pip.exe
# 2022-02-15  오전 11:58           106,861 pip3.10.exe
# 2022-02-15  오전 11:58           106,861 pip3.exe
# 2022-02-15  오전 11:58                24 pydoc.bat
# 2022-02-15  오전 11:58           263,056 python.exe
# 2022-02-15  오전 11:58           251,792 pythonw.exe
# 2022-02-15  오전 11:58           106,848 wheel-3.10.exe
# 2022-02-15  오전 11:58           106,848 wheel.exe
# 2022-02-15  오전 11:58           106,848 wheel3.10.exe
# 2022-02-15  오전 11:58           106,848 wheel3.exe
#               19개 파일           1,380,928 바이트
#                2개 디렉터리   2,099,302,400 바이트 남음
#
# C:\Users\User\myenv\Scripts>activate.bat
#
# (myenv) C:\Users\User\myenv\Scripts>pip install Django
# Collecting Django
#   Downloading Django-4.0.2-py3-none-any.whl (8.0 MB)
#      ---------------------------------------- 8.0/8.0 MB 3.2 MB/s eta 0:00:00
# Collecting tzdata
#   Downloading tzdata-2021.5-py2.py3-none-any.whl (339 kB)
#      ---------------------------------------- 339.4/339.4 KB 3.0 MB/s eta 0:00:00
# Collecting asgiref<4,>=3.4.1
#   Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
# Collecting sqlparse>=0.2.2
#   Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
#      ---------------------------------------- 42.3/42.3 KB ? eta 0:00:00
# Installing collected packages: tzdata, sqlparse, asgiref, Django
# Successfully installed Django-4.0.2 asgiref-3.5.0 sqlparse-0.4.2 tzdata-2021.5
#
# (myenv) C:\Users\User\myenv\Scripts>python
# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import Django
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'Django'
# >>> django
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'django' is not defined
# >>> Django
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Django' is not defined
# >>> import django