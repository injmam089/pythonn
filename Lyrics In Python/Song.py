import time
import sys

GOLD = '\033[38;5;220m'
CYAN = '\033[38;5;51m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

def soul_typing(text, color, speed=0.05):
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

print()
soul_typing("✨ Initiating Heart-Connection...", WHITE)
time.sleep(1)

soul_typing("🎵 Now Playing: 'Dehleez Pe Mere dil ki' 🕯️", GOLD)
print()

lyrics = [
    "Dekha Zamaana Saara Bharam hai...",
    "Ishq Ibadat...",
    "Ishq Karam Hai...",
    "Mera Thikanaa...",
    "Teri Hi Dehleez hai..."
]

for line in lyrics:
    soul_typing(line, CYAN, 0.04)
    time.sleep(1)