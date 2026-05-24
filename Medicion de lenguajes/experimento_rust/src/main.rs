use std::collections::HashMap;
use std::fs::File;
use std::io::{BufReader, Read};
use std::time::Instant;

fn main() {
    println!("Iniciando procesamiento en Rust...");

    // Empezamos a medir el tiempo exacto de CPU desde acá adentro
    let inicio = Instant::now();

    // Especificamos la ruta 
    let ruta_archivo = "datos_prueba.txt";

    // Abrimos el archivo usando un buffer
    let archivo = match File::open(ruta_archivo) {
        Ok(file) => file,
        Err(_) => {
            println!("Error: No se encontró 'datos_prueba.txt' en la carpeta.");
            println!("Correr primero el generador.py.");
            return;
        }
    };
    
    let mut lector = BufReader::new(archivo);
    let mut contenido = String::new();
    
    if lector.read_to_string(&mut contenido).is_err() {
        println!("Error al leer el contenido del archivo.");
        return;
    }

    // Procesamos el texto (separamos por palabras, pasamos a minúsculas y contamos)
    let mut contador: HashMap<String, usize> = HashMap::new();

    for palabra in contenido.split_whitespace() {
        let palabra_minuscula = palabra.to_lowercase();
        *contador.entry(palabra_minuscula).or_insert(0) += 1;
    }

    // Pasamos el HashMap a un Vector para poder ordenarlo por frecuencia de mayor a menor
    let mut frecuencias: Vec<(String, usize)> = contador.into_iter().collect();
    frecuencias.sort_by(|a, b| b.1.cmp(&a.1));

    // Tomamos las 10 palabras más comunes
    let top_10 = frecuencias.iter().take(10);

    let duracion = inicio.elapsed();

    println!("\n--- TOP 10 PALABRAS (RUST) ---");
    for (palabra, frec) in top_10 {
        println!("{}: {} veces", palabra, frec);
    }
    println!("------------------------------\n");

    println!("Procesamiento de Rust finalizado");
    println!("Tiempo de ejecución medido : {:.2?}", duracion);
}