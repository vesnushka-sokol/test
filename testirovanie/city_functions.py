def get_city_functions(land, stadt, population=''):
    if population:
        full_n = stadt.title() + ', ' + land.title() + ' - population ' + \
                 str(population)
    else:
        full_n = stadt.title() + ', ' + land.title()
    return full_n
