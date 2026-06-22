
def validar_codigo(codigo):
    """Valida que el código no esté vacío."""
    return codigo.strip() != ""

def validar_nombre(nombre):
    """Valida que el nombre no esté vacío."""
    return nombre.strip() != ""

def buscar_reserva_por_codigo(reservas, codigo):
    """
    Busca una reserva por su código.
    Retorna una tupla: (índice, diccionario_reserva) si existe, o (None, None) si no.
    """
    for i, reserva in enumerate(reservas):
        if reserva["codigo"] == codigo:
            return i, reserva
    return None, None

def calcular_categoria(total):
    """Calcula la categoría de la reserva según el monto total."""
    if total < 200000:
        return "Económica"
    elif total <= 500000:
        return "Estándar"
    else:
        return "Premium"

def leer_entero_positivo(mensaje):
    """Solicita un entero mayor a cero con manejo de excepciones."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: El valor debe ser mayor a 0.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")





def mostrar_menu():
    print("\n" + "="*30)
    print(" SISTEMA DE GESTIÓN DE HOTELES ")
    print("="*30)
    print("1. Registrar reserva")
    print("2. Buscar reserva")
    print("3. Actualizar reserva")
    print("4. Eliminar reserva")
    print("5. Mostrar reservas")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    print("="*30)




def leer_opcion():
    try:
        opcion = int(input('Ingrese una opción del 1 AL 7: '))
        if 1 <= opcion <= 7:
            return opcion
        else:
            print("Error: Opción fuera de rango (1-7).")
            return 0
    except ValueError:
        print('ERROR: Debe ingresar un número entero.')
        return 0
    
# Opcion 1
def registrar_reserva(reservas):
    print('\n--- REGISTRAR RESERVA ---')
    codigo = input("Ingrese código de reserva: ").strip()
    
    if not validar_codigo(codigo):
        print("Error: El código no puede estar vacío.")
        return

   
    _, encontrada = buscar_reserva_por_codigo(reservas, codigo)
    if encontrada is not None:
        print("Error: El código de la reserva ya existe.")
        return

    nombre = input("Ingrese nombre del huésped: ").strip()
    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío.")
        return
    
    noches = leer_entero_positivo("Ingrese la cantidad de noches de estadía: ")
    valor_noche = leer_entero_positivo("Ingrese el valor por noche: ")
    
    # Cálculos automáticos
    total = noches * valor_noche
    categoria = calcular_categoria(total)
    

    nueva_reserva = {
        "codigo": codigo,
        "nombre": nombre,
        "noches": noches,
        "valor_noche": valor_noche,
        "total": total,
        "categoria": categoria
    }
    
    reservas.append(nueva_reserva)
    print(f"\n¡Reserva registrada con éxito! Categoría asignada: {categoria}")

# Opcion 2:
def buscar_reserva(reservas):
    print('\n--- BUSCAR RESERVA ---')
    codigo = input("Ingrese el código de la reserva a buscar: ").strip()
    
    posicion, reserva = buscar_reserva_por_codigo(reservas, codigo)
    
    if reserva is not None:
        print(f"\nReserva encontrada en la posición del registro: {posicion + 1}")
        print(f"Código: {reserva['codigo']}")
        print(f"Huésped: {reserva['nombre']}")
        print(f"Noches: {reserva['noches']}")
        print(f"Valor por noche: ${reserva['valor_noche']:,}")
        print(f"Total: ${reserva['total']:,}")
        print(f"Categoría: {reserva['categoria']}")
    else:
        print("Error: No se encontró ninguna reserva con ese código.")

# Opcion 3:
def actualizar_reserva(reservas):
    print('\n--- ACTUALIZAR RESERVA ---')
    codigo = input("Ingrese el código de la reserva a modificar: ").strip()
    
    _, reserva = buscar_reserva_por_codigo(reservas, codigo)
    
    if reserva is not None:
        print("\nDeje en blanco si no desea modificar el campo.")
        
        
        nuevo_nombre = input(f"Nombre actual ({reserva['nombre']}): ").strip()
        if nuevo_nombre != "":
            reserva['nombre'] = nuevo_nombre
            
        
        modificar_noches = input(f"Noches actuales ({reserva['noches']}) ¿Desea cambiar? (s/n): ").strip().lower()
        if modificar_noches == 's':
            reserva['noches'] = leer_entero_positivo("Ingrese nueva cantidad de noches: ")
            
        
        modificar_valor = input(f"Valor noche actual (${reserva['valor_noche']:,}) ¿Desea cambiar? (s/n): ").strip().lower()
        if modificar_valor == 's':
            reserva['valor_noche'] = leer_entero_positivo("Ingrese nuevo valor por noche: ")
            
        
        reserva['total'] = reserva['noches'] * reserva['valor_noche']
        reserva['categoria'] = calcular_categoria(reserva['total'])
        
        print("\n¡Reserva actualizada con éxito!")
    else:
        print("Error: No se encontró ninguna reserva con ese código.")


def main():
    reservas = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            registrar_reserva(reservas)
        elif opcion == 2:
            buscar_reserva(reservas)
        elif opcion == 3:
            actualizar_reserva(reservas)
        elif opcion == 4:
            eliminar_reserva(reservas)
        elif opcion == 5:
            mostrar_reservas(reservas)
        elif opcion == 6:
            mostrar_estadisticas(reservas)
        elif opcion == 7:
            print('\n* Gracias por utilizar el sistema. ¡Programa finalizado! *')
            break

if __name__ == "__main__":
    main()