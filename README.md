# Notes Application

A simple notes application built with React (frontend) and Flask (backend) that allows users to create, view, and delete notes.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Node.js and npm
- Git (optional)

## Setup and Installation

### Backend Setup

1. Create and activate a Python virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Frontend Setup

1. Install Node dependencies:

```bash
cd frontend-app
npm install
```

## Running the Application

### 1. Start the Backend Server

In one terminal window:

```bash
# Make sure your virtual environment is activated
python app.py
```

The Flask backend will run on http://localhost:5001

### 2. Start the Frontend Development Server

In another terminal window:

```bash
cd frontend
npm run dev
```

The React frontend will run on http://localhost:5173

## API Endpoints

The backend provides the following API endpoints:

- `GET /api/notes` - Retrieve all notes
- `POST /api/notes` - Create a new note
  - Required fields: `title`, `content`
- `DELETE /api/notes/<note_id>` - Delete a specific note
