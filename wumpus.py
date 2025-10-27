# --- Wumpus World Simulation ---

class WumpusWorld:
    def __init__(self, size, wumpus, pits, gold):
        self.size = size
        self.wumpus = wumpus
        self.pits = pits
        self.gold = gold

    def adjacent_cells(self, cell):
        """Return adjacent cells (up, down, left, right) within bounds."""
        x, y = cell
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= self.size and 1 <= ny <= self.size:
                neighbors.append((nx, ny))
        return neighbors

    # --- Percepts ---
    def stench(self, cell):
        """True if Wumpus is adjacent to the cell."""
        return self.wumpus in self.adjacent_cells(cell)

    def breeze(self, cell):
        """True if any pit is adjacent to the cell."""
        for pit in self.pits:
            if pit in self.adjacent_cells(cell):
                return True
        return False

    def glitter(self, cell):
        """True if gold is in the same cell."""
        return cell == self.gold

    # --- Safety Check ---
    def safe(self, cell):
        """True if no pit, no wumpus, and no percepts indicating danger."""
        if cell == self.wumpus or cell in self.pits:
            return False
        return not (self.stench(cell) or self.breeze(cell))


# --- Example Usage ---
if __name__ == "__main__":
    # Define world configuration
    size = 4
    wumpus = (2, 3)
    pits = [(5, 1), (4, 4)]  # Note: (5,1) is outside 4x4 grid, ignored.
    pits = [p for p in pits if 1 <= p[0] <= size and 1 <= p[1] <= size]
    gold = (2, 2)

    world = WumpusWorld(size, wumpus, pits, gold)

    # Example queries
    print("?- stench((2,2))")
    print(world.stench((2,2)))  # True

    print("?- breeze((1,3))")
    print(world.breeze((1,3)))  # False

    print("?- glitter((2,2))")
    print(world.glitter((2,2)))  # True

    print("?- safe((1,1))")
    print(world.safe((1,1)))  # True

    print("?- safe((3,1))")
    print(world.safe((3,1)))  # True
