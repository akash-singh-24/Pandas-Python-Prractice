import tkinter as tk
from datetime import datetime

class WPMCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-time WPM Calculator")

        self.start_time = None
        self.char_count = 0
        self.text_to_type = ("The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet "
                             "and is often used for typing practice.")

        self.label = tk.Label(root, text="Type the following paragraph:", font=('Helvetica', 14))
        self.label.pack(pady=10)

        self.paragraph = tk.Label(root, text=self.text_to_type, wraplength=600, font=('Helvetica', 14), justify="left")
        self.paragraph.pack(pady=10)

        self.text_box = tk.Text(root, width=60, height=10, font=('Helvetica', 14))
        self.text_box.pack(pady=10)
        self.text_box.bind("<KeyRelease>", self.calculate_wpm)

        self.wpm_label = tk.Label(root, text="WPM: 0", font=('Helvetica', 14))
        self.wpm_label.pack(pady=10)

    def calculate_wpm(self, event):
        if not self.start_time:
            self.start_time = datetime.now()

        typed_text = self.text_box.get("1.0", tk.END).strip()
        self.char_count = len(typed_text)

        if self.char_count == 0:
            self.start_time = None
            self.wpm_label.config(text="WPM: 0")
            return

        # Highlight correct and incorrect characters
        self.highlight_text(typed_text)

        # Calculate WPM
        elapsed_time = (datetime.now() - self.start_time).total_seconds() / 60
        word_count = self.char_count / 5  # Average word length is 5 characters
        wpm = word_count / elapsed_time
        self.wpm_label.config(text=f"WPM: {int(wpm)}")

    def highlight_text(self, typed_text):
        self.text_box.tag_remove("correct", "1.0", tk.END)
        self.text_box.tag_remove("incorrect", "1.0", tk.END)

        for i, char in enumerate(typed_text):
            if i < len(self.text_to_type):
                if char == self.text_to_type[i]:
                    self.text_box.tag_add("correct", f"1.{i}", f"1.{i+1}")
                else:
                    self.text_box.tag_add("incorrect", f"1.{i}", f"1.{i+1}")
            else:
                self.text_box.tag_add("incorrect", f"1.{i}", f"1.{i+1}")

        self.text_box.tag_config("correct", foreground="green")
        self.text_box.tag_config("incorrect", foreground="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = WPMCalculator(root)
    root.mainloop()
