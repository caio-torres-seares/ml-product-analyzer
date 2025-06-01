import sqlite3

def save_to_db(df, db_path, table_name='phone'):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()