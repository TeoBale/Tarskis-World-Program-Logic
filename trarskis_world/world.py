class Object:
    sizes: dict[str, int] = {
        "small": 0,
        "medium": 1,
        "large": 2
    }
    
    def __init__(self, key: str, shape: str, size: int, pos: tuple[int, int]) -> None:
        self.key: str = key
        self.shape: str = shape
        self.size: int = size
        self.pos: tuple[int, int] = pos

class World:
    def __init__(self) -> None:
        self.objects: dict[str, Object] = {}
    
    def add_object(self, key: str, shape: str, size_key: str, pos: tuple[int, int]) -> None:
        # TODO: Fix same position objects
        if key not in self.objects:   
            self.objects[key] = Object(key, shape, Object.sizes[size_key], pos)
        
    def print_world(self) -> None:
        print(f"Shapes: {len(self.objects)}")
        
        iterator = self.objects.items()
        for k, v in iterator:
            print(f"{k} -> Shape:{v.shape}, X:{v.pos[0]}, Y:{v.pos[1]}")