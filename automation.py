import tkinter as tk
from tkinter import messagebox
import requests
import re

# ===============================
# Scrape Webpage Title Function
# ===============================
def scrape_title():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a valid URL!")
        return

    try:
        response = requests.get(url)
        html = response.text

        # Extract title using regex
        title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)

        if title_match:
            title = title_match.group(1)

            # Save to file
            with open("webpage_title.txt", "w", encoding="utf-8") as file:
                file.write(title)

            result_label.config(text=f"Title: {title}", fg="#00ff99")
        else:
            result_label.config(text="Title not found!", fg="yellow")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch webpage.\n{e}")

# ===============================
# GUI Design
# ===============================
root = tk.Tk()
root.title("Webpage Title Scraper")
root.geometry("450x300")
root.configure(bg="#1e1e2f")

title_label = tk.Label(root,
                       text="🌐 Webpage Title Scraper",
                       font=("Arial", 18, "bold"),
                       bg="#1e1e2f",
                       fg="white")
title_label.pack(pady=20)

tk.Label(root,
         text="Enter Website URL:",
         bg="#1e1e2f",
         fg="white").pack(pady=5)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

tk.Button(root,
          text="Scrape Title",
          font=("Arial", 12),
          bg="#4CAF50",
          fg="white",
          command=scrape_title).pack(pady=15)

result_label = tk.Label(root,
                        text="",
                        wraplength=400,
                        bg="#1e1e2f")
result_label.pack(pady=10)

root.mainloop()