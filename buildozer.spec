[app]

title = Kiwi Finalizer
package.name = kiwifinalizer
package.domain = org.example

source.dir = .
source.include_exts = py,kv,jpg,png

version = 1.0

requirements = python3,kivy,kivymd,pillow,reportlab,python-docx,pyjnius,plyer

orientation = portrait

# Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

# Android config
android.api = 31
android.minapi = 21
android.sdk = 31
android.build_tools = 31.0.0

android.accept_sdk_license = True
android.skip_update = True
android.sdk_path = /home/runner/android-sdk

fullscreen = 0

# Recommended for file access (Android 10+)
android.request_legacy_storage = True