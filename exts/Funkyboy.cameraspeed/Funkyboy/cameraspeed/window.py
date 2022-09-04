import omni.ext
import omni.ui as ui
import carb.settings
import carb
import omni.kit.commands
from .style import style1

WINDOW_TITLE = "Camera Speed Selector"

class SimpleCamWindow(ui.Window):
    def __init__(self, title, menu_path):
        super().__init__(title, width=300, height=150)
        self._menu_path = menu_path
        self.set_visibility_changed_fn(self._on_visibility_changed)
        self._build_ui()
    
    def on_shutdown(self):
        self._win = None

    def show(self):
        self.visible = True
        self.focus()    
    
    def hide(self):
        self.visible = False


    def _build_ui(self):
        """
        The method that is called to build all the UI once the window is
        visible.
        """
        CAMERA_VEL = "/persistent/app/viewport/camMoveVelocity" # Camera velocity setting
        self._settings = carb.settings.get_settings() # Grab carb settings

        with self.frame:
            with ui.VStack():
                ui.Button("Select a Camera Speed", style={"background_color":0xFF6FF, "color":0xFF00B976, "font_size":20,},  tooltip="  right click + WASD to fly  ")
# Defining function to Change the Camera Speed
                def on_click():
                    self._settings.set(CAMERA_VEL, 0.01)
                    carb.log_info(f"Camera velocity set to {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click2():
                    self._settings.set(CAMERA_VEL, 0.1)
                    carb.log_info(f"Camera velocity set to {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click3():
                    self._settings.set(CAMERA_VEL, 0.5)
                    carb.log_info(f"Camera velocity set to {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click4():
                    self._settings.set(CAMERA_VEL, 2.5)
                    carb.log_info(f"Camera velocity set to {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click5():
                    self._settings.set(CAMERA_VEL, 5.0)
                    carb.log_info(f"Camera velocity set to {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click6():
                    self._settings.set(CAMERA_VEL, 7.5)
                    carb.log_info(f"Camera velocity set to {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click7():
                    self._settings.set(CAMERA_VEL, 10.0)
                    carb.log_info(f"Camera velocity set to {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click8():
                    self._settings.set(CAMERA_VEL, 20.0)
                    carb.log_info(f"Camera velocity set to: {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click9():
                    self._settings.set(CAMERA_VEL, 30.0)
                    carb.log_info(f"Camera velocity set to: {self._settings.get_as_float(CAMERA_VEL)}")
                def on_click10():
                    self._settings.set(CAMERA_VEL, 50.0)
                    carb.log_info(f"Camera velocity set to: {self._settings.get_as_float(CAMERA_VEL)}")                                        
                def on_click11():
                    omni.kit.commands.execute('DuplicateFromActiveViewportCameraCommand', viewport_name='Viewport')

# Added a clicked function to handle the click call
                def call_clicked(val:int):
                    if val == 0:
                        radbt0.call_clicked_fn()
                    if val == 1:
                        radbt1.call_clicked_fn()
                    if val == 2:
                        radbt2.call_clicked_fn()
                    if val == 3:
                        radbt3.call_clicked_fn()                        
                    if val == 4:
                        radbt4.call_clicked_fn()
                    if val == 5:
                        radbt5.call_clicked_fn()
                    if val == 6:
                        radbt6.call_clicked_fn()
                    if val == 7:
                        radbt7.call_clicked_fn()
                    if val == 8:
                        radbt8.call_clicked_fn()
                    if val == 9:
                        radbt9.call_clicked_fn()                                                                                                  


#the slider
                collection = ui.RadioCollection()
                
                intSlider = ui.IntSlider(
                    collection.model,
                    min=0,
                    max=9,
                    style={
                        "draw_mode": ui.SliderDrawMode.HANDLE,
                        "background_color": 0xFF00B976,
                        "color": 0xFF00B976,
                        "font_size": 14.0,
                                     })            

                intSlider.model.add_value_changed_fn(lambda val:call_clicked(val.get_value_as_int()))
#the buttons
                with ui.HStack(style=style1):
                    radbt0 = ui.RadioButton(text ="1", name="one", radio_collection=collection, clicked_fn=lambda: on_click())
                    radbt1 = ui.RadioButton(text ="2", name="two", radio_collection=collection, clicked_fn=lambda: on_click2())
                    radbt2 = ui.RadioButton(text ="3", name="three", radio_collection=collection, clicked_fn=lambda: on_click3())
                    radbt3 = ui.RadioButton(text ="4", name="four", radio_collection=collection, clicked_fn=lambda: on_click4())
                    radbt4 = ui.RadioButton(text ="5", name="five", radio_collection=collection, clicked_fn=lambda: on_click5())
                    radbt5 = ui.RadioButton(text ="6", name="six", radio_collection=collection, clicked_fn=lambda: on_click6())
                    radbt6 = ui.RadioButton(text ="7", name="seven", radio_collection=collection, clicked_fn=lambda: on_click7())
                    radbt7 = ui.RadioButton(text ="8", name="eight", radio_collection=collection, clicked_fn=lambda: on_click8())
                    radbt8 = ui.RadioButton(text ="9", name="nine", radio_collection=collection, clicked_fn=lambda: on_click9())
                    radbt9 = ui.RadioButton(text ="10", name="ten", radio_collection=collection, clicked_fn=lambda: on_click10())
    
    def _on_visibility_changed(self, visible):
        omni.kit.ui.get_editor_menu().set_value(self._menu_path, visible)