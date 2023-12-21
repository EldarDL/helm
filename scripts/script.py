import requests
import csv


def get_characters():
    url = "https://rickandmortyapi.com/api/character/"
    params = {"species": "Human", "status": "Alive", "origin": "Earth (C-137)"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["results"]
    else:
        print(f"Error: {response.status_code}")
        return None


# Function to write results to CSV
def write_to_csv(characters):
    with open('../csv/rick_and_morty_characters.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'location', 'image'])

        for character in characters:
            writer.writerow([character['name'], character['location']['name'], character['image']])


# Main execution
if __name__ == "__main__":
    characters = get_characters()

    if characters:
        write_to_csv(characters)
        print("Results written to rick_and_morty_characters.csv")
