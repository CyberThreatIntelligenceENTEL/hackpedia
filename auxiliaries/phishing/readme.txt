Nota: Versión 1, uso limitado a python y sistemas unix que soporten curl.


Verficar que se cumplan dependencias: 
- Pandas
- Warnings

Uso:
python3 check_status.py [nombre_archivo_excel]
* Ingresar nombre de hoja desde la cual se extraerán los datos*

Ejemplo:

user@threatintell:~/main$ python3 check_status.py phishing_2022.xlsx
Hojas disponibles en el libro: ['1', 'bbddd', 'Enero 2022']

Debe escoger una hoja para extraer sus datos: Enero 2022

|> Code Status: 000 --> For Site: https://www.sitephishing-com.xyz/bancaenlinea.php
---REDACTED---
|> Code Status: 200 --> For Site: https://www.sitephishing-com.xyz/mercadocompras-phish-com.php

Códigos de estado:

000: Sin respuesta o "dead".
200: Disponible - en línea.
301: URL ha sido cambiada permanentemente (de http a https, puede redireccionar código de estado 404 o 404).
403: Petición recibida, respuesta rechazada.
404: Recurso no disponible.

Mas estados en https://es.wikipedia.org/wiki/Anexo:C%C3%B3digos_de_estado_HTTP