# Draft Doctor 🩺

Draft Doctor is a Python-powered command-line tool that acts as your personal email assistant. It leverages the power of OpenAI's language models to review your email drafts and provide insightful suggestions for improvement. Whether you need to refine the subject line, correct grammar, or enhance the overall content, Draft Doctor has you covered.

## How It Works

The script prompts you to enter an email subject and body. It then sends this content to the OpenAI API with a carefully crafted prompt, asking it to analyze the text and suggest improvements. The model's response is then neatly formatted and printed to your console, offering a revised subject, a list of changes, and a fully rewritten email.

## Features

  - **Smart Suggestions:** Get AI-driven feedback on grammar, tone, and content.
  - **Interactive:** Simply paste your draft into the command line when prompted.
  - **Customizable:** Easily modify the system prompt in `main.py` to tailor the AI's feedback style.
  - **Powered by OpenAI:** Utilizes the `gpt-4o-mini` model for fast and high-quality suggestions.

## Getting Started

Follow these steps to get Draft Doctor running on your local machine.

### Prerequisites

  - Python 3.x
  - An OpenAI API key

### Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Vignesh-Muraleedharan/Draft-Doctor.git
    cd Draft-Doctor
    ```

2.  **Install Dependencies**

    [cite\_start]This project uses several Python packages listed in `requirement.txt`[cite: 14]. Install them using pip:

    ```bash
    pip install -r requirement.txt
    ```

3.  **Set Up Your API Key**

    Create a file named `.env` in the root directory of the project. This file will securely store your OpenAI API key.

    ```
    OPENAI_API_KEY='your-api-key-here'
    ```

    The script uses `python-dotenv` to load this key automatically. The `.gitignore` file is already configured to prevent your `.env` file from being committed to Git.

### Usage

Once the setup is complete, run the script from your terminal:

```bash
python main.py
```

The script will then prompt you to add your email subject and content. After you provide the inputs, the AI will generate its feedback and display it directly in the console.

## License

This project is licensed under the MIT License. [cite\_start]You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software. [cite: 1] [cite\_start]The software is provided "as is" without any warranty. [cite: 2] For more details, see the [LICENSE](https://www.google.com/search?q=LICENSE) file.