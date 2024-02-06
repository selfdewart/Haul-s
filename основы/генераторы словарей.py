
supports = {
    'Alinur': 20,
    'Sherdos': 20
}

# [область переменной, цикл, условие]
# {область переменных, цикл, условие}

new_values = {key: value+3 for key, value in supports.items()}
print(new_values)