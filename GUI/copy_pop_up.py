import customtkinter as ctk


class RoundedFlashWindow(ctk.CTkToplevel):
    def __init__(self, master, text="Kopiert!", duration=1000, move_up=50, radius=20):
        super().__init__(master)
        self.overrideredirect(True)
        self.attributes("-topmost", True)

        self.duration = duration
        self.move_up = move_up
        self.radius = radius

        self.frame = ctk.CTkFrame(self, fg_color="#0078D7", corner_radius=radius)
        self.frame.pack(fill="both", expand=True)

        self.label = ctk.CTkLabel(
            self.frame,
            text=text,
            text_color="white",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        self.label.pack(padx=30, pady=30)

        self.start_x = master.winfo_rootx() + 100
        self.start_y = master.winfo_rooty() + 100
        self.geometry(f"+{self.start_x}+{self.start_y}")

        self.opacity = 1.0
        self.steps = 30
        self.step_duration = self.duration // self.steps
        self.dy = self.move_up / self.steps
        self.current_step = 0

        self.animate()

    def animate(self):
        if self.current_step >= self.steps:
            self.destroy()
            return

        new_y = int(self.start_y - self.dy * self.current_step)
        self.geometry(f"+{self.start_x}+{new_y}")

        new_opacity = max(0, self.opacity - (self.current_step / self.steps))
        self.attributes("-alpha", new_opacity)

        self.current_step += 1
        self.after(self.step_duration, self.animate)
