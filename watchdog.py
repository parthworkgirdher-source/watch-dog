import os
import time
from datetime import datetime, timezone

CHECK_INTERVAL = 15 * 60
TIMEOUT = 96 * 60 * 60

def main():
    print("96-hour watchdog started.")
    print("This version checks a timer only.")
    print("It does not control Meta Business Suite.")

    while True:
        print("Watchdog running:", datetime.now(timezone.utc).isoformat())
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
