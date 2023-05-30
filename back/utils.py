import pandas as pd

class Utils:
    @classmethod
    def md_to_csv(cls, md_file_path, csv_file_path):
        # Leer el archivo .md y almacenar su contenido en una variable
        try:
            with open(md_file_path, 'r') as file:
                md_content = file.read()

            # Dividir el contenido del archivo .md por líneas
            lines = md_content.split('\n')

            # Crear una lista vacía para almacenar los datos
            data = []

            # Obtener las cabeceras de la tabla
            headers = [h.strip() for h in lines[0].split('|')[1:-1]]

            # Iterar sobre cada línea del archivo .md a partir de la tercera línea
            for line in lines[2:]:
                # Dividir cada línea por las tuberías (|) para obtener los valores de cada columna
                row = [v.strip() for v in line.split('|')[1:-1]]

                # Agregar la fila a la lista de datos
                data.append(row)

            # Crear un dataframe de pandas a partir de la lista de datos y las cabeceras
            df = pd.DataFrame(data, columns=headers)

            # Eliminar la última fila que contiene valores NaN
            #df.dropna(inplace=True)

            # Guardar el dataframe como un archivo .csv
            df.to_csv(csv_file_path, index=False)
            return True

        except Exception as e:
            print(e)

    @classmethod
    def csv_to_schema(self,nombre_csv):
        #
