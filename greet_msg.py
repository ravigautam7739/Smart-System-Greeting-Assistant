import pyttsx3
import datetime
import psutil
import random

engine = pyttsx3.init()

messages = [
    "Ready to build something amazing today.",
    "Your system is fully operational.",
    "Let's make today productive."
]

battery = psutil.sensors_battery()
battery_percent = battery.percent

time_now = datetime.datetime.now().strftime("%I:%M %p")

text = f"""
Welcome back Sir.
Current time is {time_now}.
Battery is at {battery_percent} percent.
{random.choice(messages)}
"""

print(text)

engine.say(text)
engine.runAndWait()