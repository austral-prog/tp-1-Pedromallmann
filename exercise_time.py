def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    hora_completa = total_segundos // 3600
    minutos_restantes = (total_segundos % 3600)//60
    segundos_restantes = (total_segundos % 60)
    print(hora_completa)
    print(minutos_restantes)
    print(segundos_restantes)
time()
