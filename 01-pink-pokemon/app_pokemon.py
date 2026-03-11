import random
import requests
import pprint
import sys


def get_pink_pokemons():
    """Obtiene una lista de especies de color rosa desde PokéAPI."""
    url = 'https://pokeapi.co/api/v2/pokemon-color/pink/'
    response = requests.get(url)
    data = response.json()
    return data['pokemon_species']


def save_and_load_list(pokemon_species):
    """Guarda los nombres en un archivo local y retorna una lista limpia."""
    with open('pinkpokemon.txt', 'w') as list_file:
        for entry in pokemon_species:
            list_file.write(entry['name'] + '\n')

    with open('pinkpokemon.txt', 'r') as f:
        return f.read().splitlines()


def play_round(nickname, pink_list):
    """Lógica principal del juego: Adivinanza y Batalla de Stats."""
    chosen_pokemon = random.choice(pink_list)

    # Ronda 1: Adivinar el nombre al revés
    print(f"\n--- Ronda 1 ---")
    print(f"Pista (nombre al revés): {chosen_pokemon[::-1]}")
    guess = input("¿Cuál es el nombre original?: ").lower()

    if guess == chosen_pokemon:
        print(f"¡Felicidades {nickname}, lo lograste!")
    else:
        print(f"¡Casi! Era {chosen_pokemon}.")

    # Ronda 2: Batalla de Stats
    print(f"\n--- Ronda 2 ---")
    print(f"Probando el poder de ataque de tu {chosen_pokemon}...")
    url = f'https://pokeapi.co/api/v2/pokemon/{chosen_pokemon}/'
    stats_data = requests.get(url).json()
    attack_stat = stats_data['stats'][1]['base_stat']

    print(f"Tu {chosen_pokemon} tiene un Ataque Base de: {attack_stat}")

    if attack_stat > 80:
        result = "¡Ganaste! Tienes el Pink Pokemon Power."
    else:
        result = "Perdiste esta ronda, ¡sigue entrenando!"

    print(result)
    return result


def main():
    print("=== Pink Pokemon Power App ===")
    nickname = input("Introduce tu nombre: ")

    start = input(f"¡Hola {nickname}! ¿Quieres jugar? (sí/no): ").lower()
    if start not in ["si", "sí", "yes"]:
        print("¡Hasta la próxima!")
        sys.exit()

    # Procesamiento de datos
    species = get_pink_pokemons()
    pink_list = save_and_load_list(species)

    print("\nLista de Pokémon Rosa disponibles:")
    pprint.pprint(", ".join([p.capitalize() for p in pink_list]))

    # Ejecución y Log
    final_msg = play_round(nickname, pink_list)

    with open('log.txt', 'a') as log_file:
        log_file.write(f"Jugador: {nickname} | Resultado: {final_msg}\n")


if __name__ == "__main__":
    main()
