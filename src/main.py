from ticketing_utils import *  # Import all helper functions from ticketing_utils


# Show menu options to the user
def menu():
    print("""
--- Help Desk Ticketing System ---
1. Create Ticket
2. View All Tickets
3. View Open Tickets
4. Close Ticket
5. Escalate Ticket
6. Exit
""")


# Main program loop
def run():
    init_db()  # Make sure database and table are ready

    while True:
        menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            # Prompt user to enter ticket details
            requester = input("Requester Name: ")
            issue = input("Issue Description: ")
            category = input("Category (Hardware / Software / Network): ")
            priority = input("Priority (Low / Medium / High): ")
            create_ticket(requester, issue, category, priority)
            print("✅ Ticket created.\n")

        elif choice == '2':
            # Show all tickets
            print("\n--- All Tickets ---")
            for ticket in view_tickets():
                print(ticket)

        elif choice == '3':
            # Show only open tickets
            print("\n--- Open Tickets ---")
            for ticket in view_tickets("Open"):
                print(ticket)

        elif choice == '4':
            # Close a specific ticket
            ticket_id = input("Enter Ticket ID to Close: ")
            close_ticket(ticket_id)
            print("✅ Ticket closed.\n")

        elif choice == '5':
            # Escalate a specific ticket
            ticket_id = input("Enter Ticket ID to Escalate: ")
            escalate_ticket(ticket_id)
            print("🚨 Ticket escalated.\n")

        elif choice == '6':
            print("Exiting system. Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")


# Start the app
if __name__ == "__main__":
    run()
