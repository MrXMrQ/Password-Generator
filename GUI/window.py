import customtkinter as ctk

from GUI.checkBoxFrame import CheckBoxFrame
from GUI.ouputFrame import OutPutFrame


class Window(ctk.CTk):
    _PADX = 10
    _PADY = 10

    def __init__(self, title, width, height, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(True, True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        panel = ctk.CTkFrame(self)
        panel.grid_rowconfigure((0, 1), weight=1)
        panel.grid_columnconfigure(0, weight=1)
        panel.grid(row=0, column=0, sticky="nsew", padx=Window._PADX, pady=Window._PADY)

        checkBoxFrame = CheckBoxFrame(panel)
        checkBoxFrame.grid(
            row=1, column=0, sticky="nsew", padx=Window._PADX, pady=Window._PADY
        )

        outputFrame = OutPutFrame(panel, checkBoxFrame)
        outputFrame.grid(
            row=0, column=0, sticky="nsew", padx=Window._PADX, pady=Window._PADY
        )
