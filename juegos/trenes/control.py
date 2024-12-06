from system import RailwaySystem, Train, Switch, Simulation  # Importar clases y métodos
from ver_vias import draw_railway_network  # Importar la función de visualización

# Crear sistema ferroviario
system = RailwaySystem()
print("sistema creado")

# Añadir estaciones y vías
station = ["A", "B", "C", "D", "E", "F", "G", "X", "Y", "Z"]
for i in station:
    system.tracks.add_station(i)
print("estaciones creadas")

system.tracks.add_bidirectional_track("A", "F", 2)
system.tracks.add_bidirectional_track("F", "Y", 1)
system.tracks.add_bidirectional_track("Y", "B", 2)
system.tracks.add_track("C", "X", 1)
system.tracks.add_track("X", "G", 1)
system.tracks.add_track("G", "D", 2)
system.tracks.add_track("Z", "E", 1)
system.tracks.add_track("F", "G", 1)
system.tracks.add_track("X", "Y", 1)
system.tracks.add_track("Y", "Z", 1)
system.tracks.add_track("E", "B", 1)
print("vias creadas")

# Añadir un switch
switch = Switch(id="S1", connections=[("F", "Y"), ("F", "G")])
system.add_switch(switch)

train1 = Train("T1", "A", "B")
train2 = Train(id="T2", position="B", destination="A")

system.add_train(train1)
system.find_route(train1.id)
system.add_train(train2)
system.find_route(train2.id)

simulation = Simulation(system)

# Mover trenes
simulation.run(30)

# Representar visualmente las vías
draw_railway_network(system.tracks.network, {"T2": train2.position, "T1": train1.position})

