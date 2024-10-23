# Nortal Security Suite

## Overview
The Nortal Security Suite is a comprehensive framework designed to evaluate the robustness of Large Language Models (LLMs) against adversarial attacks, specifically focusing on non-iterative jailbreak prompts. The suite systematically tests LLMs by applying different strategies to bypass safety mechanisms, helping to identify vulnerabilities and enhance AI security. This framework was developed as part of a thesis exploring the efficacy of privilege escalation, attention shifting, and other techniques in bypassing model safeguards.

## Features
- **Adversarial Prompt Testing**: Supports various categories of jailbreak prompts, including privilege escalation, role-playing, and attention shifting.
- **Automated Evaluation**: Utilizes scripts to test LLMs in a non-iterative manner, analyzing how models respond to single, well-crafted prompts.
- **Comprehensive Logging**: Tracks test results, including success rates and specific responses, to help analyze the effectiveness of different prompts.
- **Customizable Testing Environment**: Flexible components that allow users to add new prompts, modify existing evaluations, and test against different LLMs.

## Project Structure
```
├── example_bots
│   ├── crplus_test_bot.py
│   ├── gpt35_test_bot.py
│   ├── llama_test_bot.py
│   └── test_bot.py
├── prompthack_suite
│   ├── logs
│   ├── additional_modes.py
│   ├── jailbreaks.py
│   ├── judge.py
│   ├── judge_llama.py
│   ├── list_dataclass_names.py
│   ├── llm_test_suite.py
│   ├── malicious_intents.py
│   ├── prompt_class_mapper.py
│   ├── requirements.txt
│   └── suite_logging.py
└── README.md
```

### Explanation of Key Components

#### example_bots/
Contains test bot scripts for various LLM models. These can be used as templates or starting points to evaluate how different models respond to adversarial prompts.

- `crplus_test_bot.py`: Example test bot for a specific LLM model (CR Plus)
- `gpt35_test_bot.py`: Example test bot for GPT-3.5 model
- `llama_test_bot.py`: Example test bot for the Llama model
- `test_bot.py`: General test bot template that can be adapted for other models

#### prompthack_suite/
Core suite containing the main testing scripts and utilities.

- `logs/`: Directory for storing log files generated during testing
- `additional_modes.py`: Adds modifiers to prompts, testing the effectiveness of variations
- `jailbreaks.py`: Contains predefined sets of adversarial prompts
- `judge.py`, `judge_llama.py`: Evaluation tools for assessing whether prompts successfully bypass model safeguards
- `list_dataclass_names.py`: Utility for managing and selecting data classes dynamically
- `llm_test_suite.py`: Main script for executing tests against LLMs
- `malicious_intents.py`: Stores prompts associated with specific malicious intents
- `prompt_class_mapper.py`: Maps prompts to categories, aiding in the classification of attack types
- `requirements.txt`: Lists all dependencies required to run the suite
- `suite_logging.py`: Manages the logging of test results

## Setup Instructions

### Prerequisites
Make sure you have Python installed (version 3.8 or higher is recommended). Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes all necessary packages, such as:
- Machine Learning frameworks: torch, transformers, cohere
- Utility packages: pandas, numpy, requests

### Environment Setup
If your tests require specific configurations (e.g., API keys for LLM services), ensure that these are set up as environment variables or included in a `.env` file.

## Usage

### Running the Test Suite
The main script to execute tests is `llm_test_suite.py`. It integrates adversarial prompts from `jailbreaks.py` and `malicious_intents.py`, applies them to selected LLMs, and uses the evaluation tools to analyze responses.

```bash
python llm_test_suite.py
```

### Running Example Test Bots
Example test bots for different models can be found in the `example_bots` directory. Use these as templates to test specific models:

```bash
python example_bots/gpt35_test_bot.py
```

### Adding Custom Prompts
You can add new prompts or modify existing ones by editing the files:
- `jailbreaks.py`: Define new sets of adversarial prompts
- `malicious_intents.py`: Add specific malicious intent scenarios for testing

### Utilizing Additional Modes
The `additional_modes.py` script allows you to append modifiers (e.g., terms of service reminders) to prompts, testing how variations might impact the success rate of jailbreaks.

### Logging and Results
The suite automatically logs all test results using `suite_logging.py`, storing detailed information about each attempt, including:
- Prompt used
- Model response
- Success or failure indication

## Customization

### Integrating New LLM Models
To test the suite against a different LLM, add a new evaluation script similar to `judge.py` or `judge_llama.py`. Ensure that your custom evaluator follows the interface required by the test suite for seamless integration.

### Creating New Prompt Categories
The `prompt_class_mapper.py` script is used to map prompts to their appropriate categories (e.g., privilege escalation, attention shifting). Update this script to include new categories as needed.

## References
This framework was developed based on the findings in my thesis, available in the repo as well. The thesis provides a detailed exploration of the vulnerabilities in LLMs and the methods used to exploit these weaknesses.

For a comprehensive understanding of the system and its methodology, please refer to the thesis.
