def segment(items, segment_size):
    """
    Función para segmentar una lista de elementos en segmentos de tamaño especificado.

    Args:
    - items: Lista de elementos a segmentar.
    - segment_size: Tamaño de cada segmento.

    Returns:
    - Una lista de segmentos, donde cada segmento contiene segment_size elementos.
    """
    return [items[i:i + segment_size] for i in range(0, len(items), segment_size)]

# Ejemplo de uso:
data = list(range(1, 21))  # Crear una lista de números del 1 al 20
segment_size = 5
result = segment(data, segment_size)
print(result)
