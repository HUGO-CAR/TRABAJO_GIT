
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
    



def eliminar_reserva(reservas):
    print('\n--- ELIMINAR RESERVA ---')
    codigo = input('Ingrese el código de la reserva a eliminar: ').strip()
    
    posicion, reserva = buscar_reserva_por_codigo(reservas, codigo)
    
    if reserva is not None:
        reservas.pop(posicion)
        print(f"¡La reserva con código '{codigo}' ha sido eliminada con éxito!")
    else:
        print("Error: No se encontró ninguna reserva con ese código.")


def mostrar_reservas(reservas):
    print('\n--- LISTADO DE RESERVAS ---')
    if not reservas:
        print("No hay reservas registradas en el sistema.")
        return
        
    for idx, r in enumerate(reservas, start=1):
        print(f"\n[{idx}] Código: {r['codigo']} | Huésped: {r['nombre']}")
        print(f"    Estadía: {r['noches']} noches x ${r['valor_noche']:,} c/u")
        print(f"    Monto Total: ${r['total']:,} ({r['categoria']})")


def mostrar_estadisticas(reservas):
    print('\n--- ESTADÍSTICAS DEL SISTEMA ---')
    cant_reservas = len(reservas)
    
    if cant_reservas == 0:
        print("No hay datos suficientes para calcular estadísticas.")
        return
        
    ingresos_totales = sum(r['total'] for r in reservas)
    promedio_ingresos = ingresos_totales / cant_reservas
    
    # Buscar la reserva de mayor valor
    reserva_max = max(reservas, key=lambda x: x['total'])
    
    print(f"Cantidad total de reservas: {cant_reservas}")
    print(f"Ingresos totales del hotel: ${ingresos_totales Glyphs:,}")
    print(f"Promedio de ingresos por reserva: ${promedio_ingresos:,.2f}")
    print(f"Reserva de mayor valor: Código {reserva_max['codigo']} de {reserva_max['nombre']} por ${reserva_max['total']:,}")




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
