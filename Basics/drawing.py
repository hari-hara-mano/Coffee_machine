from prettytable import PrettyTable 

t=PrettyTable()


t.field_names=[" Pokemon name " , " Type "]
t.add_rows([
    ["Pikachu ", "Electric"],
    ["Squiter", "Water"],
    ["Charmander", "Fire"]
])
print(t)

t.add_column(" POKEMAN NAME ", ["PIKACHU","SQUITTER","CHARMANDER"],align="l")
t.add_column("TYPE", ["ELCTRIC", "WATER", "FIRE"], align="l")

print(t)
