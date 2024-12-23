
# Discord Bot with Meme and Greeting Commands

## Description
This Discord bot allows users to fetch random memes and responds to greetings with fun messages. The bot is written in Python using the `discord.py` library and integrates with a meme API for meme fetching.

## Features
- **Fetch Memes**: Type `$meme` to get a random meme.
- **Greeting Response**: The bot responds to messages containing `hello` or `Hello` with friendly replies.
- **Error Handling**: Handles API errors gracefully to ensure the bot remains operational.

---

## Setup Instructions

### Prerequisites
1. Install [Python 3.8+](https://www.python.org/downloads/).
2. Create a Discord bot and get the token:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application.
   - Add a bot to the application.
   - Copy the bot token.
3. Install the required Python libraries:
   ```bash
   pip install discord.py requests
   ```

### Setting Up the Bot
1. Clone this repository or copy the bot's code.
2. Create a `.env` file in the project directory and add your Discord bot token:
   ```env
   DISCORD_TOKEN=your-bot-token-here
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```

---

## How to Use

### Commands
- `$meme`: Fetches and sends a random meme from the internet.
- `hello` (case-insensitive): Responds with `Hello World!`.
- `Hello`: Responds with `Bye Bye!`.

### Example
1. User: `$meme`
   - Bot: *Sends a random meme URL.*
2. User: `hello`
   - Bot: `Hello World!`
3. User: `Hello`
   - Bot: `Bye Bye!`

---

## Code Highlights
- **Error Handling**: Ensures the bot remains stable even if the meme API fails.
- **Environment Variables**: Uses `.env` for securely storing the bot token.
- **Intents**: Properly configures `Intents` for message content access.

---

## Contributing
Feel free to fork this repository and submit a pull request if you have suggestions or additional features to add.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
