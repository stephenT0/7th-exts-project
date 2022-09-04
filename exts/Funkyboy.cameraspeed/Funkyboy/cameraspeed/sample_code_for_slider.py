import omni.ext
import omni.ui as ui
class MyExtension(omni.ext.IExt):
    radbt0 = ui.RadioButton
    radbt1 = ui.RadioButton
    def on_startup(self, ext_id):
        print("[funkyboy.hello.world.1] MyExtension startup")
        self._window = ui.Window("My Window", width=300, height=300)
        with self._window.frame:
            with ui.VStack():        
                def on_click():
                    print("clicked!")
                def on_click2():
                    print("clicked!2")
                # Added a clicked function to handle the click call
                def call_clicked(val:int):
                    if val == 0:
                        radbt0.call_clicked_fn()
                    if val == 1:
                        radbt1.call_clicked_fn()
                collection = ui.RadioCollection()
                intSlider = ui.IntSlider(
                    collection.model,
                    min=0,
                    max=1,
                    style={
                        "draw_mode": ui.SliderDrawMode.HANDLE,
                        "background_color": 0xFF00B976,
                        "color": 0xFF00B976,
                        "font_size": 18.0,
                                     })
                # pass lambda arg.get_value_as_int() to call_Clicked(arg.get_value_as_int())
                intSlider.model.add_value_changed_fn(lambda val:call_clicked(val.get_value_as_int()))     
                with ui.HStack():
                    radbt0 = ui.RadioButton(text ="1",radio_collection=collection, clicked_fn=lambda: on_click())
                    radbt1 = ui.RadioButton(text ="2", radio_collection=collection, clicked_fn=lambda: on_click2())
    def on_shutdown(self):
        print("[funkyboy.hello.world.1] MyExtension shutdown")

#Here is the version with the dictionary.

# import omni.ext
# import omni.ui as ui
# class MyExtension(omni.ext.IExt):
#     radbt0 = ui.RadioButton
#     radbt1 = ui.RadioButton
#     def on_startup(self, ext_id):
#         print("[funkyboy.hello.world.1] MyExtension startup")
#         self._window = ui.Window("My Window", width=300, height=300)
#         with self._window.frame:
#             with ui.VStack():        
#                 def on_click():
#                     print("clicked!")
#                 def on_click2():
#                     print("clicked!2")
#                 collection = ui.RadioCollection()
#                 intSlider = ui.IntSlider(
#                     collection.model,
#                     min=0,
#                     max=1,
#                     style={
#                         "draw_mode": ui.SliderDrawMode.HANDLE,
#                         "background_color": 0xFF00B976,
#                         "color": 0xFF00B976,
#                         "font_size": 18.0,
#                                      })
#                 # pass lambda arg.get_value_as_int() to call_clicked[(]arg.get_value_as_int()]()
#                 intSlider.model.add_value_changed_fn(lambda val:call_clicked[val.get_value_as_int()]())     
#                 with ui.HStack():
#                     radbt0 = ui.RadioButton(text ="1",radio_collection=collection, clicked_fn=lambda: on_click())
#                     radbt1 = ui.RadioButton(text ="2", radio_collection=collection, clicked_fn=lambda: on_click2())
#                     # call_clicked ditionary approach
#                     # NOTE: no () at the end of the line, instead it is at the end of the add_value_changed_fn call
#                     call_clicked = {
#                         0:radbt0.call_clicked_fn,
#                         1:radbt1.call_clicked_fn
#                     }
#     def on_shutdown(self):
#         print("[funkyboy.hello.world.1] MyExtension shutdown")

#Thank you @ericcraft-mh from Nvidia Omniverse Discord