#### Running The Application

- Make a python Virtual Venv: `python -m venv .venv`
- Install the requirements: `pip install -r requirements.txt`
- Run the application: `uvicorn main:app --reload`

### Problem Overview

**Personal Knowledge Management and Note-Taking:**

Managing personal knowledge efficiently is crucial for productivity and information retention. Traditional hierarchical note-taking methods and applications often fall short as they do not align with the associative nature of human memory. Traditional applications have a hierarchical structure where notes are nested within each other creating a Tree data structure. This imposes a rigid organization, which can hinder the discovery of relationships between different pieces of information.

**Challenges with Hierarchical Notes:**

1. **Rigid Structure:** Traditional hierarchical note systems enforce a Tree structure (i.e. top-down approach), which can be limiting.
2. **Poor Relationship Mapping:** Hierarchical systems fail to capture the complex, interlinked nature of knowledge, leading to isolated information units.
3. **Difficulty in Retrieval:** Finding related notes often requires navigating through multiple levels of hierarchy, which is inefficient. A simple example is a file nested deeply within a file system.

### Proposed Solution

**Bidirectional and Multidirectional Weighted Graphs:**

Utilizing graph structures for note-taking addresses the limitations of hierarchical systems by enabling dynamic, flexible, and intuitive knowledge representation. In this approach, notes are represented as nodes, and relationships between them are represented as edges. The edges can be weighted to indicate the strength or frequency of the connections.

### Benefits of Graph-Based Note-Taking

1. **Enhanced Connectivity:** Reflects the natural, associative way the human brain works, promoting better information retention and retrieval.
2. **Dynamic Relationships:** Facilitates the discovery of new relationships and connections between different pieces of information.
3. **Improved Navigation:** Enables efficient traversal and retrieval of related notes using graph algorithms like DFS and BFS.

### Utilizing Graph Algorithms

**Depth-First Search (DFS):**

- **Application:** DFS can be used to explore all notes starting from a given note. This is useful for understanding the depth of knowledge and uncovering hidden connections.
- **Advantages:** Helps in finding all related notes, detecting cycles, and exploring deeply interconnected information. This utility helps users who may want to revert back temporarily to a hierarchical structure.

**Breadth-First Search (BFS):**

- **Application:** BFS can be employed to traverse notes level by level. This is beneficial for discovering immediate connections and relationships between notes.
- **Advantages:** Useful for finding the shortest path between notes and for level-order exploration of knowledge.

**Example Implementation:**

Consider a simple note-taking application where users can create notes and link them to other notes. Each reference from one note to another adds an edge to the graph, with the weight of the edge representing the number of times one note references the other.
The "Guide" sample note in the application explains how the application works in more detail.

#### Key Features:

1. **Automatic Graph Updates:** Whenever a note references another note, an edge is automatically added or updated in the graph.
2. **Weighted Edges:** The weight of the edge corresponds to the number of references (i.e. frequency of occurrence), allowing users to understand the strength of the relationships.
3. **Bidirectional and Multidirectional Links:** Notes can have multiple incoming (i.e. other notes that reference that note.) and outgoing links (i.e. other notes that are referenced in the current note.), reflecting the complex nature of knowledge.
4. **Visualization Tools**: The application has a "Graph View" that shows how all notes are interconnected. It also provides a tabular representation of connected notes for each note.

### Graph Example

The provided image illustrates a simple graph generated by our note-taking application. Here are the components of the graph:

- **Nodes:** Represent individual notes such as "Guide," "Note-Taking," "Graph-Data-Structure," and "Personal-Web."
- **Edges:** Represent references between notes, with the weights indicating the number of references.

![image](https://github.com/mohammed-alsaqqa/personal-knowledge-managment-graph-app/assets/106604798/bf543327-fc8e-4374-a1aa-d65af713fa29)


### Conclusion

Transforming traditional hierarchical note-taking into a graph-based system significantly enhances personal knowledge management. By leveraging bidirectional and multidirectional weighted graphs, users can create a more intuitive, flexible, and connected knowledge base. This approach not only aligns better with how the human brain works but also provides powerful tools for navigating and organizing information.
