ingreso = 1000

gasto = 800


if ingreso >= 1000:
    if ingreso - gasto < 0:
        print("estas en perdida")
    elif ingreso - gasto > 300:
        print("estas bien")
    else:
        print("estas gastando")