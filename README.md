<div align="center">

  # HuggingFace Chat Telegram Bot
  
  **A Python Telegram bot powered by HuggingFace Chat API.**

  *This is a Python Telegram bot that uses HuggingFace Chat API to generate creative text formats based on user input. It is designed to be a fun and interactive way to explore the possibilities of large language models.*

</div>

### Features

* Generate creative text formats like poems, code, scripts, musical pieces, etc.
* Stream the generation process, so you can see the text unfold in real-time.
* Reply to your messages with Bard's creative output.
* Easy to use with simple commands:
    * `/start`: Greet the bot and get started.
    * `/help`: Get information about the bot's capabilities.
* Send any text message to trigger the generation process.
* Send any image with captions to generate responses based on the image. (Multi-modal support)
* User authentication to prevent unauthorized access by setting `AUTHORIZED_USERS` in the `.env` file (optional).

### Requirements

* Python 3.10+
* Telegram Bot API token
* dotenv (for environment variables)


### Docker

#### GitHub Container Registry
Simply run the following command to run the pre-built image from GitHub Container Registry:

```shell
docker run --env-file .env ghcr.io/rabilrbl/hugging-tg-chatbot:latest
```

Update the image with:
```shell
docker pull ghcr.io/rabilrbl/hugging-tg-chatbot:latest
```

#### Build
Build the image with:
```shell
docker build -t hugging-tg-chatbot .
```
Once the image is built, you can run it with:
```shell
docker run --env-file .env hugging-tg-chatbot
```

### Installation

1. Clone this repository.
2. Install the required dependencies:
    * `pipenv install` (if using pipenv)
    * `pip install -r requirements.txt` (if not using pipenv)
3. Create a `.env` file and add the following environment variables:
    * `BOT_TOKEN`: Your Telegram Bot API token. You can get one by talking to [@BotFather](https://t.me/BotFather).
    * `HF_EMAIL`: Your HuggingFace email address. (optional)
    * `HF_PASSWORD`: Your HuggingFace password. (optional)
    * `AUTHORIZED_USERS`: A comma-separated list of Telegram usernames or user IDs that are authorized to access the bot. (optional) Example value: `shonan23,1234567890`
4. Run the bot:
    * `python main.py` (if not using pipenv)
    * `pipenv run python main.py` (if using pipenv)

### Usage

1. Start the bot by running the script.
   ```shell
   python main.py
   ```
2. Open the bot in your Telegram chat.
3. Send any text message to the bot.
4. The bot will generate creative text formats based on your input and stream the results back to you.
5. If you want to restrict public access to the bot, you can set `AUTHORIZED_USERS` in the `.env` file to a comma-separated list of Telegram user IDs. Only these users will be able to access the bot.
    Example:
    ```shell
    AUTHORIZED_USERS=shonan23,1234567890
    ```

### Bot Commands

| Command | Description |
| ------- | ----------- |
| `/start` | Greet the bot and get started. |
| `/help` | Get information about the bot's capabilities. |
| `/new` | Start a new chat session. |
| `/model` | Change the LLM model. |
| `/system_prompt` | Change the system prompt. |

### Star History

<a href="https://star-history.com/#rabilrbl/hugging-tg-chatbot&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=rabilrbl/hugging-tg-chatbot&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=rabilrbl/hugging-tg-chatbot&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=rabilrbl/hugging-tg-chatbot&type=Date" />
  </picture>
</a>

### Contributing

We welcome contributions to this project. Please feel free to fork the repository and submit pull requests.

### Disclaimer

This bot is still under development and may sometimes provide nonsensical or inappropriate responses. Use it responsibly and have fun!

### License

This is a free and open-source project released under the GNU Affero General Public License v3.0 license. See the LICENSE file for details.
