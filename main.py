import os
import platform

from kivymd.app import MDApp
from kivy.lang import Builder

from plyer import filechooser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PIL import Image
from docx import Document

KV = open("layout.kv").read()


class KiwiApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        self.doc_path = None
        self.img_path = None
        self.output_pdf = os.path.abspath("final_output.pdf")

        return Builder.load_string(KV)

    # -------- FILE PICKERS --------

    def pick_document(self):
        filechooser.open_file(
            filters=["*.pdf", "*.docx"],
            on_selection=self.select_doc
        )

    def select_doc(self, selection):
        if selection:
            self.doc_path = selection[0]
            self.root.ids.doc_label.text = os.path.basename(self.doc_path)
            self.check_ready()

    def pick_image(self):
        filechooser.open_file(
            filters=["*.png", "*.jpg", "*.jpeg"],
            on_selection=self.select_img
        )

    def select_img(self, selection):
        if selection:
            self.img_path = selection[0]
            self.root.ids.img_label.text = os.path.basename(self.img_path)
            self.check_ready()

    # -------- LOGIC --------

    def check_ready(self):
        if self.doc_path and self.img_path:
            self.root.ids.final_btn.disabled = False

    def create_final_pdf(self):
        c = canvas.Canvas(self.output_pdf, pagesize=A4)

        # ---- DOCX handling ----
        if self.doc_path.endswith(".docx"):
            doc = Document(self.doc_path)
            y = 800
            for p in doc.paragraphs:
                c.drawString(50, y, p.text)
                y -= 20
                if y < 50:
                    c.showPage()
                    y = 800

        # ---- PDF handling (placeholder) ----
        elif self.doc_path.endswith(".pdf"):
            c.drawString(100, 750, "PDF content copied (preview simplified)")

        # ---- Add image as last page ----
        c.showPage()
        img = Image.open(self.img_path)
        temp_img = "temp.jpg"
        img.save(temp_img)

        c.drawImage(temp_img, 50, 200, width=500, preserveAspectRatio=True)

        c.save()

        self.root.ids.share_btn.disabled = False

    # -------- SHARE --------

    def share_file(self):
        if platform.system() == "Windows":
            import webbrowser
            webbrowser.open(self.output_pdf)
        else:
            try:
                from jnius import autoclass

                Intent = autoclass('android.content.Intent')
                File = autoclass('java.io.File')
                Uri = autoclass('android.net.Uri')
                PythonActivity = autoclass('org.kivy.android.PythonActivity')

                intent = Intent()
                intent.setAction(Intent.ACTION_SEND)
                intent.setType("application/pdf")

                file = File(self.output_pdf)
                uri = Uri.fromFile(file)

                intent.putExtra(Intent.EXTRA_STREAM, uri)

                currentActivity = PythonActivity.mActivity
                currentActivity.startActivity(
                    Intent.createChooser(intent, "Share PDF")
                )

            except Exception as e:
                print("Share failed:", e)


if __name__ == "__main__":
    KiwiApp().run()