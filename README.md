# LIST APP

A simple Python application using Tkinter to manage lists. This app allows users to input, view, search, update, and delete elements in a list. Additionally, users can load lists from files and export indexed lists as tables.

## Features

- Accepts space-separated or comma-separated lists.
- Displays indexed lists in a tabular format.
- Searches for an element and displays duplicate positions if applicable.
- Allows deleting elements from the list.
- Enables updating elements with new values.
- Supports loading lists from text files.
- Saves the output table to a file.

## Installation

### Prerequisites

Ensure you have Python installed (version 3.6 or later) along with the required dependencies.

### Install Required Packages

Run the following command to install dependencies:

```bash
pip install tabulate
```

## Usage

### Running the Application
Run the application:
   ```bash
   python list_app.py
   ```

### How to Use the App

1. **Enter a List:**
   - Input a list of elements in the provided text field.
   - The list can be space-separated or comma-separated.
   - Example: `apple, banana, cherry` or `apple banana cherry`

2. **Show Indexed List:**
   - Click **"Show Indexed List"** to display the list in a structured format with indices.

3. **Search for an Element:**
   - Enter an element in the search field and click **"Search Element"** to find its position.
   - If duplicates exist, all occurrences will be displayed.

4. **Delete an Element:**
   - Enter an element in the field and click **"Delete Element"** to remove it from the list.
   - The updated list will be displayed.

5. **Update an Element:**
   - Enter the element to be replaced and the new value.
   - Click **"Update Element"** to modify the list.

6. **Load a List from a File:**
   - Click **"Load from File"** to import a list from a `.txt` file.

7. **Download Table:**
   - Click **"Download Table"** to save the displayed indexed list as a `.txt` file.

## File Operations

- **Load from File:** Allows importing a list from a `.txt` file.
- **Download Table:** Saves the displayed list with indices into a `.txt` file.

## Dependencies

- `tkinter` (built-in with Python)
- `tabulate` (for formatting tables)
## Screenshot

![List App Screenshot](images/screenshot.png)

This project is open-source and free to use.

---

Enjoy using **LIST APP**! 🚀
