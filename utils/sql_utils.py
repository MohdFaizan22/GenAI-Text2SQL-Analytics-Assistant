import re

def clean_sql_query(query):

    # Remove markdown SQL formatting
    query = query.replace("```sql", "")
    query = query.replace("```", "")

    # Remove extra spaces/newlines
    query = query.strip()

    return query