from turtle import onclick
import customtkinter as ctk

from GUI import checkBoxFrame


class OutPutFrame(ctk.CTkFrame):
    def __init__(
        self, master, checkBoxFrame: checkBoxFrame, fg_color: str, *args, **kwargs
    ) -> None:
        super().__init__(master=master, fg_color=fg_color, *args, **kwargs)

        self._checkBoxFrame = checkBoxFrame

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        textbox = ctk.CTkTextbox(self, height=75)
        textbox.insert("0.0", "Hier wird Text angezeigt.")
        textbox.configure(state="disabled")
        textbox.grid(row=0, column=0, columnspan=1, sticky="ew", padx=50)

        rerollButton = ctk.CTkButton(self, text="test", command=self.rerollClick)
        rerollButton.grid(
            row=1,
            column=0,
            sticky="ew",
        )

        copyButton = ctk.CTkButton(self, text="test", command=self.rerollClick)
        copyButton.grid(
            row=1,
            column=1,
            sticky="ew",
        )

    def click(self) -> None:
        print(self._checkBoxFrame.selected_options)
        self.clipboard_clear()  # alten Clipboard-Inhalt löschen
        self.clipboard_append(self.output_text)  # neuen Text setzen
        self.update()

    def copyClick(self) -> None:
        pass

    def rerollClick(self) -> None:
        pass
