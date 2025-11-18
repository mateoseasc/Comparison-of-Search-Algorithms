def bfs_with_count(grafo, inicio, meta):
    from collections import deque
    
    cola = deque([inicio])
    visitados = set([inicio])
    padre = {inicio: None}
    nodos_explorados = 0

    while cola:
        actual = cola.popleft()
        nodos_explorados += 1

        if actual == meta:
            break

        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                padre[vecino] = actual
                cola.append(vecino)

    if meta not in padre:
        return None, nodos_explorados

    camino = []
    nodo = meta
    while nodo is not None:
        camino.append(nodo)
        nodo = padre[nodo]
    camino.reverse()

    return camino, nodos_explorados

def dijkstra_with_count(G, inicio, meta):
    import heapq
    pq = [(0, inicio, [inicio])]
    visitados = set()
    nodos_explorados = 0

    while pq:
        costo, nodo, ruta = heapq.heappop(pq)

        if nodo in visitados:
            continue
        visitados.add(nodo)
        nodos_explorados += 1

        if nodo == meta:
            return ruta, costo, nodos_explorados

        for vecino in G.neighbors(nodo):
            if vecino not in visitados:
                peso = G[nodo][vecino]["weight"]
                heapq.heappush(pq, (costo + peso, vecino, ruta + [vecino]))

    return None, float("inf"), nodos_explorados

def a_star_with_count(G, inicio, meta):
    import heapq, math

    def h(G, nodo, meta):
        R = 6371000

        lat1 = math.radians(G.nodes[nodo]["y"])  
        lon1 = math.radians(G.nodes[nodo]["x"])
        lat2 = math.radians(G.nodes[meta]["y"])
        lon2 = math.radians(G.nodes[meta]["x"])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    pq = [(0, 0, inicio, [inicio])]
    visitados = set()
    nodos_explorados = 0

    while pq:
        f, g, actual, ruta = heapq.heappop(pq)

        if actual in visitados:
            continue
        visitados.add(actual)
        nodos_explorados += 1

        if actual == meta:
            return ruta, g, nodos_explorados

        for vecino, datos in G[actual].items():
            peso = datos["weight"]
            g_nuevo = g + peso
            f_nuevo = g_nuevo + h(G, vecino, meta)   

            heapq.heappush(pq, (f_nuevo, g_nuevo, vecino, ruta + [vecino]))

    return None, float("inf"), nodos_explorados

