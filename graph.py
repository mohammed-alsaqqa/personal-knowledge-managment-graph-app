from typing import Optional
import uuid


# The same as a node in a graph but called note because we are making a note app
class Note:
    def __init__(self, note_content, title) -> None:
        self.__title = title
        self.note_value = note_content
        self.__uuid = uuid.uuid4()

    def __str__(self) -> str:
        return self.__title

    def __hash__(self):
        return hash(self.__uuid)

    def __eq__(self, other) -> bool:
        if isinstance(other, Note):
            return self.__uuid == other.__uuid
        return NotImplemented

    def getId(self):
        return self.__uuid

    def getTitle(self):
        return self.__title

    def getValue(self):
        return self.note_value


class WeightedNoteGraph:
    def __init__(self) -> None:
        self.graph = {}

    # addVertex(vert) adds an instance of Vertex to the graph.
    def addNote(self, title, content=""):
        if self.getNoteByTitle(title) == None:
            self.graph[Note(content, title)] = {}
        else:
            raise KeyError("This vertex already exists.")

    # addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
    def addConnection(self, src_note, dest_note, weight=None):
        SOURCE = self.graph.get(src_note)
        DESTINATION = self.graph.get(dest_note)

        if (SOURCE == None) or (DESTINATION == None):
            return KeyError("Couldnt find one or both of the keys")

        SOURCE[dest_note] = weight

    # getVertex(vertKey) finds the vertex in the graph named vertKey.
    def getNoteByID(self, id) -> Optional[Note]:
        NOTE = list(filter(lambda note: str(note.getId()) == id, self.graph))
        return None if len(NOTE) < 1 else NOTE[0]

    # getVertex(vertKey) finds the vertex in the graph named vertKey.
    def getNoteByTitle(self, title) -> Optional[Note]:
        NOTE = list(filter(lambda note: note.getTitle() == title, self.graph))
        return None if len(NOTE) < 1 else NOTE[0]

    # getVertices() returns the list of all vertices in the graph.
    def getVertices(self):
        return self.graph

    def getConnected(self, note):
        return self.graph[note]

    # in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
    def has_vertex(self, note):
        return note in self.graph

    def __str__(self):
        string_value = ""
        for note in self.graph:
            string_value += f"{note} -----> {[str(N) + ', ' + str(self.graph[note][N]) for N in self.graph[note]]}\n"

        return string_value
    
    def generate_visualisations(self):
        pass


NOTEGRAPH = WeightedNoteGraph()
NOTEGRAPH.addNote(
    "Note-Taking",
    '### Note-Taking\n\nUsing graph data structures for note-taking enhances the organization and retrieval of information. Traditional linear note-taking methods often lead to fragmented and hard-to-navigate information. In contrast, graph-based note-taking allows each note to act as a node, with relationships between notes forming edges. This structure supports linking related concepts, topics, and ideas dynamically, reflecting the way knowledge and thoughts are interconnected.\n\nFor instance, a note about "Photosynthesis" can be linked to related notes on "Chlorophyll," "Plant Biology," and "Energy Conversion," creating a comprehensive network of information. This interconnected approach can be further explored through the concept of a [[Personal-Web]] and benefits from the underlying structure of a [[Graph-Data-Structure]].',
)
NOTEGRAPH.addNote(
    "Personal-Web",
    "### Personal-Web\n\nA personal-web is a digital representation of an individual's knowledge and interests, structured as a graph. It enables users to map their knowledge, track their learning journey, and visualize how various pieces of information relate to each other. This personal knowledge management system helps in creating a connected web of ideas, which can be invaluable for learning, brainstorming, and creative thinking.\n\nBy utilizing a [[Graph-Data-Structure]], users can effortlessly traverse through interconnected notes, gaining insights and discovering new connections they might have missed using linear or hierarchical systems. This method is particularly effective when combined with graph-based [[Note-Taking]] practices.",
)
NOTEGRAPH.addNote(
    "Graph-Data-Structure",
    "### Graph-Data-Structure\n\nGraph data structures consist of nodes (vertices) and edges, which can be used to model complex relationships and interactions. In the context of note-taking and personal knowledge management, graphs provide a flexible and powerful way to organize and access information. Each note can be a node, and links between notes can be edges, representing the relationships or connections between different pieces of information. \n\nThis approach mirrors the associative nature of human memory, making it easier to find and relate information. Additionally, graph databases and tools such as Neo4j, Roam Research, and Obsidian leverage this structure to provide efficient storage, querying, and visualization of interconnected data. This is particularly useful for creating a [[Personal-Web]] and enhancing [[Note-Taking]] methods.",
)
