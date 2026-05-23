# 🤖 GenAI Text2SQL Analytics Assistant

An advanced Generative AI-powered analytics assistant that converts natural language questions into executable SQL queries and retrieves insights from a live relational database.

Built using LangChain, Groq LLMs, SQLAlchemy, SQLite, and Streamlit.

---

# 🚀 Features

- Natural Language to SQL Conversion
- Live Database Query Execution
- AI-Powered Business Analytics
- SQL Query Transparency
- Interactive Analytics Dashboard
- CSV Export Functionality
- Automatic SQL Cleaning & Validation
- Multi-table SQL Reasoning
- Conversational Analytics Experience
- Real-time Data Insights

---

# 🧠 How It Works

The application does not train a custom AI model.

Instead, it uses a Large Language Model (LLM) to:
1. Understand the user's business question
2. Generate optimized SQL queries dynamically
3. Execute queries on a live SQLite database
4. Return analytics results and business insights

---

# 🏗️ Architecture

```text
User Query
    ↓
LLM (Groq + LangChain)
    ↓
SQL Query Generation
    ↓
SQLite Database Execution
    ↓
Analytics Results
    ↓
AI Business Summary + Visualization
```

---

# 🛠️ Tech Stack

| Category | Technology |
|---|---|
| LLM Provider | Groq |
| Framework | LangChain |
| Database | SQLite |
| ORM | SQLAlchemy |
| Frontend | Streamlit |
| Data Generation | Faker |
| Data Processing | Pandas |
| Language | Python |

---

# 📂 Project Structure

```bash
TEXT2SQL-GENAI/
│
├── agents/
│   ├── sql_agent.py
│   └── langchain_sql_agent.py
│
├── database/
│   ├── create_db.py
│   ├── seed_data.py
│   └── ecommerce.db
│
├── prompts/
│   └── sql_prompt.py
│
├── utils/
│   ├── sql_utils.py
│   └── query_engine.py
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🗄️ Database Schema

The project uses a relational e-commerce database containing:

- Customers
- Products
- Employees
- Orders
- Order Items

The database was populated with synthetic business data using Faker.

---

# 📊 Example Questions

```text
Top 5 products by revenue
```

```text
Which employee handled the most orders?
```

```text
Average order value by city
```

```text
Show revenue by product category
```

```text
Top customers by spending
```

---

# 🔥 Advanced Features Implemented

## ✅ Schema-Aware Prompting
Injected database schema directly into prompts to improve SQL accuracy.

## ✅ SQL Cleaning
Automatically removes markdown formatting and cleans generated SQL.

## ✅ Error Handling & Retry Logic
Detects invalid SQL queries and retries with correction prompts.

## ✅ LangChain SQL Agent
Implemented autonomous SQL reasoning using LangChain SQL Agent.

## ✅ AI Business Summaries
Generates human-readable business insights from query results.

## ✅ Interactive Analytics Dashboard
Built using Streamlit with:
- Data tables
- SQL visibility
- CSV export
- Charts and visualizations

---

# 📈 Sample Analytics Capabilities

- Revenue Analysis
- Customer Segmentation
- Product Performance
- Sales Trends
- Employee Performance Metrics
- Business Intelligence Reporting

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your_repo_url>
cd TEXT2SQL-GENAI
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Running The Project

## Step 1 — Create Database

```bash
python database/create_db.py
```

---

## Step 2 — Seed Database

```bash
python database/seed_data.py
```

---

## Step 3 — Run Streamlit App

```bash
streamlit run app.py
```

---

# 🌟 Key Learning Outcomes

- Generative AI Application Development
- Prompt Engineering
- LangChain Agent Workflows
- SQL Query Generation
- Database Integration with LLMs
- Conversational Analytics Systems
- Streamlit Dashboard Development
- AI-powered Business Intelligence

---

# 🎯 Future Improvements

- PostgreSQL Support
- Authentication System
- Query History
- Role-Based Access Control
- Real-time Streaming Responses
- Data Upload & Auto Analysis
- Multi-turn Conversational Memory
- Advanced Chart Visualizations

---

# 📌 Important Note

This project does not fine-tune or train an LLM.

Instead, it demonstrates:
- LLM orchestration
- schema-aware prompting
- live SQL generation
- autonomous database querying
- AI analytics workflows

which closely reflects real-world enterprise GenAI systems.

---

# 👨‍💻 Author

Mohd Faizanullah
