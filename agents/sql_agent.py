import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

from sqlalchemy import create_engine, text
import pandas as pd

from prompts.sql_prompt import SYSTEM_PROMPT
from utils.sql_utils import clean_sql_query



load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")



llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
)



engine = create_engine("sqlite:///database/ecommerce.db")



def generate_sql(user_question):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_question)
    ]

    response = llm.invoke(messages)

    sql_query = response.content.strip()

    cleaned_query = clean_sql_query(sql_query)

    return cleaned_query



def execute_sql(sql_query):

    try:
        with engine.connect() as connection:

            result = connection.execute(text(sql_query))

            rows = result.fetchall()

            columns = result.keys()

            df = pd.DataFrame(rows, columns=columns)

            return df

    except Exception as e:

        return f"SQL ERROR: {str(e)}"



if __name__ == "__main__":

    question = input("Ask your question: ")

   
    sql_query = generate_sql(question)

    print("\nGenerated SQL:\n")
    print(sql_query)

    print("\nExecuting Query...\n")


    result = execute_sql(sql_query)

    if isinstance(result, str) and "SQL ERROR" in result:

        print("\nRetrying with error feedback...\n")

        retry_prompt = f"""
        The following SQL query failed:

        {sql_query}

        Error:
        {result}

        Generate corrected SQLite SQL only.
        """

        corrected_sql = generate_sql(retry_prompt)

        print("\nCorrected SQL:\n")
        print(corrected_sql)

        result = execute_sql(corrected_sql)

    print("\nFinal Result:\n")
    print(result)
