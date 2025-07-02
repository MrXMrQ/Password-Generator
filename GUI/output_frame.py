from cgitb import text
import customtkinter as ctk
import pyperclip
from GUI.rounded_flash_window import RoundedFlashWindow
from GUI.check_box_frame import CheckBoxFrame
from password_generator import PasswordGenerator


class OutputFrame(ctk.CTkFrame):
    """Frame containing password output and control buttons."""

    TEXTBOX_HEIGHT = 50
    TEXTBOX_WIDTH = 550
    FONT_CONFIG = ("Inter", 25, "bold")

    def __init__(self, master, checkbox_frame: CheckBoxFrame, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.checkbox_frame = checkbox_frame
        self.password_generator = PasswordGenerator()

        self._setup_grid()
        self._create_widgets()

    def _setup_grid(self) -> None:
        """Configure grid layout for the frame."""
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

    def _create_widgets(self) -> None:
        """Create and place all widgets."""
        self._create_textbox()
        self._create_buttons()

    def _create_textbox(self) -> None:
        """Create the password display textbox."""
        self.textbox = ctk.CTkTextbox(
            self,
            height=self.TEXTBOX_HEIGHT,
            width=self.TEXTBOX_WIDTH,
            font=self.FONT_CONFIG,
            text_color="white",
        )
        self.textbox.insert(
            "0.0",
            self.password_generator.generate(
                self.checkbox_frame.selected_length,
                self.checkbox_frame.selected_options,
            ),
        )
        self.textbox.configure(state="disabled")
        self.textbox.grid(row=0, column=0, padx=10, pady=(40, 0))

    def _create_buttons(self) -> None:
        """Create the control buttons."""
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=1, column=0, pady=(0, 40))

        self.generate_button = ctk.CTkButton(
            button_frame, text="Generieren", command=self.generate_password
        )
        self.generate_button.grid(row=0, column=0, padx=10)

        self.copy_button = ctk.CTkButton(
            button_frame, text="Kopieren", command=self.copy_password
        )
        self.copy_button.grid(row=0, column=1, padx=10)

    def generate_password(self) -> None:
        """Generate and display a new password."""
        self._clear_textbox()

        length = self.checkbox_frame.selected_length
        options = self.checkbox_frame.selected_options
        password = self.password_generator.generate(length, options)

        self.textbox.insert("0.0", password)
        self.textbox.configure(state="disabled")

    def copy_password(self) -> None:
        """Copy the current password to clipboard and show notification."""
        password = self.textbox.get("0.0", "end-1c")  # Remove trailing newline
        if password.strip():  # Only copy if there's actually a password
            pyperclip.copy(password)
            RoundedFlashWindow(self, duration=800, move_up=40, radius=20)

    def _clear_textbox(self) -> None:
        """Clear the textbox content."""
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
