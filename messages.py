def siu_success_message(latency):
    return f"El siu guaraní ha respondido <b>exitosamente</b> con una latencia de <b>{latency}ms</b>"


def siu_failure_message(latency):
    return f"Falló la solicitud al siu guaraní con una latencia de <b>{latency}ms</b>"


def help_message():
    return f"<b>infoUNObot</b> te brinda información necesaria sobre la Universidad Nacional del Oeste, desde el estado del siu o el campus, hasta fechas importantes o links utiles.<br/><b>/help</b> - Muestra este mensaje.\n<b>/siu</b> - Obtiene información del siu para saber el estado del mismo y su latencia.<br/><b>/links</b> - Te devuelve un listado de links utiles sobre la carrera (grupos, comunidades, etc).<br/><b>/calendar</b> - Te muestra las fechas importantes del calendario académico de la Universidad.<br/><br/> Este bot fue posible y llevado a cabo gracias a GNUno, cualquier consulta o pregunta hacela aquí: <inserte contacto de gnuno>."