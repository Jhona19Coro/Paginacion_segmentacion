import numpy as np

# Crear un array de ejemplo
data = np.random.randint(0, 100, size=(100, 5))  # Array de 100 filas y 5 columnas

def segment_array(array, segment_size):
    """
    Función para segmentar un array NumPy en segmentos de tamaño especificado.

    Args:
    - array: Array NumPy a segmentar.
    - segment_size: Tamaño de cada segmento.

    Returns:
    - Una lista de segmentos, donde cada segmento contiene segment_size filas.
    """
    num_rows = array.shape[0]
    return [array[i:i + segment_size, :] for i in range(0, num_rows, segment_size)]

# Ejemplo de uso:
segment_size = 20
result = segment_array(data, segment_size)
print(result)

