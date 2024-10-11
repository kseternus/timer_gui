import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import time


def start_timer():
    global running, time_left
    if not running:
        try:
            hours = int(hours_entry.get())
            minutes = int(minutes_entry.get())
            seconds = int(seconds_entry.get())
            time_left = hours * 3600 + minutes * 60 + seconds
            hours_entry.config(state='disabled')
            minutes_entry.config(state='disabled')
            seconds_entry.config(state='disabled')
            running = True
        except ValueError:
            messagebox.showerror('Invalid Time', 'Please enter valid integers for hours, minutes, and seconds.')


def stop_timer():
    global running
    if running:
        running = False


def restart_timer():
    global running, time_left
    running = False
    hours_entry.config(state='normal')
    minutes_entry.config(state='normal')
    seconds_entry.config(state='normal')
    hours_entry.delete(0, tk.END)
    minutes_entry.delete(0, tk.END)
    seconds_entry.delete(0, tk.END)
    hours_entry.insert(0, '00')
    minutes_entry.insert(0, '00')
    seconds_entry.insert(0, '00')
    timer_label.config(text='00:00:00')
    time_left = 0


def update_timer():
    global time_left, running
    if running and time_left > 0:
        time_left -= 1
        time_str = time.strftime('%H:%M:%S', time.gmtime(time_left))
        timer_label.config(text=time_str)

    if time_left == 0 and running:
        # Set time left to 00:00:00 to prevent stopping on 00:00:01 while playing sound
        timer_label.config(text='00:00:00')
        root.update()   # Update root to set time at 00:00:00
        running = False
        playsound('alarm.mp3')  # Play the sound when the timer finishes

    root.after(1000, update_timer)


# Initialize variables
running = False
time_left = 0

# Create the Tkinter window
root = tk.Tk()
root.title('Timer')
root.geometry('400x300')
root.resizable(False, False)

# Timer Label
timer_label = tk.Label(root, text='00:00:00', font=('Helvetica', 48))
timer_label.pack(pady=(40, 20))

# Time Entry (Separated into hours, minutes, seconds)
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

hours_entry = tk.Entry(entry_frame, width=3, font=('Helvetica', 20), justify='center')
hours_entry.insert(0, '00')
hours_entry.grid(row=0, column=0)

colon_label1 = tk.Label(entry_frame, text=':', font=('Helvetica', 20))
colon_label1.grid(row=0, column=1)

minutes_entry = tk.Entry(entry_frame, width=3, font=('Helvetica', 20), justify='center')
minutes_entry.insert(0, '00')
minutes_entry.grid(row=0, column=2)

colon_label2 = tk.Label(entry_frame, text=':', font=('Helvetica', 20))
colon_label2.grid(row=0, column=3)

seconds_entry = tk.Entry(entry_frame, width=3, font=('Helvetica', 20), justify='center')
seconds_entry.insert(0, '00')
seconds_entry.grid(row=0, column=4)

# Start, Stop, Restart Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text='Start', command=start_timer)
start_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(button_frame, text='Stop', command=stop_timer)
stop_button.grid(row=0, column=1, padx=10)

restart_button = tk.Button(button_frame, text='Restart', command=restart_timer)
restart_button.grid(row=0, column=2, padx=10)

# Update the timer every second
update_timer()

# Run the Tkinter main loop
root.mainloop()
