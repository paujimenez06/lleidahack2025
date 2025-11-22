import csv

archivo_nombre = 'farms 1.csv'
print(f"--- LEYENDO DATOS DE {archivo_nombre} ---")

try:
    # Cambiamos encoding a 'latin-1' para evitar errores con tildes en Windows
    with open(archivo_nombre, mode='r', encoding='latin-1') as archivo:
        # DictReader es más inteligente: nos deja pedir los datos por su nombre
        lector = csv.DictReader(archivo)
        
        print(f"✅ Columnas detectadas: {lector.fieldnames}")
        print("\n--- EJEMPLO DE LAS PRIMERAS GRANJAS ---")
        
        contador = 0
        for fila in lector:
            # Solo imprimimos si hay datos en la fila
            if fila['farm_id']:
                # Extraemos los datos clave para el reto
                id_granja = fila['farm_id']
                cerdos = fila['inventory_pigs']
                peso = fila['avg_weight_kg']
                capacidad = fila['capacity']
                
                print(f"🐷 Granja {id_granja} | Cerdos: {cerdos} | Peso medio: {peso}kg | Capacidad: {capacidad}")
                
                contador += 1
                if contador >= 5: # Paramos después de 5 para no llenar la pantalla
                    break

except Exception as e:
    print(f"❌ Ocurrió un error: {e}")