import streamlit as st
import pandas as pd

from agents.langchain_sql_agent import ask_agent



st.set_page_config(
    page_title="GenAI Text2SQL Assistant",
    page_icon="🤖",
    layout="wide"
)



st.title("🤖 GenAI Text2SQL Analytics Assistant")

st.markdown("""
Query your business database using natural language.

Examples:
- Top selling products
- Revenue by category
- Monthly sales trend
- Customer spending analysis 
""")



question = st.text_input(
    "Ask your business question:"
)



if st.button("Generate Insights"):

    if question:

        with st.spinner("Analyzing database..."):

            response = ask_agent(question)

        # Error Handling
        if "error" in response:

            st.error(response["error"])

        else:


            st.subheader("🧠 Generated SQL")

            st.code(response["sql"], language="sql")

            

            st.subheader("📊 Query Results")

            st.dataframe(
                response["data"],
                use_container_width=True
            )

           

            csv = response["data"].to_csv(index=False)

            st.download_button(
                label="⬇ Download Results CSV",
                data=csv,
                file_name="query_results.csv",
                mime="text/csv"
            )

            

            st.subheader("🤖 AI Business Summary")

            st.write(response["summary"])

            

            df = response["data"]

            if len(df.columns) >= 2:

                numeric_cols = df.select_dtypes(
                    include="number"
                ).columns

                if len(numeric_cols) > 0:

                    st.subheader("📈 Visualization")

                    chart_col = numeric_cols[0]

                    st.bar_chart(
                        df.set_index(df.columns[0])[chart_col]
                    )