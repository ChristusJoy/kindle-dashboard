# Kindle Dashboard

A simple dashboard web application for Kindle, featuring a to-do list, clock, media, timer, and days left tracker.

## Features

- To-do list with unfinished and completed tasks
- Clock, media, timer, and days left/quotes navigation
- Simple, Kindle-friendly UI

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/) (if backend is Python-based)
- [pip](https://pip.pypa.io/en/stable/installation/) (for Python dependencies)
- A modern web browser

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd kindle-dashboard
   ```

2. **Install backend dependencies:**
   If there is a `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```

3. **Start the backend server:**
   If using Flask or similar, run:
   ```sh
   python backend/app.py
   ```
   *(Adjust the path and command as needed for your backend.)*

4. **Serve the frontend:**
   - The frontend files are in the `frontend/` directory.
   - You can open `frontend/index.html` directly in your browser, or use a simple HTTP server:
     ```sh
     cd frontend
     python -m http.server 8000
     ```
     Then visit [http://localhost:8000](http://localhost:8000) in your browser.

## Configuration

- Ensure the `BASE_URL` variable in your frontend JavaScript points to your backend server's address (e.g., `http://localhost:5000`).

## File Structure

```
kindle-dashboard/
├── backend/         # Backend server code (API)
├── frontend/        # Frontend HTML, CSS, JS, images
│   ├── index.html
│   ├── todo.html
│   ├── todo.css
│   └── images/
└── README.md
```

## Usage

- Navigate using the icons at the top of each page.
- Use the to-do list to track tasks. Click a task to toggle its completion status.
- Use the "Reset" button to clear all tasks.

## Notes

- For best results, use on a Kindle device or in a browser with a similar display size.
- If you encounter issues, check your browser's console and backend server logs for errors.

## License

MIT License (or specify your license here).
