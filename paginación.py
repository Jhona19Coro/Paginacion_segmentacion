def paginate(items, page_size, page_number):
    """
    Función para paginar una lista de elementos.

    Args:
    - items: Lista de elementos a paginar.
    - page_size: Tamaño de cada página.
    - page_number: Número de página a recuperar (comenzando desde 1).

    Returns:
    - La página especificada de elementos, o una lista vacía si está fuera de rango.
    """
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index]

# Ejemplo de uso:
data = list(range(1, 101))  # Crear una lista de números del 1 al 100
page_number = 2
page_size = 10
result = paginate(data, page_size, page_number)
print(result)
