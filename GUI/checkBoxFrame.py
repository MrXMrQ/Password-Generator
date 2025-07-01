import customtkinter as ctk


class CheckBoxFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self._selected_length = 12

        self.use_special = ctk.BooleanVar(value=False)
        self.use_upper = ctk.BooleanVar(value=False)
        self.use_numbers = ctk.BooleanVar(value=False)

        self.length_checkboxes = []
        self.length_values = [12, 16, 24]

        for i, val in enumerate(self.length_values):
            checkbox = ctk.CTkCheckBox(
                self,
                text=str(val),
                font=("Inter", 16, "bold"),
                command=lambda v=val: self.select_length(v),
            )
            checkbox.grid(
                row=0,
                column=i,
                padx=20,
                pady=5,
                sticky="nsew",
            )
            self.length_checkboxes.append(checkbox)

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
            checkbox.grid(
                row=1,
                column=i,
                padx=20,
                pady=5,
                sticky="nsew",
            )

        self.select_length(12)

    def select_length(self, value) -> None:
        self._selected_length = value
        for cb, val in zip(self.length_checkboxes, self.length_values):
            if val == value:
                cb.select()
            else:
                cb.deselect()
        print(f"Aktuelle Länge: {self._selected_length}")

    @property
    def selected_length(self) -> int:
        return self._selected_length

    @property
    def selected_options(self) -> dict:
        return {
            "special": self.use_special.get(),
            "upper": self.use_upper.get(),
            "numbers": self.use_numbers.get(),
        }
