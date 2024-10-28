# Sapphire Intelligence

This is the AI application for Sapphire.

## Project Structure

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
├── providers                     # Defines service providers (e.g., chat models)
│   ├── chat_models.py            # Manages various chat model integrations
│   ├── __init__.py               # Initializes the providers module
│   └── llms.py                   # Manages large language model integrations
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