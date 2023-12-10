# N = -y
# S = +y
# W = -y
# E = +y

class Tile:
    def __init__(self, coords: tuple[int, int], type: str) -> None:
        self.x, self.y = self.coords = coords
        self.type = type
        
        match type:
            case "|":
                self.coord_connections = ((self.x, self.y - 1), (self.x, self.y + 1))
            case "-":
                self.coord_connections = ((self.x - 1, self.y), (self.x + 1, self.y))
            case "L":
                self.coord_connections = ((self.x, self.y - 1), (self.x + 1, self.y))
            case "J":
                self.coord_connections = ((self.x, self.y - 1), (self.x - 1, self.y))
            case "7":
                self.coord_connections = ((self.x, self.y + 1), (self.x - 1, self.y))
            case "F":
                self.coord_connections = ((self.x, self.y + 1), (self.x + 1, self.y))
            case "S":
                self.coord_connections = ((self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1))
            case _:
                self.coord_connections = ()
    
    def assign_connections(self, tiles):
        tile_connections = []
        for connection in self.coord_connections:
            x, y = connection
            if x < 0 or x >= len(tiles[0]) or y < 0 or y >= len(tiles): continue
            tile_connections.append(tiles[y][x])
        self.tile_connections = tuple(tile_connections)
    
    def find_loop(self):
        for start in self.tile_connections:
            if self not in start.tile_connections: continue

            loop = [self, start]

            while loop[-1] != self:
                following, = [tile for tile in loop[-1].tile_connections if tile != loop[-2]]
                if following == self: return loop
                if loop[-1] not in following.tile_connections: break
                loop.append(following)
    
    def __repr__(self) -> str:
        return f"Tile({self.coords}, {self.type})"


with open("input.txt") as f:
    input_lines = f.read().strip().split("\n")

tiles = [[Tile((x, y), char) for x, char in enumerate(line)] for y, line in enumerate(input_lines)]

start = None

for row in tiles:
    for tile in row:
        tile.assign_connections(tiles)
        if tile.type == "S":
            start = tile

print(len(start.find_loop()) // 2)