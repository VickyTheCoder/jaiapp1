[app]

title = Kiwi Finalizer

package.name = kiwifinalizer
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1,kivymd==1.1.1,pillow,reportlab,pyjnius==1.5.0,plyer==2.1.0

orientation = portrait
fullscreen = 0

# Android settings
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.build_tools = 31.0.0

# IMPORTANT FIX
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

android.accept_sdk_license = True
android.skip_update = True

# Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Architectures
android.archs = arm64-v8a

# Python-for-Android
p4a.branch = stable

# Buildozer
log_level = 2
warn_on_root = 0