
import numpy as np
altura = [1.5, 1.6, 1.7]
peso = [34, 65, 87]
nalt = np.array(altura)
npeso = np.array(peso)
imc = (nalt/npeso)**2
#ja vai pegar o 1 elemento com o 1 elemento... nalt[0]/npeso[0]

