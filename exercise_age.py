def age():
    """
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """
    edad_anos = 25

    en_meses = edad_anos*12
    en_dias = edad_anos*365
    en_horas = en_dias*24
    en_minutos = en_horas*60

    print(en_meses)
    print(en_dias)
    print(en_horas)
    print(en_minutos)
age()

