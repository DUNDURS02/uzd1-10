from googletrans import Translator
import tkinter as tk
from tkinter import ttk

def translate_text():
    input_text = input_text_area.get("1.0", "end-1c")
    
    target_lang = lang_combo.get()
    
    translator = Translator()
    
    try:
        translated = translator.translate(input_text, dest=target_lang)
        output_text_area.delete("1.0", "end")
        output_text_area.insert("1.0", translated.text)
    except Exception as e:
        output_text_area.delete("1.0", "end")
        output_text_area.insert("1.0", f"Kļūda: {str(e)}")

root = tk.Tk()
root.title("Teksta tulkotājs")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

input_text_area_label = tk.Label(root, text="Ievadiet tekstu:", font=("Arial", 12), bg="#f0f0f0")
input_text_area_label.pack(pady=5)

input_text_area = tk.Text(root, height=6, width=50, font=("Arial", 12))
input_text_area.pack(pady=10)

lang_label = tk.Label(root, text="Izvēlieties mērķa valodu:", font=("Arial", 12), bg="#f0f0f0")
lang_label.pack(pady=5)

languages = ['en', 'lv', 'es', 'fr', 'de', 'it', 'ru', 'lt']
lang_combo = ttk.Combobox(root, values=languages, state="readonly", width=10, font=("Arial", 12))
lang_combo.set('en')
lang_combo.pack(pady=5)

translate_button = tk.Button(root, text="Tulkot", command=translate_text, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", height=2, width=20)
translate_button.pack(pady=15)

output_text_area_label = tk.Label(root, text="Tulkošanas rezultāts:", font=("Arial", 12), bg="#f0f0f0")
output_text_area_label.pack(pady=5)

output_text_area = tk.Text(root, height=6, width=50, font=("Arial", 12))
output_text_area.pack(pady=10)

root.mainloop()
