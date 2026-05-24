import os

def generador_de_archivo_grande(nombre_archivo, tamano_mb_necesario):
    print(f"Generando el archivo '{nombre_archivo}' de aproximadamente {tamano_mb_necesario}MB...")
    
    
    texto_base = (
        "la nube verde es el futuro de la ingenieria de software sustentable "
        "los centros de datos consumen mucha energia y agua para refrigeracion "
        "Rust es un lenguaje eficiente y rapido mientras que Python es mas lento "
        "optimizacion codigo arquitectura servidores computacion impacto ambiental "
        "espiral de wintel hardware software sistema operativo eficiencia energetica\n"
    )
    
   
    #Medimos el tanaño real del archivo convirtiendo el texto a byres
    bytes_base = texto_base.encode('utf-8')
    tamano_base = len(bytes_base)
    
    # Calculamos cuántas veces tenemos que repetir este texto para llegar al peso pedido
    bytes_objetivo = tamano_mb_necesario * 1024 * 1024
    repeticiones = bytes_objetivo // tamano_base
    
    # Escribo el archivo en bloques para no saturar la RAM al crearlo
    with open(nombre_archivo, 'wb') as f:
        for _ in range(repeticiones):
            f.write(bytes_base)
            
    tamano_final = os.path.getsize(nombre_archivo) / (1024 * 1024)
    print(f"Archivo creado con éxito. El tamaño real del archivo: {tamano_final:.2f} MB")

if __name__ == "__main__":
    #Archivo de 100MB llamado 'datos_prueba.txt'
    generador_de_archivo_grande("datos_prueba.txt", 100)