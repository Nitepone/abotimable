#!/usr/bin/env false
if __name__ == "__main__": raise SystemExit("Do not execute this script.")

import sqlite3, logging
from dataclasses import dataclass

def ensure_table_exists():
    conn = sqlite3.connect('sqlite3.db')
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS bot ("
        "token VARCHAR(255) NOT NULL,"
        "team_name VARCHAR(255) NOT NULL UNIQUE,"
        "team_id VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE"
        ");"
    );
    conn.commit()
    conn.close()

@dataclass
class Bot:
    token: str
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
            c.execute("INSERT INTO bot (team_name, team_id, token) VALUES ('{}', '{}', '{}')".format(self.team_name, self.team_id, self.token));
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
    for row in c.execute("SELECT team_id, team_name, token FROM bot"):
        yield Bot(team_id=row[0], team_name=row[1], token=row[2])
