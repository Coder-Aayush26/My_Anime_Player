import vlc
from tkinter import *
# Function to play/pause
def toggle_play_pause(event=None):  # Accept event for key binding
    if media_player.is_playing():
        media_player.pause()
    else:
        media_player.play()

# Function to stop and close
def close(event = None):
    media_player.stop()
    root.destroy()

# VLC media setup
media_player = vlc.MediaPlayer(
    r"C:\Users\Hp\Downloads\Telegram Desktop\017 - White Past, Hidden Ambition.mkv"
)

# Tkinter window setup
root = Tk()
root.title("Anime Remote")
root.geometry("240x60")  # Wide and short
root.resizable(False, False)
root.attributes("-topmost", True)

# Create a horizontal frame for side-by-side buttons
button_frame = Frame(root,bg="#2e2e2e")
button_frame.pack(pady=10)

# Buttons
play_pause_btn = Button(button_frame, text="Play/Pause", width=12, command=toggle_play_pause)
play_pause_btn.pack(side=LEFT, padx=5)

stop_btn = Button(button_frame, text="Stop & Exit", width=12, command=close)
stop_btn.pack(side=LEFT, padx=5)

# Bind spacebar to toggle play/pause
root.bind("<space>", toggle_play_pause)
root.bind("<Escape>",close)
# Handle window close
root.protocol("WM_DELETE_WINDOW", close)

# Start GUI loop
root.focus_force()
root.mainloop()



