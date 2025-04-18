# ANNNI Chat Assistant

A streamlined Streamlit chat interface that connects to an LLM through n8n workflows.

## Overview

This application provides a simple yet powerful chat interface for interacting with a language model through n8n webhooks. The app maintains a session for each user and preserves chat history within the session.

## Features

- Clean, minimalist chat interface
- Session management with unique IDs
- Persistent chat history within a session
- Real-time responses from the AI assistant
- Option to start a new conversation session

## Prerequisites

- Python 3.7+
- Streamlit
- Access to n8n workflow with a webhook endpoint

## Installation

1. Clone this repository or download the app.py file
2. Install the required dependencies:

```bash
pip install streamlit requests
```

## Configuration

Update the following variables in the app.py file:

```python
# n8n Webhook configuration
WEBHOOK_URL = "https://annnni.app.n8n.cloud/webhook/7df913c7-d1ba-42a3-bf95-6f6a769e866d/chat"
API_TOKEN = "your-bearer-token-here"  # Replace with your actual token
```

## Running the Application

Start the application with:

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501` by default.

## Usage

1. Type your message in the chat input field at the bottom of the screen
2. The AI assistant will respond with the information processed through the n8n workflow
3. Chat history is preserved within your current session
4. To start a new conversation, click the "Start New Session" button in the sidebar

## Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Log in to [Streamlit Cloud](https://share.streamlit.io/)
3. Deploy your app directly from your GitHub repository

### Other Deployment Options

- Can be deployed on any platform that supports Python applications
- Common options include Heroku, AWS, GCP, or Azure

## Customization

- Change the title and welcome message to fit your brand
- Update the webhook URL to point to your n8n workflow
- Modify the UI styling using Streamlit's theming options

## Security Note

For production deployment, replace the placeholder bearer token with a secure authentication method.
