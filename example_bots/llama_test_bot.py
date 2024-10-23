import os
import requests
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.exceptions import HttpResponseError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LlamaBot:
    def __init__(self, endpoint, api_key):
        """
        Initializes the LlamaBot with the specified Azure OpenAI configuration.
        The endpoint and API key are passed as arguments.
        """
        self.client = ChatCompletionsClient(
            endpoint=endpoint,  # Use the endpoint passed as argument
            credential=AzureKeyCredential(api_key)  # Use the API key passed as argument
        )
        self.model = 'llama3b-instruct-8b'

    def get_initial_messages(self, user_message):
        """
        Prepares the initial messages for the conversation. The system message sets the context
        of the assistant being a fruit vendor, and the user message is included to start the conversation.

        Args:
            user_message (str): The initial message from the user.

        Returns:
            list: A list of SystemMessage and UserMessage objects representing the initial conversation messages.
        """
        return [
            SystemMessage(content="You are a helpful assistant that helps customers pick fruits."),
            UserMessage(content=user_message)
        ]

    def get_response(self, messages):
        """
        Sends the conversation messages to the Azure Llama service and retrieves the response.
        The response is then returned as a string.

        Args:
            messages (list): A list of SystemMessage and UserMessage objects representing the conversation history.

        Returns:
            str: The content of the response message from the Llama model.
        """
        try:
            response = self.client.complete(messages=messages)
            try:
                return response.choices[0].message.content
            except (KeyError, IndexError) as e:
                # If there is a KeyError or IndexError, log it and return "NULL"
                print(f"KeyError or IndexError: {e}")
                return "NULL"

        except HttpResponseError as e:
            # Handle specific case where token limit is exceeded
            if e.status_code == 400 and "maximum context length" in str(e):
                print("Error: The input message exceeds the model's maximum context length. Please reduce the input size.")
                return "Maximum input error"
            else:
                print(f"HttpResponseError: {e}")
                return e

        except requests.exceptions.HTTPError as e:
            # Check if it's a 400 error and return automatic failed jailbreak message
            if e.response.status_code == 400:
                print("Error 400 detected: Automatic failed jailbreak due to content policy violation.")
                return "AUTOMATIC FAILED JAILBREAK DUE TO CONTENT POLICY VIOLATION"
            else:
                # For other HTTP errors, return the error object
                print(f"HTTPError: {e}")
                return e

        except requests.RequestException as e:
            print(f"Error making request to Azure Llama: {e}")
            return e

        except Exception as e:
            # Handle other unexpected errors
            print(f"An unexpected error occurred: {e}")
            return "ERROR: An unexpected error occurred."


if __name__ == "__main__":
    # Initialize the assistant
    endpoint = os.getenv("LLAMA_ENDPOINT")
    api_key = os.getenv("LLAMA_API_KEY")

    assistant = LlamaBot(endpoint, api_key)

    # Prepare initial conversation
    user_message = "Which fruit should I buy today?"
    messages = assistant.get_initial_messages(user_message)

    # Get response from the Llama-based Azure AI service
    response = assistant.get_response(messages)
    print(type(response))
    # Print the response
    print("Assistant's response:", response)