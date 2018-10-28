#!/usr/bin/env false
if __name__ == "__main__": raise SystemExit("Do not execute this script.")

import sqlite3, logging
from dataclasses import dataclass

def ensure_table_exists():
    conn = sqlite3.connect('sqlite3.db')
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS bot ("
        "bot_user_id VARCHAR(255) NOT NULL,"
        "bot_access_token VARCHAR(255) NOT NULL,"
        "team_name VARCHAR(255) NOT NULL UNIQUE,"
        "team_id VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE"
        ");"
    );
    conn.commit()
    conn.close()

@dataclass
class Bot:
    bot_user_id: str
    bot_access_token: str
    team_name: str
    team_id: str

    def save(self):
        """
        Save this bot into the database
        """
        ensure_table_exists()
        # TODO don't allow SQL injection
        conn = sqlite3.connect('sqlite3.db')
        c = conn.cursor()
        try:
            c.execute(
                "INSERT INTO bot (bot_user_id, bot_access_token, team_name, team_id) "
                "VALUES ('{}', '{}', '{}', '{}')".format(self.bot_user_id, self.bot_access_token, self.team_name, self.team_id)
            )
        except sqlite3.IntegrityError as e:
            logging.error(e);
        conn.commit()
        conn.close()

def get_bots():
    """
    generator to load Bot objects from database
    """
    conn = sqlite3.connect('sqlite3.db')
    c = conn.cursor()
    for row in c.execute("SELECT bot_user_id, bot_access_token, team_name, team_id FROM bot"):
        yield Bot(bot_user_id=row[0], bot_access_token=row[1], team_name=row[2], team_id=row[3])
