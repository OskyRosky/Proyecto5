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


###   ARIANA    ###

nuevos_datos= {"Country": ["Argentina", "Mexico", "Brazil"],
                "City": ["Buenos Aires", "San Cristobal", "Rio de Janeiro"],
                "Hotel Cost per Day":[70, 70, 125],
                "Air Ticket": [1200, 350, 800]
                }
dt_act= pd.concat([df, pd.DataFrame(nuevos_datos)], ignore_index=True)
print(dt_act)