[app]

title = KiwiFinalizer
package.name = kiwifinalizer
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1,kivymd==1.1.1,pillow,reportlab,pyjnius==1.5.0,plyer==2.1.0

orientation = portrait
fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

android.accept_sdk_license = True

android.release_artifact = apk

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# IMPORTANT
p4a.url = https://github.com/kivy/python-for-android.git
p4a.branch = master
p4a.commit = 2024.01.21

android.skip_update = False

log_level = 2

warn_on_root = 1