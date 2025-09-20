class TransformarPrecio:
  def transformar(self, precio_str):
    return float(precio_str.replace('€', '').replace(',', '').replace('$', '').replace('£', ''))