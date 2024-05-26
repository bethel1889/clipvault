import argparse
import json
import pyperclip as clipboard
import threading
import tkinter as tk
from tkinter import ttk
from typing import List, Union

SAVED_DATA = "clipvault.json"
THEMES = ['clam', 'alt', 'default', 'classic']
STATUS = 1


def get_args() -> None:
    """
    Parse command-line arguments for ClipVault.

    The arguments include font size, maximum number of copied entries, 
    number of characters in the preview, and the window theme.

    Returns:
        Namespace: An object with the parsed arguments as attributes.
    """
    parser = argparse.ArgumentParser(description="ClipVault: A clipboard history manager that saves and manages your clipboard entries.")
    parser.add_argument("-f", default=15, help="The font size, default is 15", type=int)
    parser.add_argument("-m", default=10, help="The maximum number of copied data stored, default is 10", type=int)
    parser.add_argument("-p", default=10, help="The number of characters shown in preview, default is 10", type=int)
    parser.add_argument("-t", default="clam", help=f"The theme of the window, available themes are; {THEMES}")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    MAX = args.m
    F_SIZE = args.f
    P_CHARS = args.p

    if args.t in THEMES:
        CURRENT_THEME = args.t
    else:
        CURRENT_THEME = THEMES[0]

    root = tk.Tk()


def main() -> None:
    """
    Main function to start the clipboard tracking thread and initialize the Tkinter window.
    """
    thread = threading.Thread(target=track_clipboard)
    thread.start()

    style = ttk.Style()
    style.theme_use(CURRENT_THEME)

    root.title("ClipVault")
    label = tk.Label(root, text="ClipVault History", font=('Arial', F_SIZE))
    label.pack(padx=20, pady=20)

    create_frame()
    root.mainloop()


def track_clipboard() -> None:
    """
    Function to track changes in the clipboard and save unique entries to a JSON file.
    """
    while True:
        if STATUS == 0:
            break

        try:
            state = root.winfo_exists()
        except:
            close_window()

        data = load(SAVED_DATA)

        if not data:
            n = 0
            previous = ""
            data = []
        else:
            n = len(data)
            previous = data[n - 1]

        current = clipboard.paste()
        if not validate(previous, current):
            continue

        if current in data:
            continue        
        if n == MAX:
            data = data[1:]

        data.append(current)
        save(SAVED_DATA, data)


def validate(previous: str, current: str) -> bool:
    """
    Validate the current clipboard content against the previous content.

    Args:
        previous (str): The previous clipboard content.
        current (str): The current clipboard content.

    Returns:
        bool: True if the current content is valid, False otherwise.
    """
    if previous == current:
        return False

    if not current.strip():
        return False
    return True


def save(filepath: str, data: List[str]) -> bool:
    """
    Save data to a JSON file.

    Args:
        filepath (str): The path to the JSON file.
        data (List[str]): The data to be saved.

    Returns:
        bool: True if data is saved successfully, False otherwise.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(data, f)
        return True
    except:
        return False


def load(filepath: str) -> List[str]:
    """
    Load data from a JSON file.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        List[str]: The loaded data, or an empty list if loading fails.
    """
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return []


def clear(frame: tk.Frame) -> None:
    """
    Clear the clipboard history and update the display frame.

    Args:
        frame (tk.Frame): The frame to be updated.
    """
    save(SAVED_DATA, [])
    update_frame(frame)


def delete(data: List[str], n: int, frame: tk.Frame) -> None:
    """
    Delete an entry from the clipboard history and update the display frame.

    Args:
        data (List[str]): The clipboard history data.
        n (int): The index of the entry to be deleted.
        frame (tk.Frame): The frame to be updated.
    """
    del data[n]
    save(SAVED_DATA, data)
    update_frame(frame)


def create_frame() -> None:
    """
    Create the display frame with clipboard history and control buttons.
    """
    # Initialize the frame
    buttonframe = tk.Frame(root)

    # Initialize columns
    for i in range(6):
        buttonframe.columnconfigure(i, weight=1)

    # Header labels
    header1 = tk.Label(buttonframe, text="SN", font=('Arial', F_SIZE))
    header1.grid(row=0, column=0, sticky=tk.W + tk.E)

    header2 = tk.Label(buttonframe, text="Preview", font=('Arial', F_SIZE))
    header2.grid(row=0, column=1, columnspan=3, sticky=tk.W + tk.E)

    header3 = tk.Label(buttonframe, text="Actions", font=('Arial', F_SIZE))
    header3.grid(row=0, column=4, columnspan=2, sticky=tk.W + tk.E)

    # Footer buttons
    exit_button = tk.Button(buttonframe, text="Quit", command=close_window, font=('Arial', F_SIZE))
    exit_button.grid(row=12, column=0, columnspan=3, sticky=tk.W + tk.E)

    clear_history = tk.Button(buttonframe, text="Clear History", command=lambda: clear(buttonframe), font=('Arial', F_SIZE))
    clear_history.grid(row=12, column=3, columnspan=2, sticky=tk.W + tk.E)

    update_button = tk.Button(buttonframe, text="Refresh", command=lambda: update_frame(buttonframe), font=('Arial', F_SIZE))
    update_button.grid(row=12, column=5, columnspan=2, sticky=tk.W + tk.E)

    # Load data and create dynamic content
    clip_data = load(SAVED_DATA)
    if not clip_data:
        buttonframe.pack()
        return

    l = len(clip_data)
    for n in range(l):
        preview = clip_data[n].strip()[:P_CHARS] + "..."
        sn = tk.Label(buttonframe, text=n + 1, font=('Arial', F_SIZE))
        sn.grid(row=n + 1, column=0, sticky=tk.W + tk.E)

        text = tk.Label(buttonframe, text=preview, font=('Arial', F_SIZE))
        text.grid(row=n + 1, column=1, columnspan=3, sticky=tk.W + tk.E)

        delete_button = tk.Button(buttonframe, text="delete", command=lambda n=n: delete(clip_data, n, buttonframe), font=('Arial', F_SIZE))
        delete_button.grid(row=n + 1, column=4, sticky=tk.W + tk.E)

        copy_button = tk.Button(buttonframe, text="copy", command=lambda n=n: clipboard.copy(clip_data[n]), font=('Arial', F_SIZE))
        copy_button.grid(row=n + 1, column=5, sticky=tk.W + tk.E)

    # Pack frame
    buttonframe.pack(fill=tk.BOTH, expand=True)


def update_frame(frame: tk.Frame) -> None:
    """
    Update the display frame by destroying and recreating it.

    Args:
        frame (tk.Frame): The frame to be updated.
    """
    frame.destroy()
    create_frame()


def close_window() -> None:
    """
    Close the Tkinter window and stop the clipboard tracking thread.
    """
    global STATUS
    STATUS = 0
    root.quit()


if __name__ == "__main__":
    main()