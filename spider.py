from curl_cffi import requests as cureq
from selectolax.parser import HTMLParser
from utiles import BuscadorLocalizaciones


def obtener_html_localizacion(nombre_ciudad: str) -> str:
    """
    Busca la ciudad con BuscadorLocalizaciones y devuelve el HTML de su página.
    """
    buscador = BuscadorLocalizaciones(nombre_ciudad)

    if not buscador.obtener_respuesta():
        raise ValueError(f"No se pudo obtener datos para la ciudad: {nombre_ciudad}")

    resultados = buscador.obtener_datos()
    url = resultados[0]["url"]

    respuesta = cureq.get(url, impersonate="chrome")
    return respuesta.text


def extraer_datos(html: str) -> dict:
    """
    A partir del HTML extrae los datos meteorológicos principales.
    """
    tree = HTMLParser(html)

    # Temperatura principal
    try:
        temperatura = tree.css_first("div.temp").text().strip()
    except Exception as e:
        print("No se pudo obtener la temperatura")

    # Otros valores (sensación real, viento, ráfagas...)
    valores = []
    contenedores = tree.css(
        "div.cur-con-weather-card__panel.details-container div.spaced-content.detail"
    )

    for nodo in contenedores:
        valor = nodo.css_first(".value").text().strip()
        valores.append(valor)

    return {
        "temperatura": temperatura,
        "viento": valores[0] if len(valores) > 0 else None,
        "rafagas": valores[1] if len(valores) > 1 else None,
        "calidad_viento": valores[2] if len(valores) > 2 else None,
    }


if __name__ == "__main__":
    html = obtener_html_localizacion("miami")
    datos = extraer_datos(html)

    print("Temperatura:", datos["temperatura"])
    print("Viento:", datos["viento"])
    print("Ráfagas:", datos["rafagas"])
    print("Calidad del viento:", datos["calidad_viento"])
