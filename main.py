import os
import traceback
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

# Android imports
if platform == "android":
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
w=1
KV = '''
MDScreen:
    md_bg_color: 1,1,1,1

    MDBoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        padding: "20dp"

        MDLabel:
            text: "Kiwi Finalizer"
            halign: "center"
            font_style: "H5"

        MDRaisedButton:
            text: "Pick Document"
            on_release: app.pick_document()

        MDRaisedButton:
            text: "Pick Image"
            on_release: app.pick_image()

        MDRaisedButton:
            text: "Final Copy"
            id: final_btn
            disabled: True
            on_release: app.final_copy()

        MDRaisedButton:
            text: "Share"
            id: share_btn
            disabled: True
            on_release: app.share_file()
'''

class MainApp(MDApp):

    def build(self):
        if platform == "android":
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE
            ])
        return Builder.load_string(KV)

    def show_error(self, e):
        print("ERROR:", e)
        traceback.print_exc()
        Snackbar(text=str(e)).open()

    # -----------------------------
    # Android File Picker
    # -----------------------------
    def open_android_picker(self, mime_type):
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')

            intent = Intent(Intent.ACTION_GET_CONTENT)
            intent.setType(mime_type)
            intent.addCategory(Intent.CATEGORY_OPENABLE)

            currentActivity = PythonActivity.mActivity
            currentActivity.startActivityForResult(intent, 1)

            Snackbar(text="File picker opened").open()

        except Exception as e:
            self.show_error(e)

    def pick_document(self):
        if platform == "android":
            self.open_android_picker("*/*")
        else:
            Snackbar(text="Desktop not supported in this build").open()

    def pick_image(self):
        if platform == "android":
            self.open_android_picker("image/*")
        else:
            Snackbar(text="Desktop not supported").open()

    # -----------------------------
    # Dummy logic (safe for now)
    # -----------------------------
    def final_copy(self):
        try:
            Snackbar(text="Final copy created (demo)").open()
            self.root.ids.share_btn.disabled = False
        except Exception as e:
            self.show_error(e)

    def share_file(self):
        try:
            Snackbar(text="Share triggered (demo)").open()
        except Exception as e:
            self.show_error(e)


MainApp().run()