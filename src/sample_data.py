from ticketing_utils import create_ticket, init_db
import random  # Used to randomly choose fake values

# List of fake people submitting tickets
requesters = ["Dr. Lee", "Sales Rep", "HR Assistant", "IT Intern", "Receptionist"]

# Ticket categories
categories = ["Software", "Hardware", "Network"]

# Common IT issues
issues = [
    "Outlook crashes on start",
    "Laptop won't power on",
    "Wi-Fi keeps disconnecting",
    "Printer is offline",
    "Browser freezes on login",
    "Can't access shared folder",
    "Audio not working on Zoom"
]

# Generate multiple fake tickets
def generate_tickets(n=25):
    init_db()  # Make sure database exists
    for _ in range(n):
        requester = random.choice(requesters)
        issue = random.choice(issues)
        category = random.choice(categories)
        priority = random.choice(["Low", "Medium", "High"])
        create_ticket(requester, issue, category, priority)

# Run this script directly to populate the system
if __name__ == "__main__":
    generate_tickets()
    print("✅ 25 fake tickets created.")
