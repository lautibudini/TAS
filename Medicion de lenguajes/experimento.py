import collections
from codecarbon import EmissionsTracker

def procesar_archivo():
    print("Iniciando el procesamiento en Python...")
    
    # Abrimos el archivo grande y contamos las palabras
    with open("datos_prueba.txt", "r", encoding="utf-8") as f:
        texto = f.read()
        palabras = texto.split()
        
        # Contamos la frecuencia de cada palabra
        contador = collections.Counter(palabras)
        
        # Obtenemos las 10 palabras más comunes
        top_10 = contador.most_common(10)
        
    print("\n--- TOP 10 PALABRAS (PYTHON) ---")
    for palabra, frec in top_10:
        print(f"{palabra}: {frec} veces")
    print("--------------------------------\n")

if __name__ == "__main__":
    # Inicializamos el tracker de CodeCarbon para medir Watts y CO2
    tracker = EmissionsTracker(project_name="Experimento_Python", output_dir=".")
    tracker.start()
    
    try:
        procesar_archivo()
    finally:
        # Frenamos el tracker para que guarde los datos en 'emissions.csv'
        tracker.stop()
        print("Medición de Python finalizada. Se guardaron los datos en emissions.csv")