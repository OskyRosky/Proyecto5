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

############################################
#   DataFrame iniciada por Marco           #
############################################
actualización = {"Country":["Nigeria", "Kenya", "South Africa"],
    "City": ["Abuja", "Nairobi", "Pretoria"],
    "Hotel Cost per Day": [50, 100, 120],
    "Air Ticket": [500, 450, 400]             
    }
act=pd.concat([df,pd.DataFrame(actualización)],ignore_index=True)
print(act)

############################################
#   DataFrame iniciada por Ariana          #
############################################



nuevos_datos= {"Country": ["Argentina", "Mexico", "Brazil"],
                "City": ["Buenos Aires", "San Cristobal", "Rio de Janeiro"],
                "Hotel Cost per Day":[70, 70, 125],
                "Air Ticket": [1200, 350, 800]
                }
dt_act= pd.concat([act, pd.DataFrame(nuevos_datos)], ignore_index=True)
print(dt_act)