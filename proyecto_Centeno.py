###############################################
#    Proyecto de realizar y aceptar los PR    #
###############################################

########################
#  Importar librerías  #
########################

import numpy as np
import pandas as pd

############################################
#   DataFrame iniciada por O Centeno       #
############################################

# Create a DataFrame with 5 cases
df = pd.DataFrame({
    "Country": ["France", "Italy", "Spain", "Greece", "Portugal"],
    "City": ["Paris", "Rome", "Barcelona", "Athens", "Lisbon"],
    "Hotel Cost per Day": [100, 150, 120, 100, 110],
    "Air Ticket": [200, 250, 200, 220, 210]
})

# Print the DataFrame
print(df)

#DATAFRAME ARIANA 


pastelería={"Nombre Producto":["vainilla", "chocolate", "red velvet", "marmoleado", "Limón"], 
"Cantidad de Ventas":[25,15,20,10, 5], 
"Costo de Produccion":[187500, 112500, 160000, 75000, 45000],
"Margen de Beneficio":[187500, 112500, 160000, 75000, 45000],  
"Precio de Venta": [375000, 225000, 360000, 150000, 90000]}
pt = pd.DataFrame(pastelería)
print(pt)