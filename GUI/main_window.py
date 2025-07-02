import customtkinter as ctk
from GUI.check_box_frame import CheckBoxFrame
from GUI.output_frame import OutputFrame


class MainWindow(ctk.CTk):
    """Main application window."""

    PADDING = 10

    def __init__(self, title: str, width: int, height: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(True, True)

        self._setup_grid()
        self._create_widgets()

    def _setup_grid(self) -> None:
        """Configure main window grid."""
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def _create_widgets(self) -> None:
        """Create and place all widgets."""
        # Main panel
        panel = ctk.CTkFrame(self)
        panel.grid_rowconfigure((0, 1), weight=1)
        panel.grid_columnconfigure(0, weight=1)
        panel.grid(row=0, column=0, sticky="nsew", padx=self.PADDING, pady=self.PADDING)

        # Checkbox frame
        checkbox_frame = CheckBoxFrame(panel)
        checkbox_frame.grid(
            row=1, column=0, sticky="nsew", padx=self.PADDING, pady=self.PADDING
        )

        # Output frame
        output_frame = OutputFrame(panel, checkbox_frame)
        output_frame.grid(
            row=0, column=0, sticky="nsew", padx=self.PADDING, pady=self.PADDING
        )
