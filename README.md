# Sapphire Intelligence 💎

Sapphire Intelligence is the brains behind [Sapphire](https://github.com/Caramel-Labs/CaramelLabs_Sapphire), the digital nomad's guide to Sri Lanka. 🇱🇰

This project was developed to demonstrate the integration of multiple AI-related services to work in harmony and provide reasoning capabilities to software applications.

Sapphire Intelligence features the use of LLMs and chat models for reasoning (context-aware [agent with tooling](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/tool_calling/)) and content generation (intelligent experience generation for tourists) on LangChain infrastructure, as well as providing Sapphire with support for verifying the biometric data and content of its users' passports.

## Project Structure 🌳

```sh
.
├── chat                          # Handles chat-related functionalities
│   ├── agents.py                 # Defines various agent classes for chat handling
│   ├── contextualizers.py        # Manages context within chat interactions
│   ├── __init__.py               # Initializes the chat module
│   ├── payloads.py               # Structures for data payloads in chat requests
│   ├── prompts.py                # Contains prompt templates for chat responses
│   └── routes.py                 # Sets up chat-specific API routes
│
├── database                      # Contains database configurations
│   ├── config.py                 # Database connection and configuration settings
│   └── __init__.py               # Initializes the database module
│
├── experience                    # Handles user experience modules
│   ├── chains.py                 # Defines chains of actions or workflows
│   ├── data_models.py            # Defines data models for experience-related entities
│   ├── __init__.py               # Initializes the experience module
│   ├── output_parsers.py         # Parses outputs from experience workflows
│   ├── payloads.py               # Structures for data payloads in experiences
│   ├── prompts.py                # Contains prompt templates for experiences
│   └── routes.py                 # Sets up experience-specific API routes
│
├── providers                     # Defines LLM service providers
│   ├── chat_models.py            # Manages chat model integrations
│   ├── __init__.py               # Initializes the providers module
│   └── llms.py                   # Manages LLM integrations
│
├── schemas                       # Contains data schema definitions
│   ├── experiences.py            # Schemas for experience-related data
│   ├── hotels.py                 # Schemas for hotel-related data
│   ├── __init__.py               # Initializes the schemas module
│   └── messages.py               # Schemas for message data structures
│
├── visaguard                     # Handles visa-related data processing
│   ├── biometrics.py             # Processes biometric data
│   ├── chains.py                 # Defines visa-related workflows and chains
│   ├── data_models.py            # Data models specific to visa processing
│   ├── __init__.py               # Initializes the visaguard module
│   ├── output_parsers.py         # Parses outputs from visa workflows
│   ├── payloads.py               # Structures for data payloads in visa workflows
│   ├── prompts.py                # Prompt templates for visa processing
│   └── routes.py                 # Sets up visa-related API routes
│
├── Dockerfile                    # Docker configuration for containerizing the app
├── LICENSE                       # License information for the project
├── README.md                     # Project overview and usage instructions
├── main.py                       # Entry point for running the application
└── requirements.txt              # Lists dependencies required to run the application

```

## Setup ⚙️

To setup Sapphire Intelligence, clone this repository to a desired location on your system:

```shell
git clone https://github.com/ravi-aratchige/sapphire-intelligence.git
```

Navigate into the cloned directory:

```shell
cd sapphire-intelligence
```

Create a `.env` file within the root folder with the following content:

```shell
GROQ_API_KEY = "your-api-key"
COHERE_API_KEY = "your-api-key"
MONGO_URI_STRING = "your-mongo-uri"
```

To connect to LangSmith for observability, add the following content too:

```shell
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="your-api-key"
LANGCHAIN_PROJECT="default"
```

Install the required packages:

```shell
pip install -r requirements.txt
```

Launch the FastAPI server:

```shell
fastapi dev main.py
```

---

Built with ❤️ by [Ravindu Aratchige](ravi-aratchige.github.io).