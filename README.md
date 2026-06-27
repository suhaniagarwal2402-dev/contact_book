# Contact Book 

A clean, interactive Python terminal application designed to manage personal contacts. This project implements full CRUD capability (Create, Read, Update, Delete) locally within a command-line interface using dynamic data structures.

---

##  Features

* **Add a New Contact:** Collects contact name, phone number, and email address, storing them securely in a structured dictionary format.
* **View All Contacts:** Displays a cleanly indexed, numbered list of all your saved entries at a glance.
* **Search for a Contact:** Case-insensitive search that scans your directory by name to pull up specific records instantly.
* **Delete a Contact:** Allows you to effortlessly wipe out outdated entries from your list by matching names.
* **Robust Main Menu:** An interactive user interface wrapped in recursive validation logic to handle menu choices seamlessly without crashing.

---

##  Prerequisites

Before executing this script, ensure you have Python installed on your system:
* [Download Python](https://www.python.org/downloads/) (Version 3.x recommended)

---

## 💻 How to Run

1. **Open your terminal** and verify you are inside the isolated project directory where your file lives:
   ```bash
   cd contact_book
   
**System Architecture & Workflow**
1.Main Loop: Upon execution, the application initializes an empty registry contacts = [] and loops through an interactive numerical menu.

2.Data Model: Every individual record is captured as a key-value mapping dictionary:

Python
contact = {
    'name': 'Name',
    'phone': 'Phone Number',
    'email': 'Email Address'
}

3.Graceful Exit: Typing 0 cleanly terminates the thread and outputs a goodbye confirmation message.   
