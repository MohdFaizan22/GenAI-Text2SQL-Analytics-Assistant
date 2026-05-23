import pandas as pd
from sqlalchemy import create_engine, text



engine = create_engine("sqlite:///database/ecommerce.db")



def run_query(sql_query):

    try:

        with engine.connect() as connection:

            result = connection.execute(text(sql_query))

            rows = result.fetchall()

            columns = result.keys()

            df = pd.DataFrame(rows, columns=columns)

            return df

    except Exception as e:

        return str(e)