from jailbreaks import (
    PayloadSplittingPrompt,
    BasicJailbreak,
    BasicPromptLeak,
    GodModePrompt,
    GPT4OPlinyPrompt,
    DeveloperModePrompt,
    VirtualizationPrompt,
    PythonProgramExecutionPrompt,
    MultiOnJailbreakPrompt,
    MoralizingRantPrompt,
    DANPrompt,
    EvilBotPrompt,
    D1r7ymu33yPrompt,
    DrAIPrompt,
    CompDocPrompt
)

class PromptClassMapper:
    @staticmethod
    def get_prompt_class_mapping():
        """
        Returns a dictionary mapping prompt class names to their respective prompt classes.
        """
        return {
            "PayloadSplittingPrompt": PayloadSplittingPrompt,
            "BasicJailbreak": BasicJailbreak,
            "BasicPromptLeak": BasicPromptLeak,
            "GodModePrompt": GodModePrompt,
            "GPT4OPlinyPrompt": GPT4OPlinyPrompt,
            "DeveloperModePrompt": DeveloperModePrompt,
            "VirtualizationPrompt": VirtualizationPrompt,
            "PythonProgramExecutionPrompt": PythonProgramExecutionPrompt,
            "MultiOnJailbreakPrompt": MultiOnJailbreakPrompt,
            "MoralizingRantPrompt": MoralizingRantPrompt,
            "DANPrompt": DANPrompt,
            "EvilBotPrompt": EvilBotPrompt,
            "D1r7ymu33yPrompt": D1r7ymu33yPrompt,
            "DrAIPrompt": DrAIPrompt,
            "CompDocPrompt": CompDocPrompt
        }
