import sqlite3  # Built-in library to work with SQLite databases


# Create the ticket table if it doesn't exist
def init_db():
    conn = sqlite3.connect('database.db')  # Connect to the local database file
    c = conn.cursor()

    # Create the table structure for storing tickets
    c.execute('''
              CREATE TABLE IF NOT EXISTS tickets
              (
                  id
                  INTEGER
                  PRIMARY
                  KEY
                  AUTOINCREMENT,
                  requester
                  TEXT,
                  issue
                  TEXT,
                  category
                  TEXT,
                  priority
                  TEXT,
                  status
                  TEXT,
                  escalation
                  TEXT,
                  created_at
                  TIMESTAMP
                  DEFAULT
                  CURRENT_TIMESTAMP
              )
              ''')

    conn.commit()  # Save changes to the database
    conn.close()  # Close the connection


# Create and save a new ticket
def create_ticket(requester, issue, category, priority="Low"):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
              INSERT INTO tickets (requester, issue, category, priority, status, escalation)
              VALUES (?, ?, ?, ?, 'Open', 'No')
              ''', (requester, issue, category, priority))

    conn.commit()
    conn.close()


# View all tickets, or only those with a specific status (Open or Closed)
def view_tickets(status=None):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if status:
        c.execute("SELECT * FROM tickets WHERE status = ?", (status,))
    else:
        c.execute("SELECT * FROM tickets")

    results = c.fetchall()
    conn.close()
    return results


# Mark a ticket as closed
def close_ticket(ticket_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("UPDATE tickets SET status = 'Closed' WHERE id = ?", (ticket_id,))

    conn.commit()
    conn.close()


# Escalate a ticket to higher support
def escalate_ticket(ticket_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("UPDATE tickets SET escalation = 'Yes' WHERE id = ?", (ticket_id,))

    conn.commit()
    conn.close()
