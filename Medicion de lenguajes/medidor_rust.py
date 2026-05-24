import subprocess
from codecarbon import EmissionsTracker

if __name__ == "__main__":
    print("Iniciando el entorno de medición para Rust...")
    
    # Inicializamos el tracker para Rust
    tracker = EmissionsTracker(project_name="Experimento_Rust", output_dir=".")
    tracker.start()
    
    try:
        # Ejecuto el archivo .exe que se compilo en /release
        # Uso la ruta relativa correcta hacia la carpeta target
        ruta_exe = r".\experimento_rust\target\release\experimento_rust.exe"
        
        # subprocess.run frena el script de Python hasta que el .exe de Rust termine por completo
        subprocess.run(ruta_exe, check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el binario de Rust: {e}")
    except FileNotFoundError:
        print("Error: No se encontró el ejecutable de Rust.")
        print("Asegurate de haber corrido 'cargo build --release' adentro de la carpeta experimento_rust.")
    finally:
        # Frenamos el tracker y guardamos los datos de Rust
        tracker.stop()
        print("Medición de Rust finalizada. Datos agregados en emissions.csv")