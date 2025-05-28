# Kindle Dashboard

A simple dashboard web application for Kindle, featuring a to-do list, clock, media, timer, and days left tracker.

## Features

- Media controller
- To-do list with unfinished and completed tasks
- Clock, timer, and days left/quotes navigation
- Simple, Kindle-friendly UI

## Setup kindle

1. Jailbreak and install KUAL -> https://kindlemodding.org/

2. Get the browser to go fullscreen [kindle-kual-fullmesquite](https://github.com/mitchellurgero/kindle-kual-fullmesquite). If you are on 5.16.4+, you could try [kindle-shortcut-browser](https://github.com/mitchellurgero/kindle-shortcut-browser) (Not tested). Big thank you to [Mitchell Urgero](https://github.com/mitchellurgero) :)

3. If you plan on using the media controller or the todo widgets, then you need to setup a local server on your computer which can be polled from the dashboard.


4. **Install backend dependencies:**
   To download the requirements run:
   ```sh
   pip install -r requirements.txt
   ```

3. **Start the backend server:**
   Run to start the server:
   ```sh
   python backend/app.py
   ```
   *(Adjust the path and command as needed for your backend.)*

4. **Serve the frontend:**
   - The frontend files are in the `frontend/` directory.
   - Use a hosting service(like vercel) if you want the dashboard running when your computer is switched off.
   - Or use a simple HTTP server:
     ```sh
     cd frontend
     python -m http.server 8000
     ```
     Then visit url in your kindle browser.

## Configuration

- Ensure the `BASE_URL` variable in your frontend JavaScript points to your backend flask server's address (e.g., `http://localhost:8080`).


## Notes

- Media controls use playerctl which does not have windows support 
- Only tested with kindle paperwhite 4th gen
- Feel free to contribute 

## License

MIT License.
