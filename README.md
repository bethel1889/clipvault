# ClipVault
#### Video Demo:  <URL HERE>
#### Description:
ClipVault is a clipboard history manager built using Python and Tkinter. It saves and manages your clipboard entries, providing you with quick access to your clipboard history.

## Features
- **Clipboard Tracking**: Continuously monitors changes in the clipboard content.
- **Clipboard History**: Maintains a history of copied items, allowing you to access previously copied content.
- **Customization**: Customize font size, maximum history size, preview length, and window theme.
- **Intuitive Interface**: User-friendly interface for easy navigation and management of clipboard history.
- **Cross-Platform**: Works on Windows, macOS, and Linux platforms.

## Requirements
- Python 3.x
- Tkinter (Python's standard GUI library)
- Pyperclip (Cross-platform clipboard module)
- pytest (for running unit tests)

## Usage
### Installation:
1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip: pip install -r requirements.txt


### Run ClipVault:
- Run the `clipvault.py` script: python clipvault.py


### Command-line Arguments:
- You can customize ClipVault using command-line arguments: python clipvault.py -f <font_size> -m <max_entries> -p <preview_length> -t <theme>

- `-f <font_size>`: Set the font size (default is 15).
- `-m <max_entries>`: Set the maximum number of stored entries (default is 10).
- `-p <preview_length>`: Set the length of the preview text (default is 10 characters).
- `-t <theme>`: Set the theme of the window (default is "clam").
- example: python clipvault.py -f 15 -m 10 -p 10 -t clam
    This will start the clipboard manager with a font size of 15, a maximum of 10 entries, 10 characters in the preview, and the "clam" theme.

### Interacting with ClipVault:
- Clipboard entries are automatically saved and displayed in the ClipVault window.
- Use the "delete" button to remove entries from the history.
- Click on the "copy" button to copy an entry back to the clipboard.

### Exiting ClipVault:
- Click on the "Quit" button to exit the ClipVault application.

## Function Descriptions

### `get_args() -> None`
Parse command-line arguments for ClipVault.

The arguments include font size, maximum number of copied entries, number of characters in the preview, and the window theme.

Returns:
Namespace: An object with the parsed arguments as attributes.

### `main() -> None`
Main function to start the clipboard tracking thread and initialize the Tkinter window.

### `track_clipboard() -> None`
Function to track changes in the clipboard and save unique entries to a JSON file.

### `validate(previous: str, current: str) -> bool`
Validate the current clipboard content against the previous content.

Args:
  previous (str): The previous clipboard content.
  current (str): The current clipboard content.

Returns:
  bool: True if the current content is valid, False otherwise.

### `save(filepath: str, data: List[str]) -> bool`
Save data to a JSON file.

Args:
  filepath (str): The path to the JSON file.
  data (List[str]): The data to be saved.

Returns:
  bool: True if data is saved successfully, False otherwise.

### `load(filepath: str) -> List[str]`
Load data from a JSON file.

Args:
  filepath (str): The path to the JSON file.

Returns:
  List[str]: The loaded data, or an empty list if loading fails.

### `clear(frame: tk.Frame) -> None`
Clear the clipboard history and update the display frame.

Args:
  frame (tk.Frame): The frame to be updated.

### `delete(data: List[str], n: int, frame: tk.Frame) -> None`
Delete an entry from the clipboard history and update the display frame.

Args:
  data (List[str]): The clipboard history data.
  n (int): The index of the entry to be deleted.
  frame (tk.Frame): The frame to be updated.

### `create_frame() -> None`
Create the display frame with clipboard history and control buttons.

### `update_frame(frame: tk.Frame) -> None`
Update the display frame by destroying and recreating it.

Args:
  frame (tk.Frame): The frame to be updated.

### `close_window() -> None`
Close the Tkinter window and stop the clipboard tracking thread.

## Contributing
Contributions are welcome! If you have any ideas for improvements or find any issues, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.