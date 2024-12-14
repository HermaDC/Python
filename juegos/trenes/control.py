from system import RailwaySystem, Train, Switch, Simulation  # Importar clases y métodos
print("clases cargadas")
from ver_vias import draw_railway_network  # Importar la función de visualización
print("importado todo, creando sistema")



def init(station, trains) -> None:
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
    
    id = {}
    for i in trains:
        system.add_train(i)
        system.find_route(i.id)
        id[i.id] = i.position
def run():
    simulation.run(30)

if __name__ == "__main__":
    print("importado todo, creando sistema")
    system = RailwaySystem()
    print("sistema creado")

    station = ["A", "B", "C", "D", "E", "F", "G", "X", "Y", "Z"]  #Añadir estaciones y vías
    trenes = [Train("T5", "A", "B"), Train("T6", "A", "Y")]
    init(station, trenes)

    simulation = Simulation(system)
    run()
      
    draw_railway_network(system.tracks.network, id)  # Representar visualmente las vías