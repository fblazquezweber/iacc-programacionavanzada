def asignar_beneficios(antiguedad):
    if antiguedad >= 5:
        return "Bono anual y 5 días adicionales de vacaciones"
    elif antiguedad >= 3:
        return "Bono anual"
    else:
        return "Sin beneficios adicionales"