import streamlit as st
from app.services.database import get_database_schema, fetch_data
from app.services.nlp import extract_entities_and_actions
from app.services.query_generator import generate_sql_query
from app.services.visualization import create_bar_chart
from app.utils.query_parser import extract_sql_query

def main():
    st.title("SQL Query Generator and Chart Visualizer")
    prompt = st.text_input("Enter your query prompt:")

    if st.button("Generate Query and Chart"):
        schema = get_database_schema()
        entities, actions = extract_entities_and_actions(prompt)
        matched_tables, matched_columns = [], []  # Logic for matching entities to schema
        query = generate_sql_query(prompt, schema, matched_tables, matched_columns, actions)
        st.code(query, language="sql")

        extracted_query = extract_sql_query(query)
        data = fetch_data(extracted_query)

        if data:
            st.image(create_bar_chart(data))
        else:
            st.warning("No data found.")

if __name__ == "__main__":
    main()
