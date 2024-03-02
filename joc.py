import sys

def carregar_dades(nom_fitxer):
    try:
        with open(nom_fitxer, 'r') as fitxer:
            linies = fitxer.readlines()
        return linies
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        sys.exit(1)

def mostrar_pregunta_i_respostes(pregunta, respostes):
    print(f"\n\033[1;34m{pregunta}\033[0m")
    for i, resposta in enumerate(respostes, start=97):
        print(f"{chr(i)}) \033[1;36m{resposta}\033[0m")

def calcular_puntuacio(resposta_usuari, resposta_correcta, puntuacio):
    if resposta_usuari == resposta_correcta:
        puntuacio += 1
        print("\033[1;32mCorrecte! +1 punt\033[0m")
    else:
        puntuacio -= 0.2
        print("\033[1;31mIncorrecte. -0.2 punts\033[0m")
    return puntuacio

def main():
    puntuacio = 0
    preguntes_file = "preguntes.txt"
    respostes_file = "respostes.txt"

    preguntes = carregar_dades(preguntes_file)
    respostes_correctes = carregar_dades(respostes_file)

#    if len(preguntes) != len(respostes_correctes):
#        print("Error: El nombre de preguntes i respostes no coincideix.")
#        sys.exit(1)

    for i in range(0, len(preguntes), 5):
        pregunta = preguntes[i].strip()
        respostes = [r.strip() for r in preguntes[i + 1:i + 5]]
        resposta_correcta = respostes_correctes[i // 5].strip().lower()

        mostrar_pregunta_i_respostes(pregunta, respostes)
        resposta_usuari = input("La teva resposta: ").lower()

        puntuacio = calcular_puntuacio(resposta_usuari, resposta_correcta, puntuacio)

    print(f"\n\033[1;35mPuntuació Final: {puntuacio}\033[0m")

if __name__ == "__main__":
    main()

