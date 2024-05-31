import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack
import logging

class SaveRecapitulatorManager(toga.App):
    def startup(self):

        brutus_icon = "icons/brutus"
        cricket_icon = "icons/cricket-72.png"

        self.logger = logging.getLogger('SaveRecapitulator App')
        self.main_box = toga.Box()

        rtf_box = toga.Box()
        rtf_lab = toga.Label(text="RTF File: ")
        rtf_lab.style.update(width=125)
        self.rtf_inp = toga.TextInput(readonly=True)
        self.rtf_inp.style.update(direction=ROW, padding=(0, 20), flex=1)
        self.rtf_btn = toga.Button(text="...", on_press=self.action_open_file_dialog, enabled=True)

        rtf_box.add(rtf_lab)
        rtf_box.add(self.rtf_inp)
        rtf_box.add(self.rtf_btn)

        self.main_box.add(rtf_box)


        self.main_window = toga.MainWindow()
        # Command 2 has not been *explicitly* added to the app. Adding it to
        # a toolbar implicitly adds it to the app.
        self.main_window.content = self.main_box

        self.main_window.show()

    async def action_open_file_dialog(self, widget):
        self.logger.info("Select File...")
        try:
            fname = await self.main_window.open_file_dialog(
                title="Open RTF file",
                multiple_select=False,
                file_types=['rtf']
            )
            self.logger.info("Created file-dialog")
            if fname is not None:
                fname = str(fname)
                self.rtf_inp.value = fname
                #self.profile_manager.prf_cfg['rtf'] = fname
                self.path_name = fname
                self.logger.info("RTF file: " + fname)
                #Config_Manager().save_config(str(self.paths.app)+"/.user/"+self.profile_manager.cur_prf+".json", self.profile_manager.prf_cfg)
            else:
                #self.profile_manager.prf_cfg['rtf'] = ""
                self.rtf_inp.value = ""
                #Config_Manager().save_config(str(self.paths.app)+"/.user/"+self.profile_manager.cur_prf+".json", self.profile_manager.prf_cfg)
        except Exception:
            self.logger.error("Fatal error in main loop", exc_info=True)
            pass


def main():
    return SaveRecapitulatorManager("Save Recapitulator", "org.beeware.toga.tutorial")