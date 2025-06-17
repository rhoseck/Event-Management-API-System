# Event Management API

This is a FastAPI-based application for managing events, including creating, retrieving, updating, and deleting events, with automatic speaker assignment functionality.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.9 or higher**
- **pip** (Python package manager)

## Installation

1. *Clone the Repository*
git clone https://github.com/rhoseck/Event-Management-API-System
cd eventaus

2. *Create and activate Virtual Environment*

python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

3. *Install Dependencies*

pip install -r requirements.txt
fastapi
uvicorn
pydantic


4. *Run the application*

uvicorn main:app --reload

