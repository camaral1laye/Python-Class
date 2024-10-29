def load_world_cup_data(filename):
    champions = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                year, country, _, _ = line.strip().split(',')
                # Normalize country name for consistency
                country = country.strip()
                
                if country in champions:
                    champions[country]['wins'] += 1
                    champions[country]['years'].append(year)
                else:
                    champions[country] = {
                        'wins': 1,
                        'years': [year]
                    }
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return champions

def display_champions(champions):
    print("\nFIFA World Cup Winners")
    print()
    print("Country         Wins  Years           ")
    print("=======         ====  =====           ")
    
    # Sort countries alphabetically
    for country in sorted(champions):
        wins = champions[country]['wins']
        years = ', '.join(champions[country]['years'])
        print(f"{country:<15} {wins:<5} {years}")

def main():
    filename = 'world_cup_champions.txt'  # File containing World Cup data
    champions = load_world_cup_data(filename)

    if champions:
        display_champions(champions)

        # Find the country with the most wins
        most_wins_country = max(champions, key=lambda x: champions[x]['wins'])
        most_wins = champions[most_wins_country]['wins']

        print(f"\nThe country with the most championships is {most_wins_country} with {most_wins} wins.")

if __name__ == "__main__":
    main()