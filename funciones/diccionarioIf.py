DISFRAZ_DEFECTO = "PECERA"

adversario = input("Quien tienes enfrente ")
# if adversario.lower() == "loki":
#     misterio = "Lady Loki"
# elif adversario.lower() == "hulk":
#     misterio = "Thanos"
# elif adversario.lower() == "thor":
#     misterio = "Odin"
# elif adversario.lower() == "superman":
#     misterio = "Darkseid"
# else:
#     misterio = DISFRAZ_DEFECTO

disfraces_misterio={
       "superman":"Darkseid",
       "thor":"Odin",
       "loki":"Lady Loki",
       "hulk":"Thanos"
    }
print(disfraces_misterio.get(adversario.lower(), DISFRAZ_DEFECTO))