import json as j
import re as re

with open("result.json") as file:
    archivo = j.load(file)

    informacion = ""
    print("procesando .....")
    cont = len(archivo["messages"])
    sumador = 0
    print("0  de ", cont)
    for a in archivo["messages"]:
        sumador += 1
        print(sumador, " de ", cont)
        # Eliminamos cadenas vacias o vectores que contienen publicidad
        # tambien algunos caracteres como monedas o porcentaje ademas de convertir todo en minuscula

        if not str(a["text"]).__eq__("") and not str(a["text"]).__contains__("[") and not str(a["text"]).__contains__("]") and not str(a["text"]).__contains__("{") and not str(a["text"]).__contains__("}"):

            # eliminamos cualquier tipo de url que pueda contener el texto
            # eliminamos numeros y signos de puntuación
            # y por ultimo eliminamos aquellas lineas de texto menores a 3 caracteres
            if not re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', a["text"]).__eq__("") and str(len(a["text"]) > 1):
                aux = str(a["text"]).replace("$", "").replace("#", "").replace(
                    "%", "").replace("€", "").replace("\n", "").replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("?", "").replace("¿", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "").replace("!", "").replace("*", "").replace("/", "").replace("@", "").replace("=", "").replace("+", "").replace("\"", "").replace("\'", "").replace("(", "").replace(")", "").lower().strip().lstrip().rstrip()
                if len(aux) > 2:
                    informacion += aux.strip().lstrip().rstrip() + "\n"

        # eliminamos los emoticones

        eliminar_emo = re.compile("["
                                  u"\U00000091-\U0001FFFF"  # emoticones
                                  "]+", flags=re.UNICODE)
        informacion = eliminar_emo.sub(r'', informacion)

    # se guarda en un nuevo archivo el texto en su primera etapa de preproceso
    with open("salida.txt", "w") as file:
        file.write(informacion)
    print("Tarea finalizada ")
