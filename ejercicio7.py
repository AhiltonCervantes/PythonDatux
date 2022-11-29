class problema7():
    import requests
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    response.json()
    res=response.json()
    dolar_compra = res['compra']
    dolar_venta = res['venta']
    cantidad=float(input("ingrese la cantidad a comprar: "))
    print(cantidad*dolar_compra)