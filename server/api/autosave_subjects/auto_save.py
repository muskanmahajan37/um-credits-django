import requests

ADRESS_IP = "127.0.0.1"
PORT = 8000

list_subjects = [
    {"code": "0001", "name": "TECNOLOGIA CIENCIA Y SOCIEDAD", "credits": "3", "year": "1"},
    {"code": "0002", "name": "QUIMICA GENERAL", "credits": "4", "year": "1"},
    {"code": "0003", "name": "CALCULO I", "credits": "3", "year": "1"},
    {"code": "0004", "name": "CALCULO II", "credits": "3", "year": "1"},
    {"code": "0005", "name": "SISTEMAS DE REPRESENTACION", "credits": "3", "year": "1"},
    {"code": "2025", "name": "ANALISIS DE SISTEMAS I", "credits": "6", "year": "1"},
    {"code": "0007", "name": "ALGEBRA Y GEOMETRIA ANALITICA", "credits": "5", "year": "1"},
    {"code": "0008", "name": "INGLES TECNICO", "credits": "4", "year": "1"},
    {"code": "0009", "name": "INFORMATICA", "credits": "7", "year": "1"},
    {"code": "2031", "name": "ANALISIS DE SISTEMAS II", "credits": "4", "year": "2"},
    {"code": "2023", "name": "ARQUITECTURA DE COMPUTADORAS", "credits": "3", "year": "2"},
    {"code": "2040", "name": "DISEÑO DE BASES DE DATOS I (*)", "credits": "5", "year": "2"},
    {"code": "2022", "name": "MATEMATICA DISCRETA Y DISEÑO LOGICO (*)", "credits": "3", "year": "2"},
    {"code": "2032", "name": "REDES DE DATOS", "credits": "6", "year": "2"},
    {"code": "2027", "name": "ALGEBRA LINEAL", "credits": "3", "year": "2"},
    {"code": "2024", "name": "ESTADISTICA APLICADA I (*)", "credits": "4", "year": "2"},
    {"code": "2020", "name": "FISICA", "credits": "5", "year": "2"},
    {"code": "2026", "name": "SISTEMAS OPERATIVOS", "credits": "4", "year": "2"},
    {"code": "2028", "name": "COMPUTACION (*)", "credits": "6", "year": "2"},
    {"code": "2030", "name": "ANALISIS NUMERICO", "credits": "5", "year": "3"},
    {"code": "2035", "name": "AUTOMATAS Y GRAMATICAS", "credits": "3", "year": "3"},
    {"code": "2033", "name": "ESTADISTICA APLICADA II", "credits": "3", "year": "3"},
    {"code": "2043", "name": "ORGANIZACION", "credits": "3", "year": "3"},
    {"code": "2054", "name": "DISEÑO DE BASES DE DATOS II", "credits": "5", "year": "3"},
    {"code": "2046", "name": "ECONOMIA", "credits": "3", "year": "3"},
    {"code": "2036", "name": "DISEÑO DE SISTEMAS", "credits": "5", "year": "3"},
    {"code": "2037", "name": "COMUNICACION DE DATOS", "credits": "3", "year": "3"},
    {"code": "2038", "name": "PROGRAMACION", "credits": "4", "year": "3"},
    {"code": "2034", "name": "COMPUTACION II", "credits": "6", "year": "3"},
    {"code": "2041", "name": "INGENIERIA DE SOFTWARE", "credits": "5", "year": "4"},
    {"code": "2044", "name": "SEGURIDAD INFORMATICA I", "credits": "5", "year": "4"},
    {"code": "2042", "name": "TELEINFORMATICA", "credits": "5", "year": "4"},
    {"code": "2404", "name": "TRABAJO INTEGRADOR FINAL 1", "credits": "3", "year": "4"},
    {"code": "2048", "name": "FORMULACION Y EVALUACION DE PROYECTOS", "credits": "4", "year": "4"},
    {"code": "2080", "name": "INGENIERIA DE SOFTWARE APLICADA", "credits": "4", "year": "4"},
    {"code": "2055", "name": "INTELIGENCIA ARTIFICIAL", "credits": "4", "year": "4"},
    {"code": "2047", "name": "INVESTIGACION OPERATIVA", "credits": "4", "year": "4"},
    {"code": "2409", "name": "TRABAJO INTEGRADOR FINAL 2", "credits": "3", "year": "4"},
    {"code": "2049", "name": "PROGRAMACION II", "credits": "6", "year": "4"},
    {"code": "2501", "name": "ASEGURAMIENTO DE CALIDAD DEL SOFTWARE", "credits": "4", "year": "5"},
    {"code": "2502", "name": "GESTION DE CALIDAD Y MEDIO AMBIENTE", "credits": "4", "year": "5"},
    {"code": "2503", "name": "HIGIENE Y SEGURIDAD DEL TRABAJO", "credits": "3", "year": "5"},
    {"code": "2504", "name": "MODELOS Y SIMULACION", "credits": "3", "year": "5"},
    {"code": "2505", "name": "TRABAJO INTEGRADOR FINAL 3", "credits": "3", "year": "5"},
    {"code": "2506", "name": "SEGURIDAD INFORMATICA II", "credits": "4", "year": "5"},
    {"code": "2507", "name": "INGENIERIA DERECHO Y ETICA PROFESIONAL", "credits": "3", "year": "5"},
    {"code": "2508", "name": "AUDITORIA DE SISTEMAS", "credits": "4", "year": "5"},
    {"code": "2509", "name": "PLANEAMIENTO Y GESTION DE EMPRESAS (*)", "credits": "5", "year": "5"},
    {"code": "2510", "name": "TRABAJO INTEGRADOR FINAL 4", "credits": "3", "year": "5"},
    {"code": "2500", "name": "PRACTICA PROFESIONAL", "credits": "0", "year": "5"}
]

status_codes = []

for i in list_subjects:
    status_codes.append(requests.post(f'http://{ADRESS_IP}:{PORT}/api/subjects/', data=i))

print(status_codes)
