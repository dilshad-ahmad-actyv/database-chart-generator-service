import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import openai
# from config.settings import OPENAI_API_KEY
# import requests
# import json
# openai.api_key = OPENAI_API_KEY

# # def generate_sql_query(prompt, schema, entities_actions):
# def generate_sql_query(prompt, schema):
#     """
#     Generates a SQL query dynamically using OpenAI API based on the prompt, matched tables, columns, and actions.
#     """
#     # print('matched_tables: ', matched_tables, 'matched_columns: ', matched_columns)
#     # if not matched_tables and not matched_columns:
#     #     return "No valid query could be generated based on the prompt."


#     # schema_description = "\n".join(
#     #     f"Table: {table}, Columns: {', '.join(columns)}"
#     #     for table, columns in schema.items()
#     # )

#     def load_schema(file_path):
#         try:
#             with open(file_path, 'r') as file:
#                 schema = json.load(file)  # This parses the JSON into Python objects (list of dicts)
#                 # print("Loaded schema:", schema)  # Debugging: Check what is loaded
#                 return schema
#         except Exception as e:
#             print(f"Error loading schema: {e}")
#             return None

#     file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'schema.json')
#     schema = load_schema(file_path)
#     if not schema:
#         return "Error: Could not load the schema."

#     # Convert schema into a string description for OpenAI (this can be customized based on your needs)
#     schema_description = ""

#     for table in schema:
#         # Extract table name and columns
#         table_name = table['table']
#         columns = table['columns']
        
#         # Add basic table and columns information
#         schema_description += f"Table: {table_name}, Columns: {', '.join(columns)}\n"

#         # Check if 'data' is present and process the first row for column details
#         if 'data' in table and table['data']:
#             sample_data = table['data'][0]  # Use the first row of data for example ranges/values
            
#             # Extract column-specific details
#             for column, value in sample_data.items():
#                 # Handle null or non-informative values
#                 if value is None:
#                     value_description = "NULL"
#                 elif isinstance(value, bool):
#                     value_description = f"Boolean ({value})"
#                 elif isinstance(value, (int, float)):
#                     value_description = f"Numeric (e.g., {value})"
#                 elif isinstance(value, str) and len(value) > 20:  # Trim long strings
#                     value_description = f"Text (e.g., '{value[:20]}...')"
#                 elif isinstance(value, str):
#                     value_description = f"Text (e.g., '{value}')"
#                 else:
#                     value_description = f"Example Value: {value}"
                
#                 # Append the description for this column
#                 schema_description += f"    Column '{column}': {value_description}\n"

#     # Print schema description for debugging
#     print("Schema Description:\n", schema_description)


#     system_message = (
#     "You are a highly skilled SQL assistant responsible for generating accurate and efficient SQL queries "
#     "based on the user's prompt and the provided database schema. Your goal is to:\n"
#     "1. Analyze the user's request.\n"
#     "2. Use the schema to identify relevant tables and columns.\n"
#     "3. Extract any value-based filters (e.g., conditions for WHERE or HAVING clauses) from the user's prompt.\n"
#     "4. Handle special data formats, such as ranges in columns, appropriately:\n"
#     "- For columns with range-like values (e.g., '10-2', '40-23'), split the values into two numbers.\n"
#     "- Compute derived metrics like averages of the range (e.g., for '10-2', use (10+2)/2).\n"
#     "5. Generate a syntactically correct and valid SQL query for Microsoft SQL Server.\n\n"
#     "Here is the database schema which contains table, columns and a sample data of it:\n"
#     f"{schema_description}\n\n"
#     "Guidelines:\n"
#     "The schema description contains table, columns and a sample data of it."
#     "- Ensure to understand and consider the data types and value ranges (e.g., AHT column contains data in specific ranges (10-30)) in the provided schema before generating the query."
#     "- Handle special data/value formats, such as ranges in columns, appropriately:\n"
#     "   - For columns with range-like values (e.g., '10-2', '40-23'), split the values into two numbers.\n"
#     "   - Compute derived metrics like averages of the range (e.g., for '10-2', use (10+2)/2).\n"
#     "- Ensure table and column names match exactly with the schema, respecting case sensitivity.\n"
#     "- Include (Only inclue it if it's required based on the user's 'prompt') WHERE, HAVING, or JOIN conditions when value-based filters are explicitly or implicitly requested.\n"
#     "- Use correct MS SQL Server syntax (e.g., use 'TOP' instead of 'LIMIT').\n"
#     "- End the query with a semicolon.\n"
#     "- If the request cannot be fulfilled with the given schema, respond with: 'The schema does not support this request.'\n"
#     )

#     user_message = (
#     f"User Prompt: {prompt}\n"
#     "Based on the database schema provided, generate a valid SQL query that:\n"
#     "- Matches the user's request.\n"
#     "- Use the exact table and column names as defined in the schema.\n"
#     "- Refer to the sample data provided in the schema for additional context.\n"
#     "- Include relevant conditions or filters (e.g., WHERE clauses) from the user's intent, but only if they are necessary based on the provided prompt."
#     "- Ensures relationships between tables are respected, but only if joins are necessary.\n"
#     "- Uses Microsoft SQL Server syntax (e.g., 'TOP' for limiting results instead of 'LIMIT').\n"
#     "If no valid query can be generated, respond with 'The schema does not support this request.'"
#     )

