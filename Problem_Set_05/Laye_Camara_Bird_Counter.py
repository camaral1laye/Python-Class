import pickle
import os

# Function to load bird counts from a file
def load_bird_counts(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return {}

# Function to save bird counts to a file
def save_bird_counts(bird_counts, filename):
    with open(filename, 'wb') as file:
        pickle.dump(bird_counts, file)

def main():
    filename = 'birds.bin'  # Updated filename
    bird_counts = load_bird_counts(filename)

    print("Bird Counter Program")
    print()
    print("Enter 'x' to exit")

    while True:
        bird_name = input("Enter name of bird: ")
        if bird_name.lower() == 'x':
            break

        # Normalize the bird name to title case
        bird_name = bird_name.title()

        # Update the count of the bird
        if bird_name in bird_counts:
            bird_counts[bird_name] += 1
        else:
            bird_counts[bird_name] = 1

    # Save the bird counts to the file
    save_bird_counts(bird_counts, filename)

    # Sort the bird names and display the counts
    print("\nName                      Count")
    print("========================= =====")
    for bird in sorted(bird_counts):
        print(f"{bird:<25} {bird_counts[bird]}")

if __name__ == "__main__":
    main()