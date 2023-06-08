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