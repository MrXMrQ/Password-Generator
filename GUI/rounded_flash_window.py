import customtkinter as ctk


class RoundedFlashWindow(ctk.CTkToplevel):
    """Animated popup window that shows a message and fades out."""

    DEFAULT_COLOR = "#0078D7"
    DEFAULT_TEXT_COLOR = "white"
    DEFAULT_FONT_SIZE = 24

    def __init__(self, master, text="Kopiert!", duration=1000, move_up=50, radius=20):
        super().__init__(master)
        self.duration = duration
        self.move_up = move_up
        self.radius = radius

        self._setup_window()
        self._create_widgets(text)
        self._calculate_position(master)
        self._initialize_animation()
        self.animate()

    def _setup_window(self) -> None:
        """Configure window properties."""
        self.overrideredirect(True)
        self.attributes("-topmost", True)

    def _create_widgets(self, text: str) -> None:
        """Create and configure the frame and label."""
        self.frame = ctk.CTkFrame(
            self, fg_color=self.DEFAULT_COLOR, corner_radius=self.radius
        )
        self.frame.pack(fill="both", expand=True)

        self.label = ctk.CTkLabel(
            self.frame,
            text=text,
            text_color=self.DEFAULT_TEXT_COLOR,
            font=ctk.CTkFont(size=self.DEFAULT_FONT_SIZE, weight="bold"),
        )
        self.label.pack(padx=30, pady=30)

    def _calculate_position(self, master) -> None:
        """Calculate and set initial window position."""
        self.start_x = master.winfo_rootx() + 100
        self.start_y = master.winfo_rooty() + 100
        self.geometry(f"+{self.start_x}+{self.start_y}")

    def _initialize_animation(self) -> None:
        """Initialize animation parameters."""
        self.opacity = 1.0
        self.steps = 30
        self.step_duration = self.duration // self.steps
        self.dy = self.move_up / self.steps
        self.current_step = 0

    def animate(self) -> None:
        """Animate the window movement and fade out."""
        if self.current_step >= self.steps:
            self.destroy()
            return

        # Update position
        new_y = int(self.start_y - self.dy * self.current_step)
        self.geometry(f"+{self.start_x}+{new_y}")

        # Update opacity
        new_opacity = max(0, self.opacity - (self.current_step / self.steps))
        self.attributes("-alpha", new_opacity)

        self.current_step += 1
        self.after(self.step_duration, self.animate)
