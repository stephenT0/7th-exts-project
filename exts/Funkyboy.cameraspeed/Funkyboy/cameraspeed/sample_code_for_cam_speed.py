import omni.ext
import omni.ui as ui
import carb.settings
import carb

class MyExtension(omni.ext.IExt):

    def on_startup(self, ext_id):
        CAMERA_VEL = "/persistent/app/viewport/camMoveVelocity" # Camera velocity setting
        self._settings = carb.settings.get_settings() # Grab carb settings
        self._window = ui.Window("My Window", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                ui.Label("Some Label")
                def on_click():
                    carb.log_info(f"Camera velocity before: {self._settings.get_as_string(CAMERA_VEL)}")
                    # Here is the function we use to set setting values. Setting values are stored inside of carb
                    # so we have to give it the path for that setting, hence why we have CAMERA_VEL
                    # 100 is the new camera speed that is hard coded in, you could put any number there
                    self._settings.set(CAMERA_VEL, 100)
                    carb.log_info(f"Camera velocity after: {self._settings.get_as_string(CAMERA_VEL)}")
                ui.Button("Click Me", clicked_fn=lambda: on_click())

    def on_shutdown(self):
        print("[omni.code.snippets] MyExtension shutdown")

#Thank you Jen from Nvidia Omniverse Discord