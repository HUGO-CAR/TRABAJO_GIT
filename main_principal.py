
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