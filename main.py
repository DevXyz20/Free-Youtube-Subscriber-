# follow me  on instagram  :  xyzrich.a
# Discord:  ------>>>>  @9li2
import os
import random
from colorama import init, Fore, Style
from pytube import YouTube
from time import sleep

init(autoreset=True)

ascii_art = """
██╗░░██╗██╗░░░██╗███████╗
╚██╗██╔╝╚██╗░██╔╝╚════██║
░╚███╔╝░░╚████╔╝░░░███╔═╝
░██╔██╗░░░╚██╔╝░░██╔══╝░░
██╔╝╚██╗░░░██║░░░███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
"""

def print_rainbow_art(art):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for line in art.splitlines():
        print("".join(random.choice(colors) + char for char in line))
        sleep(0.1)

file_name = "xyzbot.txt"
try:
    with open(file_name, "r") as f:
        accounts = f.readlines()
except FileNotFoundError:
    print(f"{Fore.RED}File {file_name} not found!")
    exit()

print_rainbow_art(ascii_art)

print(Fore.YELLOW + "[[ Follow me on Instagram  :  xyzrich.a ]]\n")
sleep(1)

print("Waiting to log in accounts...\n")
sleep(2)

for account in accounts:
    email, password = account.strip().split(":")
    print(f"Logging in with {email}...")
    print(f"{Fore.GREEN}Logged in (channel name in YouTube)\n")
    sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.RED + ascii_art)

print("Choose an action:\n")
print("1- Subscribe to a channel")
print("2- Like a video")
print("3- Comment on a video with a random emoji")

choice = input("\nEnter your choice: ")

def subscribe_to_channel():
    print(f"Subscribed to the channel!\n")

def like_video():
    print(f"Liked the video!\n")

def comment_on_video():
    emojis = ['😀', '😍', '🔥', '🎉', '💯']
    comment = f"Great video! {random.choice(emojis)}"
    print(f"Commented: {comment}\n")

if choice == "1":
    subscribe_to_channel()
elif choice == "2":
    like_video()
elif choice == "3":
    comment_on_video()
else:
    print(f"{Fore.RED}Invalid choice!")
# Add Accounts in xyzbot.txt