#     # user_message = (
#     # f"User Prompt: {prompt}\n"
#     # f"Entities and Actions Detected:\n{entities_actions}\n\n"
#     # "Based on the database schema provided, generate a valid SQL query that:\n"
#     # "- Matches the user's request.\n"
#     # "- Uses the exact table and column names from the schema.\n"
#     # "- Include relevant conditions or filters (e.g., WHERE clauses) from the user's intent, but only if they are necessary based on the provided prompt."
#     # "- Ensures relationships between tables are respected if joins are necessary.\n"
#     # "- Uses Microsoft SQL Server syntax (e.g., 'TOP' for limiting results instead of 'LIMIT').\n"
#     # "If no valid query can be generated, respond with 'The schema does not support this request.'"
#     # )

#     # OpenAI API call
#     openai.api_key = OPENAI_API_KEY
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": system_message},
#             {"role": "user", "content": user_message},
#         ],
#     )

#     # Extract and return the generated query
#     query = response['choices'][0]['message']['content']
#     query = query.replace("```sql", "").replace("```", "").strip()
#     return query


import sys
import os
import openai
import json
import pyodbc  # For MS SQL validation
from config.settings import OPENAI_API_KEY
import requests

openai.api_key = OPENAI_API_KEY

def load_schema(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading schema: {e}")
        return None

def validate_sql_query(query):
    """
    Validate SQL query against the schema. If not valid, return False.
    Placeholder for actual validation logic (could use `pyodbc` or manual checks).
    """
    try:
        conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DILSHAD0194;'
        'DATABASE=PD11.2.411;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
        )
        # conn = pyodbc.connect('DRIVER={SQL Server};SERVER=your_server;DATABASE=your_db;UID=user;PWD=password')
        cursor = conn.cursor()
        cursor.execute("EXPLAIN " + query)  # Example, adjust depending on your DBMS
        return True, ""
    except pyodbc.Error as e:
        # Capture the error dynamically
        error_message = f"SQL Error: {str(e)}"
        print(f"Validation Error: {error_message}")
        return False, error_message
    finally:
        conn.close()

def generate_sql_query(prompt):
    """
    Generates a SQL query dynamically using OpenAI API based on the prompt and the provided schema.
    Includes retry mechanism for validation.
    """

    # Load schema once
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'schema.json')
    schema = load_schema(file_path)

    if not schema:
        return "Error: Could not load the schema."

    # Convert schema into a string description for OpenAI (this can be customized based on your needs)
    schema_description = ''
    for table in schema:
        # Extract table name and columns
        table_name = table['table']
        columns = table['columns']
        
        # Add basic table and columns information
        schema_description += f"Table: {table_name}, Columns: {', '.join(columns)}\n"

        # Check if 'data' is present and process the first row for column details
        if 'data' in table and table['data']:
            sample_data = table['data'][0]  # Use the first row of data for example ranges/values
            
            # Extract column-specific details
            for column, value in sample_data.items():
                # Handle null or non-informative values
                if value is None:
                    value_description = "NULL"
                elif isinstance(value, bool):
                    value_description = f"(e.g.,: {value})"
                elif isinstance(value, (int, float)):
                    value_description = f"(e.g.,: {value})"
                elif isinstance(value, str) and len(value) > 10:  # Trim long strings
                    value_description = f"(e.g.,: '{value[:10]}')"
                else:
                    value_description = f"e.g.,: {value[:10]}"
                
                # Append the description for this column
                schema_description += f"    Column '{column}': {value_description}\n"


    # print('schema_description====>', schema_description)
    # Optimized system message
    system_message = (
        "You are a highly skilled SQL assistant. Your task is to generate valid SQL queries for Microsoft SQL Server. "
        "You will use the provided schema to identify relevant tables and columns and generate a syntactically correct query."
        "Follow these guidelines:\n"
        "1. Use the schema to identify tables and columns.\n"
        "2. Ensure to match the exact table and column names.\n"
        "3. Handle special data formats and conditions, such as ranges and derived metrics.\n"
        "4. Use SQL Server syntax (e.g., 'TOP' instead of 'LIMIT').\n"
        "5. If the request cannot be fulfilled, respond with 'The schema does not support this request.'\n"
        f"Here is the provided schema:\n{schema_description}\n"
    )

    # Optimized user message
    user_message = (
        f"User Prompt: {prompt}\n"
        "Generate a SQL query based on the provided schema. The schema includes table names, column names, and sample data.\n"
        "- Use the exact table and column names from the schema.\n"
        "- Refer to the sample data for additional context, such as value ranges.\n"
        "- Include conditions like WHERE, HAVING, JOIN if required by the prompt.\n"
        "- Ensure the query is syntactically correct for MS SQL Server.\n"
        "- If no valid query can be generated, respond with 'The schema does not support this request.'"
    )

    # OpenAI API call to generate SQL query
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": user_message}],
    )

    query = response['choices'][0]['message']['content'].strip()
    query = query.replace("```sql", "").replace("```", "").strip()
    print('============query=============>', query)
    # Validate query before returning
    retry_count = 0
    error_message = ""
    while retry_count < 2:
        is_valid, error_message = validate_sql_query(query)
        if is_valid:
            return query
        retry_count += 1
        print(f"Validation failed (Attempt {retry_count}). Error: {error_message}")
        print(f"Validation failed, retrying... (Attempt {retry_count})")
        # Retry by regenerating the query
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": system_message}, {"role": "user", "content":  f"{user_message}\n\nError: {error_message}"}],
        )
        query = response['choices'][0]['message']['content'].strip()
        query = query.replace("```sql", "").replace("```", "").strip()

    return query if validate_sql_query(query) else "Error: Generated query is invalid after 2 retries."



