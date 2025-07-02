import customtkinter as ctk
from typing import Dict


class CheckBoxFrame(ctk.CTkFrame):
    """Frame containing checkboxes for password length and character options."""

    DEFAULT_LENGTH = 12
    LENGTH_OPTIONS = [12, 16, 24]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._setup_grid()
        self._initialize_variables()
        self._create_widgets()
        self.select_length(self.DEFAULT_LENGTH)

    def _setup_grid(self) -> None:
        """Configure grid layout for the frame."""
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def _initialize_variables(self) -> None:
        """Initialize instance variables."""
        self._selected_length = self.DEFAULT_LENGTH
        self.use_special = ctk.BooleanVar(value=False)
        self.use_upper = ctk.BooleanVar(value=False)
        self.use_numbers = ctk.BooleanVar(value=False)
        self.length_checkboxes = []

    def _create_widgets(self) -> None:
        """Create and place all widgets."""
        self._create_length_checkboxes()
        self._create_option_checkboxes()

    def _create_length_checkboxes(self) -> None:
        """Create checkboxes for password length selection."""
        for i, length in enumerate(self.LENGTH_OPTIONS):
            checkbox = ctk.CTkCheckBox(
                self,
                text=str(length),
                font=("Inter", 16, "bold"),
                command=lambda v=length: self.select_length(v),
            )
            checkbox.grid(row=0, column=i, padx=20, pady=5, sticky="nsew")
            self.length_checkboxes.append(checkbox)

    def _create_option_checkboxes(self) -> None:
        """Create checkboxes for character type options."""
        options = [
            ("Sonderzeichen", self.use_special),
            ("Großbuchstaben", self.use_upper),
            ("Zahlen", self.use_numbers),
        ]

        for i, (text, var) in enumerate(options):
            checkbox = ctk.CTkCheckBox(
                self,
                text=text,
                font=("Inter", 16, "bold"),
                variable=var,
            )
            checkbox.grid(row=1, column=i, padx=20, pady=5, sticky="nsew")

    def select_length(self, value: int) -> None:
        """Select a specific length and update checkboxes accordingly."""
        self._selected_length = value
        for checkbox, length in zip(self.length_checkboxes, self.LENGTH_OPTIONS):
            if length == value:
                checkbox.select()
            else:
                checkbox.deselect()

    @property
    def selected_length(self) -> int:
        """Get the currently selected password length."""
        return self._selected_length

    @property
    def selected_options(self) -> Dict[str, bool]:
        """Get the currently selected character options."""
        return {
            "special": self.use_special.get(),
            "upper": self.use_upper.get(),
            "numbers": self.use_numbers.get(),
        }
