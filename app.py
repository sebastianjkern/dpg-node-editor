import os
import shutil

import dearpygui.dearpygui as dpg

if not os.path.exists("user_custom_layout.ini"):
    shutil.copy("custom_layout.ini", "user_custom_layout.ini")

dpg.create_context()
dpg.configure_app(docking=True, docking_space=True, init_file="user_custom_layout.ini")
dpg.create_viewport(title='Node Editor', width=800, height=600)
dpg.setup_dearpygui()

# left_window = dpg.generate_uuid()
# right_window = dpg.generate_uuid()
# top_window = dpg.generate_uuid()
# bottom_window = dpg.generate_uuid()
center_window = dpg.generate_uuid()

# add a font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("Arial.ttf", 14)
    dpg.bind_font(default_font)


def link_callback(sender, app_data):
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)
    print(f"Connection established {app_data[0], app_data[1]}")


def delink_callback(sender, app_data):
    dpg.delete_item(app_data)
    print("Connection terminated")


with dpg.window(label="Node Editor", tag=center_window, no_collapse=True, no_close=True, no_title_bar=True):
    with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
        with dpg.node(label="Node 1"):
            with dpg.node_attribute(label="Node A1"):
                dpg.add_input_float(label="F1", width=150)

            with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_input_float(label="F2", width=150)

        with dpg.node(label="Node 2"):
            with dpg.node_attribute(label="Node A3"):
                dpg.add_input_float(label="F3", width=200)

            with dpg.node_attribute(label="Node A4", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_input_float(label="F4", width=200)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
