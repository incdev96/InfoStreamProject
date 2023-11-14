import tkinter as tk

class TextScroller:
    def __init__(self, root):
        self.root = root
        self.root.title("Info Stream")
        
        # Déterminez la largeur et la hauteur de l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = 100  # Hauteur de 100px

        # Créez une toile pour afficher le texte
        self.canvas = tk.Canvas(self.root, width=screen_width, height=screen_height)
        self.canvas.pack()

        # Textes à dérouler
        self.texts = [
            "Premier informations de la journée.",
            "Deuxième informations de la journée",
            "Et la troisième informations de la journée qui défile.",
        ]

        self.current_text = 0  # Texte actuellement affiché
        self.text_speed = 2  # Vitesse de défilement des textes (plus la valeur est grande, plus c'est rapide)
        
        # Affichez le premier texte
        self.display_text()

    def display_text(self):
        text = self.texts[self.current_text - 1]
        text_width = self.canvas.create_text(0, 50, text=text, anchor="w", fill="red", font=("Helvetica", 24, "bold"))

        # Faites dérouler le texte de gauche à droite
        self.scroll_text(text_width, 0)

        # Mettez la fenêtre au-dessus des autres
        self.root.attributes("-topmost", True)

    def scroll_text(self, text_id, x):
        self.canvas.coords(text_id, x, 50)
        if x < self.canvas.winfo_width():
            self.root.after(10, self.scroll_text, text_id, x + self.text_speed)
        else:
            self.canvas.delete(text_id)
            self.current_text = (self.current_text + 1) % len(self.texts)
            self.root.after(1000, self.display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextScroller(root)
    root.mainloop()
