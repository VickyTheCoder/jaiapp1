[app]

title = KiwiFinalizer
package.name = kiwifinalizer
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1,kivymd==1.1.1,pillow,plyer==2.1.0

orientation = portrait

fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

p4a.branch = master

android.accept_sdk_license = True

log_level = 2

warn_on_root = 1

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.enable_androidx = True

android.gradle_dependencies =

android.allow_backup = True

android.release_artifact = aab
