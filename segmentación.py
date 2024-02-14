import pandas as pd

# Crear un DataFrame de ejemplo
data = {'ID': range(1, 101),
        'Name': [f'Person {i}' for i in range(1, 101)],
        'Age': [20 + i for i in range(100)]}
df = pd.DataFrame(data)

def paginate_and_segment_dataframe(dataframe, page_size, page_number, segment_size):
    """
    Función para paginar y segmentar un DataFrame.

    Args:
    - dataframe: DataFrame a paginar y segmentar.
    - page_size: Tamaño de cada página.
    - page_number: Número de página a recuperar (comenzando desde 1).
    - segment_size: Tamaño de cada segmento.

    Returns:
    - El segmento especificado del DataFrame paginado, o None si está fuera de rango.
    """
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    paginated_data = dataframe.iloc[start_index:end_index]
    
    segment_start_index = 0
    segment_end_index = segment_size
    segment_data = paginated_data.iloc[segment_start_index:segment_end_index]
    
    return segment_data

# Ejemplo de uso:
page_number = 2
page_size = 10
segment_size = 5
result = paginate_and_segment_dataframe(df, page_size, page_number, segment_size)
print(result)
