import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


class SaveRecap(toga.App):
    def __init__(self):
        super().__init__()
        
    def startup(self):
        self.formal_name = "Save Recapitulator"
        self.path_box = toga.Box()
        
        self.path_input = toga.Textinput(readonly=True)
        self.path_input_box_label = toga.Label("Entrer le chemin d'acces vers le fichier", style=Pack(text_align=RIGHT))
        
        self.path_box.add(self.path_input_box_label)
        self.path_box.add(self.path_input)
        
        self.main_window = toga.MainWindow(title=self.formal_name, size=(1000, 600))
        

if __name__ == "__main__":
    SaveRecap()
