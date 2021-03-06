def conversion(unit1, unit2, value):
    # function for converting unit
    if unit1 == unit2:
        return value

    if unit1 == 'sq ft':
        if unit2 == 'sq m':
            return value / 10.7639
        elif unit2 == 'cent':
            return value / 435.599
        elif unit2 == 'ares':
            return value / 1076.39

    elif unit1 == 'sq m':
        if unit2 == 'sq ft':
            return value * 10.7639
        elif unit2 == 'cent':
            return value / 40.46856
        elif unit2 == 'ares':
            return value / 100

    elif unit1 == 'cent':
        if unit2 == 'sq m':
            return value * 40.46856
        elif unit2 == 'sq ft':
            return value * 435.599
        elif unit2 == 'ares':
            return value / 2.47067
    else:
        if unit2 == 'sq m':
            return value * 100
        elif unit2 == 'sq ft':
            return value * 1076.39
        elif unit2 == 'cent':
            return value * 2.47067
