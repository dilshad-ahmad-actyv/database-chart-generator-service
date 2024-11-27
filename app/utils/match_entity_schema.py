def match_entities_to_schema(entities, schema):
    print('----------------------------------------------------------------------' )
    matched_tables = []
    matched_columns = []

    # Normalize entity and schema strings to lowercase for case-insensitive matching
    lower_entities = [entity.lower() for entity in entities]

    for table, columns in schema.items():
        table_lower = table.lower()

        # Check both directions: entity -> table and table -> entity
        if any(entity in table_lower or table_lower in entity for entity in lower_entities):
            matched_tables.append(table)

        for column in columns:
            column_lower = column.lower()

            # Check both directions: entity -> column and column -> entity
            if any(entity in column_lower or column_lower in entity for entity in lower_entities):
                matched_columns.append((table, column))

    return matched_tables, matched_columns
