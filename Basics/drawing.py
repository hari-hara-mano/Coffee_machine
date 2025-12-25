from prettytable import PrettyTable 

t=PrettyTable()
#table.add_column(" My name ",["manohar", "manu", "pandu", "mano", "kungfupanda", "jaan", "chinnu", "handsome"])
#table.add_row(["Harika" , "Chiinutalli" , "bujji_konda","bangaru_konda", "cutie_pie", "Semma_hot"])

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