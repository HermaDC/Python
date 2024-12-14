import networkx as nx
import time
from typing import List, Tuple


class RailwayTracks:
    def __init__(self):
        """Inicializa la red ferroviaria como un grafo dirigido."""
        self.network = nx.DiGraph()

    def add_station(self, name: str):
        """Añade una estación al sistema ferroviario."""
        if name in self.network:
            raise ValueError(f"Station {name} already exists!")
        self.network.add_node(name)

    def add_bidirectional_track(self, start: str, end: str, length: float):
        """
        Añade una vía bidireccional entre dos estaciones.
        """
        if start == end:
            raise ValueError("A track cannot connect a station to itself.")
        self.network.add_edge(start, end, length=length)  # De A a B
        self.network.add_edge(end, start, length=length)  # De B a A

    def add_track(self, start: str, end: str, length: float):
        """
        Añade una vía unidireccional entre dos estaciones.
        """
        if start == end:
            raise ValueError("A track cannot connect a station to itself.")
        self.network.add_edge(start, end, length=length)

    def __repr__(self):
        """Representación visual de las estaciones y conexiones."""
        return f"Railway Tracks: {self.network.nodes} with {len(self.network.edges)} tracks."


class Train:
    def __init__(self, id: str, position: str, destination: str):
        """
        Inicializa un tren con un ID, posición y destino.
        """
        if not position or not destination:
            raise ValueError("ID, position, and destination must be provided.")
        self.id = id
        self.position = position
        self.destination = destination
        self.route = []
        self.speed = 1  # Unidades por segundo

    def __repr__(self):
        """Representación del tren."""
        return f"Train({self.id}, Position: {self.position}, Destination: {self.destination})"


class Switch:
    def __init__(self, id: str, connections: List[Tuple[str, str]]):
        """
        Inicializa un switch con conexiones posibles.
        """
        if not connections:
            raise ValueError("Switch must have at least one connection.")
        self.id = id
        self.connections = connections
        self.current_connection = connections[0]

    def switch(self, to: Tuple[str, str]):
        """Cambia la conexión activa del switch."""
        if to not in self.connections:
            raise ValueError(f"Invalid connection for this switch: {to}")
        self.current_connection = to

    def __repr__(self):
        """Representación del switch."""
        return f"Switch({self.id}, Current: {self.current_connection})"


class RailwaySystem:
    def __init__(self):
        """Inicializa el sistema ferroviario."""
        self.tracks = RailwayTracks()
        self.trains = {}
        self.switches = {}

    def add_switch(self, switch: Switch):
        """Añade un switch al sistema ferroviario."""
        self.switches[switch.id] = switch

    def add_train(self, train: Train):
        """Añade un tren al sistema ferroviario."""
        self.trains[train.id] = train

    def find_route(self, train_id: str):
        """
        Encuentra la ruta más corta para un tren.
        """
        train = self.trains.get(train_id)
        if not train:
            raise ValueError(f"Train with ID {train_id} does not exist.")
        train.route = nx.shortest_path(
            self.tracks.network,
            train.position,
            train.destination,
            weight="length"
        )
        print(f"Train {train_id} route: {train.route}")

    def move_train(self, train_id: str, time_step: float = 1.0):
        """
        Mueve un tren a la siguiente estación de su ruta.
        """
        train = self.trains.get(train_id)
        if not train:
            raise ValueError(f"Train with ID {train_id} does not exist.")
        if not train.route:
            print(f"Train {train_id} has no route!")
            return

        next_station = train.route.pop(0)
        print(f"Train {train_id} moving from {train.position} to {next_station}")
        time.sleep(time_step)  # Simula tiempo real
        train.position = next_station


class Simulation:
    def __init__(self, system: RailwaySystem):
        """Inicializa la simulación para el sistema ferroviario."""
        self.system = system

    def run(self, steps: int, time_step: float = 1.0):
        """Ejecuta la simulación en intervalos de tiempo."""
        for _ in range(steps):
            for train_id in self.system.trains:
                if self.system.trains[train_id].position != self.system.trains[train_id].destination:
                    self.system.move_train(train_id, time_step)
                
            time.sleep(0.2)  