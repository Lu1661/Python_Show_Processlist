import mysql.connector
import time
from tabulate import tabulate

config = {                                                                          # Configuración de la conexión a MySQL
    'user': 'USUARIO',
    'password': f'CONTRASEÑA@',
    'host': '999.999.999.999',
    'database': 'BASEDEDATOS',
}
def show_processlist():                                                             # Función para ejecutar y mostrar el resultado de SHOW PROCESSLIST
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("SHOW PROCESSLIST")
    processes = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]                               # Obtener los nombres de las columnas
    table = tabulate(processes, headers=column_names, tablefmt="fancy_grid")        # Tabular los resultados  
    print(table)                                                                    # Imprimir la tabla formateada
    cursor.close()
    connection.close()
while True:                                                                         # Bucle principal
    show_processlist()
    print("Actualizando en 3 segundos...")
    time.sleep(3)
