import os
import re

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

from utils.query_engine import run_query


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")



llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0
)



SYSTEM_PROMPT = """
You are an expert SQL assistant.

IMPORTANT:
1. Generate ONLY SQLite SQL queries.
2. Do not explain anything.
3. Use valid SQLite syntax.
4. Return only executable SQL.

DATABASE TABLES:

customers(
    customer_id,
    name,
    email,
    city,
    signup_date
)

products(
    product_id,
    product_name,
    category,
    price,
    stock
)

employees(
    employee_id,
    employee_name,
    department
)

orders(
    order_id,
    customer_id,
    employee_id,
    order_date,
    total_amount
)

order_items(
    order_item_id,
    order_id,
    product_id,
    quantity
)
"""



def clean_sql(query):

    query = query.replace("```sql", "")
    query = query.replace("```", "")

    return query.strip()



def generate_sql(question):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=question)
    ]

    response = llm.invoke(messages)

    sql_query = clean_sql(response.content)

    return sql_query



def generate_summary(question, dataframe):

    summary_prompt = f"""
    User Question:
    {question}

    Query Result:
    {dataframe.head(10).to_string()}

    Generate a short business summary.
    """

    response = llm.invoke(summary_prompt)

    return response.content



def ask_agent(question):

    try:

        # Generate SQL
        sql_query = generate_sql(question)

        # Execute Query
        result_df = run_query(sql_query)

        # Generate Summary
        summary = generate_summary(question, result_df)

        return {
            "sql": sql_query,
            "data": result_df,
            "summary": summary
        }

    except Exception as e:

        return {
            "error": str(e)
        }