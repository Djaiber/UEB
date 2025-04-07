# Advanced Wars Clone

![Game Banner](docs/images/banner.png)

A Java-based web implementation of the classic turn-based strategy game featuring advanced pathfinding and skill progression systems.

## Table of Contents
- [Core Features](#-core-features)
- [Technical Architecture](#-technical-architecture)
- [Algorithm Details](#-algorithm-details)
- [Installation](#-installation)
- [Database Setup](#-database-setup)
- [API Documentation](#-api-documentation)
- [License](#-license)

## 🎮 Core Features

### Pathfinding System
```java
// BFS implementation in Pathfinder.java
public List<Position> calculateMoves(Unit unit, GameMap map) {
    Queue<PathNode> queue = new LinkedList<>();
    boolean[][] visited = new boolean[map.getWidth()][map.getHeight()];
    List<Position> validMoves = new ArrayList<>();
    
    queue.add(new PathNode(unit.getPosition(), unit.getMovementRange()));
    visited[unit.getX()][unit.getY()] = true;
    
    while (!queue.isEmpty()) {
        PathNode current = queue.poll();
        validMoves.add(current.position);
        
        for (Position neighbor : map.getNeighbors(current.position)) {
            if (isValidMove(neighbor, unit) && !visited[neighbor.x][neighbor.y]) {
                queue.add(new PathNode(neighbor, current.range - 1));
                visited[neighbor.x][neighbor.y] = true;
            }
        }
    }
    return validMoves;
}
