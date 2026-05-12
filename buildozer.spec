[app]

title = Kiwi Finalizer
package.name = kiwifinalizer
package.domain = org.example

source.dir = .
source.include_exts = py,kv,jpg,png

version = 1.0

requirements = python3==3.10.11,kivy,kivymd,pillow,reportlab,pyjnius,plyer

orientation = portrait

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

android.api = 31
android.minapi = 21
android.build_tools = 31.0.0

android.arch = arm64-v8a
android.ndk = 25b

android.sdk_path = /home/runner/android-sdk
android.accept_sdk_license = True
android.skip_update = True

android.release_artifact = apk

fullscreen = 0
android.request_legacy_storage = True