# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer

def main():
    filename = input("Nombre del archivo: ")
    with open(filename, "r") as file:
        max_laps = int(file.readline().strip())
        timer = lap_timer.init(max_laps)
        for line in file:
            time = float(line.strip())
            lap_timer.add_lap(timer, time)
    result = lap_timer.longest_decreasing_streak(timer)
    

if __name__ == "__main__":
    main()
