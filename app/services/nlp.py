import openai
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_entities_and_actions(prompt, schema):
    # Format the schema description for OpenAI
    schema_description = "\n".join(
        f"Table: {table}, Columns: {', '.join(columns)}"
        for table, columns in schema.items()
    )

    system_message = (
    "You are a highly intelligent and schema-aware assistant. Your task is to extract entities (tables and their respective columns) "
    "and actions (e.g., SELECT, INSERT, UPDATE, DELETE) from complex user prompts by analyzing the provided database schema. "
    "You must ensure that:\n"
    "1. Columns are strictly associated with their respective tables as defined in the schema.\n"
    "3. Synonyms, antonyms, and linguistic variations in the user's prompt are used to infer intent, but the table and columns should be correct and matched with schema.\n\n"
    "Here is the database schema:\n"
    f"{schema_description}\n\n"
    "Instructions:\n"
    "- Use the schema to match tables and columns accurately, respecting case sensitivity.\n"
    "- Ensure that the output explicitly maps tables to their columns.\n"
    "- If the schema does not support the user's request, respond with: 'The schema does not support this request.'\n"
    "- Respond in the following structured format:\n\n"
    "  Entities:\n"
    "    TableName1: [Column1, Column2, ...]\n"
    "    TableName2: [Column1, Column2, ...]\n"
    "  Actions: [Action1, Action2, ...]\n\n"
    "Focus on accuracy, schema alignment, and clarity in your response."
    )


    # User message: specify the user's prompt
    user_message = (
    f"User Prompt: {prompt}\n\n"
    "Based on the provided database schema, identify the relevant tables and columns (entities) and actions required to fulfill the user's request. "
    "Respond in the following structured format:\n\n"
    "  Entities:\n"
    "    TableName1: [Column1, Column2, ...]\n"
    "    TableName2: [Column1, Column2, ...]\n"
    "  Actions: [Action1, Action2, ...]"
    )


    # OpenAI API call to extract entities and actions
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ]
    )

    print('-------------------response-------------->', response)
    # Parse the response
    response_content = response['choices'][0]['message']['content']
    return response_content
    # Extract entities and actions (assuming the response format specifies these clearly)
    try:
        entities_start = response_content.index("Entities:") + len("Entities:")
        actions_start = response_content.index("Actions:") + len("Actions:")
        
        entities = response_content[entities_start:actions_start - len("Actions:")].strip().split(", ")
        actions = response_content[actions_start:].strip().split(", ")
    except ValueError:
        # Handle cases where "Entities:" or "Actions:" is missing
        entities = []
        actions = []
    print('entities====>', entities,  '\n\nactions====>', actions)
    return entities, actions
