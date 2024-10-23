from openai import AzureOpenAI
import os


class GPT35Bot:
    def __init__(self, endpoint, api_key, api_version, model):
        """
        Initializes the FruitVendorAssistant with the specified Azure OpenAI configuration.

        Args:
            endpoint (str): The endpoint URL for the Azure OpenAI service.
            api_key (str): The API key for authenticating with the Azure OpenAI service.
            api_version (str): The version of the Azure OpenAI API to use.
            model (str): The specific model to use for generating responses (e.g., "gpt35").
        """
        self.client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version
        )
        self.model = model

    def get_initial_messages(self, user_message):
        """
        Prepares the initial messages for the conversation. The system message sets the context
        of the assistant being a fruit vendor, and the user message is included to start the conversation.

        Args:
            user_message (str): The initial message from the user.

        Returns:
            list: A list of dictionaries representing the initial conversation messages.
        """
        return [
            {"role": "system",
             "content": "You are a fruit vendor assistant designed to help a customer pick a fruit to buy."},
            {"role": "user", "content": user_message},
        ]

    def get_response(self, messages):
        """
        Sends the conversation messages to the Azure OpenAI service and retrieves the response.
        The response is then returned as a string.

        Args:
            messages (list): A list of message dictionaries representing the conversation history.

        Returns:
            str: The content of the response message from the chatbot.
        """
        try:
            # Sending the request to the Azure OpenAI service
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )

            # Ensure we are accessing the message content properly
            if response.choices and len(response.choices) > 0:
                # Access the message content correctly
                if response.choices[0].message.content is None:
                    return "NULL"
                return response.choices[0].message.content

            print("Unexpected response format: no choices or content found")
            return "NULL"

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return e


if __name__ == "__main__":
    assistant = GPT35Bot(
        endpoint="https://htwgpt.openai.azure.com/",
        api_key="5e34fe89635c4b3688d9a3942047297a",
        api_version="2024-02-01",
        model="gpt35"
    )

    # Create the initial message payload
    messages = assistant.get_initial_messages("Hello")

    # Get the response and print it
    response = assistant.get_response(messages)
    if response:
        print(response)