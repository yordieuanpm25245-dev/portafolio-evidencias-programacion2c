# ==============================================
# PROGRAMA DE GESTIÓN DE VENTAS (MODULARIZADO)
# ==============================================

# --- FUNCIÓN 1: Pedir datos al usuario ---
def capturar_datos():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    return nombre, precio, cantidad

# --- FUNCIÓN 2: Calcular el subtotal ---
def calcular_subtotal(precio, cantidad):
    return precio * cantidad

# --- FUNCIÓN 3: Aplicar descuento ---
def aplicar_descuento(monto):
    if monto > 1000:
        descuento = monto * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")
        return descuento
    else:
        return 0

# --- FUNCIÓN 4: Calcular IVA ---
def calcular_iva(monto):
    return monto * 0.16

# --- FUNCIÓN 5: Imprimir el ticket ---
def mostrar_ticket(producto, sub, desc, iva, total):
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${sub:.2f}")
    print(f"Descuento: -${desc:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("------------------------")

# ==============================================
#              PROGRAMA PRINCIPAL
# ==============================================

print("--- Sistema de Cobro v1.0 ---")

# Llamamos a las funciones en orden
producto, precio, cantidad = capturar_datos()

subtotal = calcular_subtotal(precio, cantidad)
descuento = aplicar_descuento(subtotal)
subtotal_con_desc = subtotal - descuento
iva = calcular_iva(subtotal_con_desc)
total_final = subtotal_con_desc + iva

mostrar_ticket(producto, subtotal, descuento, iva, total_final)