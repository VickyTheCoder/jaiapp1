[app]

title = KiwiFinalizer
package.name = kiwifinalizer
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

version = 1.0

requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,reportlab,pyjnius==1.5.0,plyer==2.1.0

orientation = portrait
fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

android.accept_sdk_license = True

p4a.branch = develop

# VERY IMPORTANT
# remove python3 version pin completely
# do NOT use python3==3.10.11

# disable AAB
android.release_artifact = apk

# use sdkmanager correctly
android.skip_update = False

# build tools
android.sdk = 31
android.sdk_path = /home/runner/android-sdk

# permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

log_level = 2

warn_on_root = 1