# Expense Tracking System

A web-based Expense Tracking System built with Streamlit (frontend), FastAPI (backend), and Pytest (testing).
Easily track, update, and analyze daily expenses with visual insights.

# Features

- Add / Update Expenses: Enter date, category, amount, and notes.

- Analytics: View totals and category-wise percentage breakdown.

- Visualization: Interactive bar charts for better insights.

- Validation: Ensures correct inputs (no negative values).

- Testing: Backend logic tested with Pytest for reliability.

# Tech Stack

- Layer	Technology

- Frontend	Streamlit

- Backend	FastAPI

- Database	MySQL 

- Data	Pandas

- Testing	Pytest

# Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/AsokTamang/expense-tracker
cd expense-tracker

2️⃣ Create virtual environment & install dependencies
python -m venv .venv

windows: 
.venv\Scripts\activate

macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt

3️⃣ Run Backend
uvicorn backend/src/server:app --reload


FastAPI server runs at http://127.0.0.1:8000/

4️⃣ Run Frontend
streamlit run frontend/app.py

The app opens in your browser automatically.
Connects to the FastAPI backend for data retrieval and analytics.