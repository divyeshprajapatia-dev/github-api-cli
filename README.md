# GitHub User Info CLI (Learning Project)

This is a **Python CLI tool** built as part of my learning journey toward backend development and internship readiness.

The purpose of this project is **learning and practice**, not production use.  
It focuses on understanding how backend systems communicate using HTTP and JSON.

---

## What this tool does

This CLI tool fetches **public GitHub user information** using the GitHub REST API and displays it in a clean, human-readable format.

It demonstrates:
- Making HTTP GET requests
- Handling API responses and status codes
- Parsing JSON data
- Filtering useful information
- Writing clean, structured Python code

---

## Data shown

For a given GitHub username, the tool displays:

- Username
- Account type (User / Organization)
- Name
- Location
- Public repositories
- Followers
- Following
- Account creation date

Unnecessary fields like internal IDs, URLs, and links are intentionally ignored.

---

## Requirements

- Python 3.8+
- Internet connection
- Python package:
  - `requests`

---

## Setup (Recommended: Virtual Environment)

### 1. Create a virtual environment

```bash
python3 -m venv venv
```
### 2. Activate the virtual environment
```bash
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install requests
```

---

## Usage

Basic usage:
```
python3 github_user.py <github_username>
```
Example:
```
python3 github_user.py torvalds
```
Example Output
```
GitHub User Info
----------------
Username: torvalds
Account Type: User
Name: Linus Torvalds
Location: Portland, OR
Public Repos: 6
Followers: 292000
Following: 0
Account Created: 2011-09-03T15:26:22Z
```

---

## Error Handling

  - If the user does not exist, the tool handles the 404 response gracefully.
  - Network or unexpected errors are caught and reported cleanly.
  - Missing data fields are shown as "Not available" instead of None.

---

## Project Structure
```
github-api-cli/
├── github_user.py
├── README.md
└── venv/   (not committed)
```
---

## What I learned from this project

  - How HTTP GET requests work
  - How APIs return and structure JSON data
  - How to safely parse external data
  - Why separating logic and CLI output matters
  - How to use virtual environments properly
  - How backend systems communicate with each other

---

## Notes

  - Built and tested on Linux
  - Uses only standard Python libraries plus requests
  - This is a learning project, not a resume-ready production app

More features may be added as learning continues.
