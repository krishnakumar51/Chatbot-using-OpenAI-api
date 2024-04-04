# OpenAI Chatbot with Streamlit

This project demonstrates the implementation of a chatbot using the OpenAI API and Streamlit framework in Python. The chatbot utilizes the power of OpenAI's language model to generate responses based on user input, and Streamlit provides a user-friendly interface for interaction.

## Features

- **Interactive Chat Interface**: Users can engage in conversation with the chatbot by typing messages into the input field.
- **Real-time Responses**: The chatbot generates responses in real-time, providing an interactive conversational experience.
- **Customizable Prompts**: Users can customize prompts to guide the conversation and receive more relevant responses from the chatbot.
- **Easy Deployment**: The application can be easily deployed using Streamlit's built-in deployment options or any other hosting service.

## Requirements

- Python 3.x
- OpenAI API key (sign up [here](https://beta.openai.com/signup/) to get access)
- Streamlit (install via `pip install streamlit`)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/openai-chatbot.git
2. Navigate to the project directory:
   
    ```bash
    cd openai-chatbot
3. Install dependencies:

    ```bash
   pip install -q streamlit openai

4. Set up your OpenAI API key by adding it to a 'secrets.toml' file under .streamlit directory:
   
   "OPENAI_API_KEY=your-api-key-here"

5. Run the sretamlit app

   ```bash
   streamlit run app.py
6. Access the chatbot interface by opening the provided URL in your web browser.


# Contributing, License, and Acknowledgement

## Contributing

We welcome contributions from the community! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository and create your branch from `main`.
2. Make your changes and ensure they adhere to the project's coding style.
3. Test your changes thoroughly.
4. Submit a pull request describing the changes you've made and any relevant information.

## License

This project is licensed under the MIT License. You can find the full license text in the [LICENSE](LICENSE) file.

## Acknowledgement

We would like to acknowledge the following individuals and projects for their contributions to this project:

- [OpenAI](https://openai.com/) for providing the powerful language model used in this chatbot.
- [Streamlit](https://streamlit.io/) for the user-friendly framework that enables easy deployment and interaction.




