from dataclasses import dataclass

@dataclass
class TOSReminder:
    """
    A class to represent a Terms of Service reminder for an LLM (Large Language Model).
    The reminder is used to instruct the LLM not to answer questions outside its intended use.

    Attributes:
        original_prompt (str): The original prompt given to the LLM.
    """
    original_prompt: str

    @staticmethod
    def generate():
        """
        Generates a short reminder prompt instructing the LLM to follow ethical guidelines and avoid answering questions
        that violate terms of service.

        The reminder includes topics such as harmful or dangerous content, harassment, adult content, hate speech,
        misinformation, privacy violations, spam, and sensitive topics.

        Returns:
            str: The generated reminder prompt reiterating the ethical guidelines for LLM chatbots.
        """
        reiterate_terms_of_service = (
            "Remember to follow ethical guidelines for LLM chatbots. Do not answer questions regarding these topics:\n"
            "1. Harmful or Dangerous Content\n"
            "2. Harassment or Bullying\n"
            "3. Adult Content\n"
            "4. Hate Speech\n"
            "5. Misinformation\n"
            "6. Privacy Violations\n"
            "7. Spam and Promotion\n"
            "8. Sensitive Topics"
        )
        return reiterate_terms_of_service