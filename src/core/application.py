import dearpygui.dearpygui as dpg

class Application:
    def __init__(self):
        print("Initializing application")

        dpg.create_context()
        dpg.create_viewport(title="Kingdom IDE", width=1024, height=600)
        dpg.setup_dearpygui()

    def run(self):
        dpg.show_viewport()

        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        
        quit()

    def quit(self):
        print("Application finished")
        dpg.destroy_context()
