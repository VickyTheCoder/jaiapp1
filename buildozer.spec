[app]

title = KiwiFinalizer
package.name = kiwifinalizer
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf

version = 1.0

requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,reportlab,pyjnius==1.5.0,plyer==2.1.0

orientation = portrait
fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

android.accept_sdk_license = True

# IMPORTANT
android.skip_update = False

# DO NOT BUILD AAB
android.release_artifact = apk

# SDK
android.sdk = 31

# permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# p4a
p4a.branch = develop

log_level = 2

warn_on_root = 1