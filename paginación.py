import pandas as pd

# Crear un DataFrame de ejemplo
data = {'ID': range(1, 101),
        'Name': [f'Person {i}' for i in range(1, 101)],
        'Age': [20 + i for i in range(100)]}
df = pd.DataFrame(data)

def paginate_dataframe(dataframe, page_size, page_number):
    """
    Función para paginar un DataFrame.

    Args:
    - dataframe: DataFrame a paginar.
    - page_size: Tamaño de cada página.
    - page_number: Número de página a recuperar (comenzando desde 1).

    Returns:
    - La página especificada del DataFrame, o None si está fuera de rango.
    """
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return dataframe.iloc[start_index:end_index]

# Ejemplo de uso:
page_number = 2
page_size = 10
result = paginate_dataframe(df, page_size, page_number)
print(result)
