# helpdesk-ticketing-system

# Help Desk Ticketing System (Python + SQLite)

This is a help desk simulation project built using Python. It mimics real-world Tier 1 IT support workflows by allowing you to create, track, resolve, and escalate tickets using a terminal-based interface. Ticket data is stored in a local SQLite database, and there’s also an optional Excel-based tracker to simulate manual ticket logging.

The goal of this project is to better understand how help desk systems work and to practice the kind of task management and documentation you'd see in an entry-level IT support or SOC environment.

---

## What Is a Ticket?

A ticket is a record of a technical issue or support request. It’s typically used in IT help desk and customer support environments to keep track of who reported an issue, what the issue is, when it was reported, and whether or not it has been resolved or escalated.

In the real world, if someone emails or calls IT saying “I can’t log into my account,” that request is logged as a ticket. Each ticket usually contains the following:

- A unique ticket ID
- Requester name
- Issue description
- Category (Hardware, Software, Network)
- Priority level (Low, Medium, High)
- Status (Open or Closed)
- Escalation flag (Yes or No)
- Time created

This project simulates that process using Python and SQLite.

---

## Project Features

- Create new support tickets
- View all tickets or only open ones
- Close resolved tickets
- Escalate tickets to higher support levels
- Simulate daily ticket volume using randomized sample data
- Log tickets in an Excel file (optional)

---

## Technologies and Components

### Python

Used to write the core logic of the system. It handles all ticket operations like creating, reading, updating, and escalating through a command-line interface (CLI). Python was chosen for its readability and ability to quickly automate simple workflows.

### SQLite

A lightweight file-based database used to store tickets in a persistent way. All ticket data is saved to a `database.db` file, allowing you to reopen and view tickets even after restarting the program. SQLite is easy to use and doesn’t require a server or installation.

### Command-Line Interface (CLI)

The program runs in the terminal. It simulates how many internal IT teams or sysadmins work—interacting with tools and systems via scripts instead of full web interfaces.

### Excel Spreadsheet (tickets.xlsx) – Optional

Some small IT teams and offices still track tickets manually using Excel. This project includes a sample Excel tracker to mirror that workflow. It can be used to manually log tickets, escalate actions, or prepare simple reports.

---

## Project Files and Their Purpose

helpdesk_ticketing_system/
├── main.py # Main program – shows menu and handles user input
├── ticketing_utils.py # Functions for ticket creation, escalation, and database updates
├── sample_data.py # Generates 25 fake tickets for testing purposes
├── database.db # SQLite database that stores tickets (auto-generated)
├── tickets.xlsx # Optional Excel-based manual ticket log

---

## How to Run the Project

1. Open your terminal and navigate to the project folder:
cd /path/to/helpdesk_ticketing_system/

2. (Optional) Generate fake tickets for testing:
python3 sample_data.py

3. Launch the help desk system:
python3 main.py

You’ll be able to:
- Create new tickets
- View open or all tickets
- Escalate or close tickets

---

## What I Learned

- How tickets are tracked and managed in a help desk environment
- The structure of real ticketing workflows (create, update, close, escalate)
- How to build a CLI app in Python
- How to use SQLite to store structured data
- How to document and manually track tickets using Excel

---

## Why I Built This

I wanted to simulate what it's like to work in Tier 1 technical support. This project gave me hands-on experience with issue tracking, escalation logic, and using both automated (database) and manual (Excel) tracking tools. It also helped me get more confident working with Python for real-world problems.

---

## Use Cases

This project is great for:

- Entry-level IT support or help desk training
- SOC Tier 1 simulation
- Resume or interview prep
- Practicing escalation and documentation workflows
- Small office ticket tracking

---

## Contact

Created by Sihon Evans  
GitHub: [https://github.com/siwavy](https://github.com/siwavy)  
LinkedIn: [https://linkedin.com/in/sihonevans](https://linkedin.com/in/sihonevans)
