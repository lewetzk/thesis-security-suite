import os
import sqlite3

class LogExporter:
    def __init__(self, db_path='logs/logs.db'):
        """
        Initializes the LogExporter with the specified database path. Creates the logs directory
        and the database table if they do not exist.

        Args:
            db_path (str): The path to the SQLite database file. Defaults to 'logs/logs.db'.
        """
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self):
        """
        Creates the 'logs' table in the database if it does not already exist. The table
        stores log entries with the following columns: id, prompt, model, llm_answer, success,
        modifier_type, intent, judge_answer, prompt_name, and intent_category.
        """
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prompt TEXT NOT NULL,
                    model TEXT NOT NULL,
                    llm_answer TEXT NOT NULL,
                    success TEXT NOT NULL,
                    modifier_type TEXT,
                    intent TEXT,
                    judge_answer TEXT,
                    prompt_name TEXT, 
                    intent_category TEXT  
                )
            ''')
        print("Table 'logs' created successfully.")

    def insert_log(self, prompt, model, llm_answer, success, modifier_type=None, intent=None, judge_answer=None,
                   prompt_name=None, intent_category=None):
        """
        Inserts a log entry into the 'logs' table, including the category of the intent (intent_category).
        """
        with self.conn:
            self.conn.execute('''
                INSERT INTO logs (prompt, model, llm_answer, success, modifier_type, intent, judge_answer, prompt_name, intent_category)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
            prompt, model, llm_answer, success, modifier_type, intent, judge_answer, prompt_name, intent_category))
        print("Log inserted successfully.")

    def close(self):
        """
        Closes the connection to the SQLite database.
        """
        self.conn.close()
        print("Connection closed.")

