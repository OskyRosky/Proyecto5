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

#Marco

pelicula={"Nombre": ["Super Mario Bros", "The Whale", "Spiderman: Across", "Notting Hill", "Kiki:entregas a domicilio", "Green Book"], 
"Género":["animada", "drama", "animada", "romance", "anime", "Drama" ],
"Duración": ["1h32m", "1h57m", "2h20m", "2h04m", "1h42m", "2h10m"],
"Puntaje Rotten Tomatoes": [60, 65, 96, 85, 99, 77]}
pl= pd.DataFrame(pelicula)
print(pl)