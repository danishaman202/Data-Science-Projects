import tkinter as tk
from tkinter import messagebox
from scraper import RottenTomatoesScraper

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rotten Tomatoes TV Series Scraper")
        self.geometry("400x200")
        self.configure(bg="#F0F0F0")  # Set background color
        
        # Create and style widgets
        self.label = tk.Label(self, text="Enter TV Series Name:", bg="#F0F0F0", font=("Helvetica", 14))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self, font=("Helvetica", 12))
        self.entry.pack(padx=20, pady=5, fill="x")
        
        self.button = tk.Button(self, text="Search", command=self.search_tv_series, font=("Helvetica", 12), bg="#007acc", fg="#FFFFFF", relief="raised")
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(self, text="", bg="#F0F0F0", font=("Helvetica", 12))
        self.result_label.pack(padx=20, pady=5, fill="both")

    def search_tv_series(self):
        series_name = self.entry.get()
        series_name = series_name.lower()
        
        # Handle series name formatting (removing special characters, replacing spaces)
        series_name = series_name.replace(",", "").replace("'", "")
        series_name = "_".join(series_name.split())
        
        if series_name:
            scraper = RottenTomatoesScraper()
            try:
                scores = scraper.get_scores(series_name)
                self.result_label.config(text=f"Rotten Tomato Score: {scores['rotten_tomato_score']}\nAudience Score: {scores['audience_score']}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Please enter a TV series name.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
