[app]

title = Kiwi Finalizer
package.name = kiwifinalizer
package.domain = org.example

source.dir = .
source.include_exts = py,kv,jpg,png

version = 1.0

# 🔥 Stable requirements (no python-docx to avoid build failure)
requirements = python3==3.10.11,kivy,kivymd,pillow,reportlab,pyjnius,plyer

orientation = portrait

# Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

# Android config
android.api = 31
android.minapi = 21
android.build_tools = 31.0.0

# 🔥 VERY IMPORTANT FIXES
android.arch = arm64-v8a
android.sdk_path = /home/runner/android-sdk
android.accept_sdk_license = True
android.skip_update = True

# 🔥 Stabilize python-for-android
p4a.branch = stable

fullscreen = 0

# Android 10+ file access
android.request_legacy_storage = True