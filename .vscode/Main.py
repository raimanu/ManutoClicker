import keyboard

def main():
    print("Press 'q' to quit.")
    while True:
        if keyboard.is_pressed('q'):
            break
        if keyboard.is_pressed('space'):
            print("Spacebar pressed!")

if __name__ == "__main__":
    main()