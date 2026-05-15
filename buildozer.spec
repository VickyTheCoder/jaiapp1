[app]

title = KiwiFinalizer
package.name = kiwifinalizer
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

version = 1.0

requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,reportlab,plyer==2.1.0

orientation = portrait

fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

android.accept_sdk_license = True
android.allow_backup = True

p4a.branch = master

log_level = 2

warn_on_root = 1

[buildozer]

log_level = 2

build_dir = .buildozer
bin_dir = ./bin