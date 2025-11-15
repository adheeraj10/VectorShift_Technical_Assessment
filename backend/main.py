from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from collections import defaultdict, deque

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # development only; tighten for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
async def parse_pipeline(request: Request):
    """
    Expects JSON body: { nodes: [...], edges: [...] }
    edges should be objects with 'source' and 'target' (node ids)
    """
    body = await request.json()
    nodes = body.get('nodes', [])
    edges = body.get('edges', [])

    num_nodes = len(nodes)
    num_edges = len(edges)

    # Build adjacency list for node ids
    adj = defaultdict(list)
    indeg = defaultdict(int)
    node_ids = set()

    for n in nodes:
        nid = n.get('id')
        if nid is not None:
            node_ids.add(nid)
            indeg[nid] = 0

    # Add edges (assume edge objects contain 'source' and 'target' which are node ids)
    for e in edges:
        src = e.get('source')
        tgt = e.get('target')
        if src is None or tgt is None:
            # Sometimes reactflow edges include handle ids; you can refine normalization here
            continue
        # normalize if user included handle suffixes (like 'nodeId' or 'nodeId.handle')
        # Keep them as-is for now, assuming pipeline uses node ids
        adj[src].append(tgt)
        indeg[tgt] = indeg.get(tgt, 0) + 1

    # Kahn's algorithm to detect if graph is acyclic
    q = deque([n for n in node_ids if indeg.get(n, 0) == 0])
    visited = 0
    while q:
        u = q.popleft()
        visited += 1
        for v in adj.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    is_dag = (visited == len(node_ids))

    return {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': is_dag}
