'''=============================================================================
 AUTOR              : Camilo Andres Hernandez Soler
 GRUPO              : 213022_711
 PROGRAMA           : ECBTI
 CODIGO FUENTE      : Autoria propia

 FECHA (dd/mm/aaaa) : 26/05/2026
============================================================================='''
def calificacion(id,duracion,eventos):
    if duracion > 180 and eventos > 8:
        etiqueta="Alto"
    elif duracion < 60 or eventos < 3:
        etiqueta ="Bajo"
    else:
        etiqueta="Medio"

    print(f"{id:<22} {etiqueta:<12}")

def main():
    base_datos = [
        ["042_Pixel3", 200, 10],
        ["123_iPhone8", 181, 9],
        ["256_GalaxyS9", 180, 8],
        ["307_Pixel4a", 181, 8],
        ["410_MotoG7", 30, 5],
        ["555_Nokia7", 120, 2],
        ["608_Xperia5", 0, 0],
        ["711_OnePlus7", 90, 4],
        ["825_GalaxyA50", 120, 5],
        ["930_PocoX3", 250, 20],
        ["004_LGG7", 60, 3],
        ["999_Zenfone5", 59, 10]
    ]

    print("=" * 40)
    print(f"{'ID':<22} {'Clasificación':<12}")
    print("=" * 40)

    for i in range(len(base_datos)):
        calificacion(base_datos[i][0],base_datos[i][1],base_datos[i][2])
main()
