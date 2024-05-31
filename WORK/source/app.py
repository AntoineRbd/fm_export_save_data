import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


class SaveRecap(toga.App):
    def startup(self):

        brutus_icon = "icons/brutus"
        cricket_icon = "icons/cricket-72.png"

        self.file_path_box = toga.Box()

        self.path_box = toga.Box()
        self.path_input = toga.TextInput()
        self.path_label = toga.Label("Entrer le chemin d'accès au fichier", style=Pack(text_align=RIGHT))
    
        self.path_box.add(self.path_input)
        self.path_box.add(self.path_label)
        self.file_path_box.add(self.path_box)

        self.file_path_box.style.update(direction=COLUMN, padding=10)
        self.path_box.style.update(direction=ROW, padding=5)
        self.path_input.style.update(flex=1, padding_left=210)
        self.path_label.style.update(width=100, padding_left=10)

        self.main_window = toga.MainWindow()
        # Command 2 has not been *explicitly* added to the app. Adding it to
        # a toolbar implicitly adds it to the app.
        self.main_window.content = self.file_path_box

        self.main_window.show()


def main():
    return SaveRecap("Save Recapitulator", "org.beeware.toga.tutorial")