def find_user_by_name(cursor, name):
    """Look up a user row by name."""
    query = f"SELECT * FROM users WHERE name = '{name}'"
    return cursor.execute(query)
