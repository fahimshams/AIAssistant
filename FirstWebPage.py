from taipy.gui import Gui, notify


text = "Original"

page = """
# Getting started with Taipy GUI
    
My text: <|{text}|>

<|{text}|input|>

<|Run local|button|on_action=on_action_button|>

"""


def on_action_button(state):
    notify(state, 'info', f'The text is { state.text }' )
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

Gui(page).run(use_reloader=True)