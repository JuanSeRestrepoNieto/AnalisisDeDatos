import numpy as np
import pandas as pd

class TransformarKilometraje:
  def transformar(self, valor, unidad='km'):
    if pd.isna(valor):
      return np.nan
    valor = str(valor).replace(',', '').strip()
    if unidad == 'millas' or 'millas' in valor.lower() or 'miles' in valor.lower():
      numero = float(valor.lower().replace('millas', '').replace('miles', '').strip())
      return numero * 1.60934  # Convertir millas a kilómetros
    else:
      numero = float(valor.lower().replace('km', '').strip())
      return numero