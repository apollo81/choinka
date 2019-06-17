list = [1,2,3,4]
nowa_lista = list.copy()

# lista zagniedzona

chamiea = ['proszek', 'ply', 'mydlo']
spozywcze = ['marchew', 'seler', 'ogorek']

zakupy_czerwiec = [chamiea, spozywcze]
zakupy_lipiec = copy.deepcopy(zakupy_czerwiec)
zakupy_lipiec[1][0] = 'rzodkiewka'

print(zakupy_lipiec)