import customtkinter as ctk
import string
import random
import pyperclip
from math import floor, ceil

from GUI.window import CheckBoxFrame


class OutPutFrame(ctk.CTkFrame):
    def __init__(self, master, checkBoxFrame: CheckBoxFrame, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

        self._checkBoxFrame = checkBoxFrame

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._special_chars = [
            "!",
            '"',
            "#",
            "$",
            "%",
            "&",
            "(",
            ")",
            "*",
            "+",
            "-",
            "/",
            ":",
            ";",
            "<",
            "=",
            ">",
            "?",
            "@",
            "[",
            "]",
            "^",
            "~",
            "@",
        ]
        self._numbers = list(string.digits)
        self._lowercase_letters = list(string.ascii_lowercase)
        self._uppercase_letters = list(string.ascii_uppercase)

        self.textbox = ctk.CTkTextbox(
            self, height=50, width=550, font=("Inter", 25, "bold"), text_color="white"
        )
        self.textbox.configure(state="disabled")
        self.textbox.grid(row=0, column=0, padx=10, pady=(40, 0))

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=1, column=0, pady=(0, 40))

        self.generate_button = ctk.CTkButton(
            button_frame, text="Generieren", command=self.generate
        )
        self.generate_button.grid(row=0, column=0, padx=10)

        self.copy_button = ctk.CTkButton(
            button_frame, text="Kopieren", command=self.copy
        )
        self.copy_button.grid(row=0, column=1, padx=10)

    def generate(self) -> None:
        self._clear()
        self.textbox.insert("0.0", self._password_gen())
        self.textbox.configure(state="disabled")

    def _password_gen(self) -> str:
        length = self._checkBoxFrame.selected_length
        options = self._checkBoxFrame.selected_options

        groups = []
        if options["special"]:
            groups.append(self._special_chars)
        if options["numbers"]:
            groups.append(self._numbers)
        if options["upper"]:
            groups.append(self._uppercase_letters)

        groups.append(self._lowercase_letters)

        num_groups = len(groups)
        ideal_count = length / num_groups
        min_count = floor(ideal_count * 0.9)
        max_count = ceil(ideal_count * 1.1)

        counts = [int(ideal_count)] * num_groups
        total = sum(counts)

        i = 0
        while total < length:
            if counts[i] < max_count:
                counts[i] += 1
                total += 1
            i = (i + 1) % num_groups
        while total > length:
            if counts[i] > min_count:
                counts[i] -= 1
                total -= 1
            i = (i + 1) % num_groups

        password_chars = []
        for group, count in zip(groups, counts):
            password_chars.extend(random.choices(group, k=count))

        random.shuffle(password_chars)
        return "".join(password_chars)

    def _clear(self) -> None:
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")

    def copy(self) -> None:
        pyperclip.copy(self.textbox.get("0.0", "end"))
