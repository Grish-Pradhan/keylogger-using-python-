# Keylogger: Server and Client Implementation

This project consists of a server and client implementation for logging keystrokes. The client captures keystrokes on a device and sends them to the server for storage and analysis.

## Components

### Server (`serverside.py`)
- Listens for incoming connections from the client.
- Receives and logs keystrokes to a file (`server_keylog.txt`).

### Client (`clientside.py`)
- Captures keystrokes from a specified input device using the `evdev` library.
- Sends the captured keystrokes to the server.

## Features

- **Server:**
  - Configurable IP address and port.
  - Handles multiple incoming connections.
  - Logs all keystrokes to a text file.

- **Client:**
  - Monitors keyboard input via `evdev`.
  - Encodes and sends keystrokes to the server.
  - Maps special keys (e.g., Enter, Backspace) to human-readable formats.

## Prerequisites

### Server:
- Python 3.x

### Client:
- Python 3.x
- `evdev` library (install via `pip install evdev`)
- Access to the keyboard input device (may require root privileges).

## Setup and Usage

### Server:
1. Configure the `server_ip` and `server_port` in `serverside.py`.
   ```python
   server_ip = '127.0.0.1'  # Change to the desired IP address
   server_port = 12345      # Specify the listening port
   ```
2. Run the server script:
   ```bash
   python3 serverside.py
   ```
3. The server will log received keystrokes to `server_keylog.txt`.

### Client:
1. Configure the `server_ip`, `server_port`, and `input_device_path` in `clientside.py`.
   ```python
   server_ip = '127.0.0.1'         # Server IP address
   server_port = 12345            # Server port
   input_device_path = '/dev/input/event0'  # Path to the keyboard device
   ```
2. Run the client script:
   ```bash
   sudo python3 clientside.py
   ```
   > **Note:** Root privileges may be required to access the input device.

3. The client will send captured keystrokes to the server.

## Example Workflow

1. Start the server:
   ```
   Server listening on 127.0.0.1:12345
   Connection from ('127.0.0.1', 54321)
   Received: [Enter]
   ```

2. Start the client and press keys on the keyboard:
   ```
   Keylogger started. Press Ctrl+C to stop.
   ```

3. Keystrokes will be logged in `server_keylog.txt` on the server:
   ```
   [Enter]
   h
e
l
l
o
```

## Customization

- **Server IP and Port:** Update the `server_ip` and `server_port` variables in both scripts.
- **Keyboard Device:** Change the `input_device_path` in `clientside.py` to match your system's keyboard device.

## Troubleshooting

- **Permission Denied (Client):** Run the client script with `sudo`.
- **Device Not Found:** Verify the correct input device path using `ls /dev/input/`.
- **Connection Errors:** Ensure the server is running and reachable from the client.

## Security and Ethical Use

This project is intended for educational purposes and must be used responsibly. Unauthorized use of keyloggers is illegal and unethical.

## License

This project is open-source. Modify and use it responsibly.

