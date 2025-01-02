from system import RailwaySystem, Train, Switch, Simulation  # Importar clases y métodos
print("clases cargadas")
from ver_vias import draw_railway_network  # Importar la función de visualización
print("importado todo, creando sistema")



def init(station: list[str], trains: list[Train], sistema: RailwaySystem) -> tuple[RailwaySystem, dict[str, str]]:
    """Inicializa el sistema con estaciones, vías y trenes"""
    for i in station:
        sistema.tracks.add_station(i)
    print("estaciones creadas")

    sistema.tracks.add_bidirectional_track("A", "F", 2)
    sistema.tracks.add_bidirectional_track("F", "Y", 1)
    sistema.tracks.add_bidirectional_track("Y", "B", 2)
    sistema.tracks.add_track("C", "X", 1)
    sistema.tracks.add_track("X", "G", 1)
    sistema.tracks.add_track("G", "D", 2)
    sistema.tracks.add_track("Z", "E", 1)
    sistema.tracks.add_track("F", "G", 1)
    sistema.tracks.add_track("X", "Y", 1)
    sistema.tracks.add_track("Y", "Z", 1)
    sistema.tracks.add_track("E", "B", 1)
    print("vias creadas")
    
    trains_id = {}
    for i in trains:
        sistema.add_train(i)
        sistema.find_route(i.id)
        trains_id[i.id] = i.position
    return sistema, trains_id
def run():
    simulation.run(30)

if __name__ == "__main__":
    print("importado todo, creando sistema")
    system = RailwaySystem()
    print("sistema creado")

    station = ["A", "B", "C", "D", "E", "F", "G", "X", "Y", "Z"]  #Añadir estaciones y vías
    trenes = [Train("T5", "A", "B"), Train("T6", "A", "Y")]
    system, train_id = init(station, trenes, system)

    simulation = Simulation(system)
    run()
      
    draw_railway_network(system.tracks.network, train_id)  # Representar visualmente las vías
