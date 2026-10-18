ROOMS = {
    "start": {"desc": "A dark room.", "exits": {"north": "hall"}},
    "hall": {"desc": "A long hall.", "exits": {"south": "start", "east": "treasure"}},
    "treasure": {"desc": "You found treasure!", "exits": {"west": "hall"}}
}

def main():
    here = "start"
    while True:
        room = ROOMS[here]
        print(f"\n{room['desc']}")
        cmd = input("> ").strip().lower()
        if cmd in room["exits"]:
            here = room["exits"][cmd]
        elif cmd in ("quit", "exit"):
            break
        else:
            print("You can't go that way.")

if __name__ == "__main__":
    main()