"""
Para realizar las gráfica de precios mensuales
"""

def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.
    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    from datetime import datetime

    def obtain_axix_plotting():
        monthly_prices = pd.read_csv('data_lake/business/precios-mensuales.csv', header=0)
        monthly_prices['Fecha'] = pd.to_datetime(monthly_prices['Fecha'], format='%Y-%m-%d')
        X = monthly_prices['Fecha']
        y = monthly_prices['Precio']
        return X,y
        
    def plotting(X,y): 
        plt.figure(figsize=(15, 6))
        plt.plot(X, y, 'b', label='Prom. precio')
        plt.title('Promedio de Precio Mensual de Energía')
        plt.xlabel('Fecha')
        plt.ylabel('Precio')
        plt.legend()
        plt.xticks(rotation="vertical")
        plt.savefig("data_lake/business/reports/figures/monthly_prices.png")

    X, y = obtain_axix_plotting()
    plotting(X, y)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    make_monthly_prices_plot()