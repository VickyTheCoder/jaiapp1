[app]

title = Kiwi Finalizer

package.name = kiwifinalizer
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,reportlab,pyjnius==1.5.0,plyer==2.1.0

orientation = portrait

fullscreen = 0

android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.build_tools = 31.0.0

android.accept_sdk_license = True
android.skip_update = True

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.archs = arm64-v8a

p4a.branch = stable

log_level = 2
warn_on_root = 0