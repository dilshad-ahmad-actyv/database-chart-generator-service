import openai
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_sql_query(prompt, schema, matched_tables, matched_columns, actions):
    schema_description = "\n".join(
        f"Table: {table}, Columns: {', '.join(columns)}"
        for table, columns in schema.items()
    )
    system_message = (
        "You are an assistant generating SQL queries. "
        f"Schema:\n{schema_description}\n"
        "Use correct SQL Server syntax."
    )
    user_message = (
        f"Prompt: {prompt}\n"
        f"Actions: {', '.join(actions)}\n"
        f"Tables: {', '.join(matched_tables)}\n"
        f"Columns: {', '.join(f'{table}.{column}' for table, column in matched_columns)}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ]
    )
    return response['choices'][0]['message']['content'].strip()
