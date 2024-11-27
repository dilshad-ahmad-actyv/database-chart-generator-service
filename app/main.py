import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from app.services.database import get_database_schema, fetch_data
from app.services.nlp import extract_entities_and_actions
from app.services.query_generator import generate_sql_query
from app.services.visualization import create_bar_chart
from app.utils.query_parser import extract_sql_query

def main():
    st.title("SQL Query Generator and Chart Visualizer")
    
    # User prompt input
    prompt = st.text_input("Enter your query prompt:", "")
    
    if st.button("Generate Query and Chart"):
        st.subheader("Generated Query")
        
        # Process prompt
        # schema = get_database_schema()
        # entities_actions = extract_entities_and_actions(prompt, schema)
        # print('entities_actionsentities_actions================>', entities_actions)
        # Generate SQL query
        # query = generate_sql_query(prompt, schema, entities_actions)
        query = generate_sql_query(prompt)
        print('=====================query=======================>', query)
        st.code(query, language="sql")
        extracted_query = extract_sql_query(query)
        # Fetch and display data
        data = fetch_data(extracted_query)

        st.text(f"Response: \n\n{data}")

        if data:
            st.subheader("Generated Chart")
            chart_buffer = create_bar_chart(data)
            st.image(chart_buffer)
        else:
            st.warning("No data found for the generated query.")

if __name__ == "__main__":
    main()