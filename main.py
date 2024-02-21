import taipy as tp
from taipy import Config, Core, Gui


def build_message(name: str):
    return f"Hello {name}!"


input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

input_name = "Taipy"
message = None

def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()

page = """
Enter your name: <|{input_name}|input|>

<|submit|button|on_action=submit_scenario|>

Message: <|{message}|text|>
"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Core().run()

    scenario = tp.create_scenario(scenario_cfg)
    Gui(page).run()
    # hello_scenario = tp.create_scenario(scenario_cfg)
    # hello_scenario.input_name.write("Taipy")
    # hello_scenario.submit()
    # print(hello_scenario.message.read())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
