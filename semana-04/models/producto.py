class Producto:
    """Representa un producto en el inventario."""
    
    def __init__(self, sku, nombre, categoria, precio, stock, stock_minimo):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)
        self.stock_minimo = int(stock_minimo)
    
    def necesita_reorden(self):
        """Determina si el producto necesita ser reordenado."""
        return self.stock < self.stock_minimo
    
    def unidades_faltantes(self):
        """Calcula cuántas unidades faltan para alcanzar el stock mínimo."""
        if self.necesita_reorden():
            return self.stock_minimo - self.stock
        return 0
    
    def valor_inventario(self):
        """Calcula el valor monetario del inventario actual."""
        return self.precio * self.stock
    
    def __str__(self):
        """Representación legible para usuarios."""
        estado = "[REORDEN]" if self.necesita_reorden() else "[OK]"
        return f"{estado} {self.sku}: {self.nombre} - Stock: {self.stock}/{self.stock_minimo}"
    
    def __repr__(self):
        """Representación técnica para desarrolladores."""
        return (f"Producto('{self.sku}', '{self.nombre}', '{self.categoria}', "
                f"{self.precio}, {self.stock}, {self.stock_minimo})")