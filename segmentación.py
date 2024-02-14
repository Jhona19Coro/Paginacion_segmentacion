import pandas as pd

# Crear un DataFrame de ejemplo
data = {'ID': range(1, 101),
        'Name': [f'Person {i}' for i in range(1, 101)],
        'Age': [20 + i for i in range(100)]}
df = pd.DataFrame(data)

def segment_dataframe(dataframe, segment_size):
    """
    Función para segmentar un DataFrame en segmentos de tamaño especificado.

    Args:
    - dataframe: DataFrame a segmentar.
    - segment_size: Tamaño de cada segmento.

    Returns:
    - Una lista de segmentos, donde cada segmento contiene segment_size filas.
    """
    num_rows = len(dataframe)
    return [dataframe.iloc[i:i + segment_size, :] for i in range(0, num_rows, segment_size)]

# Ejemplo de uso:
segment_size = 20
result = segment_dataframe(df, segment_size)
print(result)


