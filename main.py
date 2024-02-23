from taipy.gui import Gui, State, notify
import openai

context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "
conversation = {
    "Conversation": ["Who are you?", "Hi! I am GPT-3. How can I help you today?"]
}
current_user_message = ""

client = openai.Client(api_key="API KEY")


def request(state: State, prompt: str) -> str:
    """
    Send a prompt to the GPT-3 API and return the response.

    Args:
        - state: The current state.
        - prompt: The prompt to send to the API.

    Returns:
        The response from the API.
    """
    response = state.client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content


def send_message(state: State) -> None:
    """
        Send the user's message to the API and update the conversation.

        Args:
            - state: The current state.
        """
    # Add the user's message to the context
    state.context += f"Human: \n {state.current_user_message}\n\n AI:"
    notify(state, "info", f'Message Send')
    # Send the user's message to the API and get the response
    answer = request(state, state.context).replace("\n", "")
    # Add the response to the context for future messages
    state.context += answer

    # Update the conversation
    conv = state.conversation._dict.copy()
    conv["Conversation"] += [state.current_user_message, answer]
    state.conversation = conv
    # Clear the input field
    state.current_user_message = ""

def style_conv(state: State, idx: int, row: int) -> str:
    """
    Apply a style to the conversation table depending on the message's author.

    Args:
        - state: The current state of the app.
        - idx: The index of the message in the table.
        - row: The row of the message in the table.

    Returns:
        The style to apply to the message.
    """
    if idx is None:
        return None
    elif idx % 2 == 0:
        return "user_message"
    else:
        return "gpt_message"

page = """
<|{conversation}|table|show_all|style=style_conv|>
<|{current_user_message}|input|label=Write your message here...|on_action=send_message|class_name=fullwidth|>
"""

if __name__ == "__main__":
    Gui(page).run(title="Taipy Chat")
# :param state:
# :param prompt:
# :return:
