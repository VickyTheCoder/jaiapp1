[app]

title = Kiwi Finalizer
package.name = kiwifinalizer
package.domain = org.example

source.dir = .
source.include_exts = py,kv,jpg,png,pdf,doc,docx

version = 1.0

requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,reportlab,pyjnius,plyer

orientation = portrait

fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

android.api = 31
android.minapi = 21
android.sdk = 31
android.build_tools = 31.0.0

android.arch = arm64-v8a
android.ndk = 25b

android.accept_sdk_license = True
android.skip_update = True
android.sdk_path = /home/runner/android-sdk

android.release_artifact = apk

android.request_legacy_storage = True

p4a.branch = master