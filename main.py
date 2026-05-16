import flet as ft
from pathlib import Path


def main(page: ft.Page):
    page.title = "Final Copy App"
    page.padding = 20
    page.window_width = 500
    page.window_height = 700

    # ---------------- STATE ---------------- #

    doc_path = ""
    image_path = ""

    selected_doc = ft.Text("No document selected")
    selected_image = ft.Text("No image selected")

    result_text = ft.Text()

    # ---------------- BUTTONS ---------------- #

    image_button = ft.ElevatedButton(
        "Choose Image",
        disabled=True,
    )

    final_copy_button = ft.ElevatedButton(
        "Final Copy",
        disabled=True,
    )

    share_button = ft.ElevatedButton(
        "Share",
        disabled=True,
    )

    # ---------------- FILE PICKERS ---------------- #

    def pick_doc_result(e):
        nonlocal doc_path

        if e.files:
            doc_path = e.files[0].path

            selected_doc.value = (
                f"Selected: {Path(doc_path).name}"
            )

            # Enable image selection
            image_button.disabled = False

            page.update()

    def pick_image_result(e):
        nonlocal image_path

        if e.files:
            image_path = e.files[0].path

            selected_image.value = (
                f"Selected: {Path(image_path).name}"
            )

            # Enable final copy button
            final_copy_button.disabled = False

            page.update()

    doc_picker = ft.FilePicker(on_result=pick_doc_result)

    image_picker = ft.FilePicker(on_result=pick_image_result)

    page.overlay.extend([doc_picker, image_picker])

    # ---------------- BUTTON ACTIONS ---------------- #

    def final_copy_clicked(e):
        result_text.value = (
            "Final Copy Ready!\n\n"
            f"Document:\n{doc_path}\n\n"
            f"Image:\n{image_path}"
        )

        # Enable share button
        share_button.disabled = False

        page.update()

    def share_clicked(e):
        result_text.value += "\n\nShared Successfully!"

        page.update()

    # Assign actions after creation
    image_button.on_click = lambda _: image_picker.pick_files(
        allow_multiple=False,
        allowed_extensions=[
            "jpg",
            "jpeg",
            "png",
            "webp",
        ],
    )

    final_copy_button.on_click = final_copy_clicked

    share_button.on_click = share_clicked

    # ---------------- UI ---------------- #

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Final Copy Application",
                    size=30,
                    weight="bold",
                ),

                ft.Divider(),

                ft.Text(
                    "Step 1: Choose DOC/PDF File"
                ),

                ft.ElevatedButton(
                    "Choose Document",
                    on_click=lambda _: doc_picker.pick_files(
                        allow_multiple=False,
                        allowed_extensions=[
                            "pdf",
                            "doc",
                            "docx",
                        ],
                    ),
                ),

                selected_doc,

                ft.Divider(),

                ft.Text(
                    "Step 2: Choose Image"
                ),

                image_button,

                selected_image,

                ft.Divider(),

                ft.Row(
                    [
                        final_copy_button,
                        share_button,
                    ]
                ),

                ft.Divider(),

                result_text,
            ],
            spacing=20,
        )
    )


ft.app(target=main)