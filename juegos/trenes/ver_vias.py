import matplotlib.pyplot as plt
import networkx as nx

def draw_railway_network(network, train_positions: dict=None):
    """
    Dibuja la red ferroviaria y las posiciones de los trenes.
    
    Args:
        network (networkx.Graph): La red ferroviaria representada como un grafo.
        train_positions (dict): Diccionario con las posiciones actuales de los trenes.
                                Ejemplo: {"T1": "A", "T2": "B"}
    """
    positions = nx.spring_layout(network, seed=42)  # Calcula las posiciones de los nodos

    plt.clf()  # Limpia la figura anterior

    # Dibuja nodos y aristas
    nx.draw(network, positions, with_labels=True, node_size=700, node_color="lightblue", font_weight="bold")

    # Dibuja los trenes
    for train_id, position in train_positions.items():
        x, y = positions[position]
        plt.text(x, y + 0.05, train_id, color="red", fontsize=12, ha="center", va="center", bbox=dict(facecolor="white", alpha=0.6))

    plt.title("Railway Network")
    plt.show()
