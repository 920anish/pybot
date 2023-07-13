# Discord Bot

This is a Discord bot that can perform various tasks, including greeting users, echoing text, evaluating mathematical expressions, and providing weather information.

## Setup

To set up the Discord bot locally, follow these steps:

### Prerequisites

- Python 3.7 or higher installed on your machine
- Your discord bot [token](https://discord.com/developers/applications/)
- OpenWeather API key (get it from [OpenWeatherMap](https://openweathermap.org/))

### Installation

Use the package manager pip to install the required dependencies.

```
pip install -r requirements.txt
```

### Configuration

Create a .env file in the root of the project directory and add the following environment variables:

```
DISCORD_BOT_TOKEN=<your-discord-bot-token>
OPENWEATHER_API_KEY=<your-openweather-api-key>
```

## Usage

Start the bot:

```
python main.py
```

### Bot Commands

The bot supports the following commands:

`!hello` : Greets you with your username.\
`!echo [text]`: Repeats the provided text.\
`!calc [expression]`: Evaluates a mathematical expression.\
`!weather [city]`: Shows the current weather for the specified city.\
`!help`: Shows the available commands.

## Contributing

Contributions are welcome and encouraged!
