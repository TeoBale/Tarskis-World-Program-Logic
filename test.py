import re
from dataclasses import dataclass
from typing import Dict, List, Tuple, Set, Optional, Union, Callable

# Define the world model
@dataclass
class Object:
    name: str
    shape: str  # "cube", "tetrahedron", "dodecahedron"
    size: str   # "small", "medium", "large"
    position: Tuple[int, int]  # (x, y) coordinates

class World:
    def __init__(self):
        self.objects: Dict[str, Object] = {}
    
    def add_object(self, obj: Object):
        self.objects[obj.name] = obj
    
    def get_object(self, name: str) -> Optional[Object]:
        return self.objects.get(name)

# Define the expression parser
class ExpressionParser:
    def __init__(self):
        self.predicates = {
            "IsSameShape": self._is_same_shape,
            "isLeft": self._is_left,
            "IsCube": self._is_cube,
            "IsTetrahedron": self._is_tetrahedron,
            "IsDodecahedron": self._is_dodecahedron,
            "IsSameSize": self._is_same_size,
            "IsSmall": self._is_small,
            "IsMedium": self._is_medium,
            "IsLarge": self._is_large,
            "IsRightOf": self._is_right_of,
            "IsFrontOf": self._is_front_of,
            "IsBackOf": self._is_back_of,
        }
        self.operators = {"&", "|", "->", "<->", "~"}
    
    def parse(self, expression: str) -> dict:
        """Parse the expression into a syntax tree"""
        expression = expression.strip()
        
        # Check if the expression is a compound expression with logical operators
        for op in ["&", "|", "->", "<->"]:
            if op in expression:
                # Split only on the operator not inside parentheses
                parts = self._smart_split(expression, op)
                if len(parts) > 1:
                    return {
                        "type": "binary",
                        "operator": op,
                        "left": self.parse(parts[0]),
                        "right": self.parse(parts[1])
                    }
        
        # Check for negation
        if expression.startswith("~"):
            return {
                "type": "unary",
                "operator": "~",
                "expression": self.parse(expression[1:].strip())
            }
        
        # Handle parentheses
        if expression.startswith("(") and expression.endswith(")"):
            return self.parse(expression[1:-1].strip())
        
        # Parse atomic predicates
        match = re.match(r"(\w+)\((.*?)\)", expression)
        if match:
            predicate_name = match.group(1)
            args = [arg.strip() for arg in match.group(2).split(",")]
            return {
                "type": "predicate",
                "name": predicate_name,
                "args": args
            }
        
        raise ValueError(f"Failed to parse expression: {expression}")
    
    def _smart_split(self, expression: str, operator: str) -> List[str]:
        """Split the expression by operator but respect parentheses"""
        result = []
        paren_count = 0
        current_part = ""
        
        i = 0
        while i < len(expression):
            # Check if we've found the operator at the top level
            if (expression[i:i+len(operator)] == operator and paren_count == 0):
                result.append(current_part.strip())
                current_part = ""
                i += len(operator)
                continue
                
            # Keep track of parentheses
            if expression[i] == "(":
                paren_count += 1
            elif expression[i] == ")":
                paren_count -= 1
                
            current_part += expression[i]
            i += 1
            
        if current_part:
            result.append(current_part.strip())
            
        return result
    
    # Predicate implementations
    def _is_same_shape(self, world: World, args: List[str]) -> bool:
        obj1 = world.get_object(args[0])
        obj2 = world.get_object(args[1])
        if not obj1 or not obj2:
            return False
        return obj1.shape == obj2.shape
    
    def _is_left(self, world: World, args: List[str]) -> bool:
        obj1 = world.get_object(args[0])
        obj2 = world.get_object(args[1])
        if not obj1 or not obj2:
            return False
        return obj1.position[0] < obj2.position[0]
    
    def _is_cube(self, world: World, args: List[str]) -> bool:
        obj = world.get_object(args[0])
        if not obj:
            return False
        return obj.shape == "cube"
    
    def _is_tetrahedron(self, world: World, args: List[str]) -> bool:
        obj = world.get_object(args[0])
        if not obj:
            return False
        return obj.shape == "tetrahedron"
    
    def _is_dodecahedron(self, world: World, args: List[str]) -> bool:
        obj = world.get_object(args[0])
        if not obj:
            return False
        return obj.shape == "dodecahedron"
    
    def _is_same_size(self, world: World, args: List[str]) -> bool:
        obj1 = world.get_object(args[0])
        obj2 = world.get_object(args[1])
        if not obj1 or not obj2:
            return False
        return obj1.size == obj2.size
    
    def _is_small(self, world: World, args: List[str]) -> bool:
        obj = world.get_object(args[0])
        if not obj:
            return False
        return obj.size == "small"
    
    def _is_medium(self, world: World, args: List[str]) -> bool:
        obj = world.get_object(args[0])
        if not obj:
            return False
        return obj.size == "medium"
    
    def _is_large(self, world: World, args: List[str]) -> bool:
        obj = world.get_object(args[0])
        if not obj:
            return False
        return obj.size == "large"
    
    def _is_right_of(self, world: World, args: List[str]) -> bool:
        obj1 = world.get_object(args[0])
        obj2 = world.get_object(args[1])
        if not obj1 or not obj2:
            return False
        return obj1.position[0] > obj2.position[0]
    
    def _is_front_of(self, world: World, args: List[str]) -> bool:
        obj1 = world.get_object(args[0])
        obj2 = world.get_object(args[1])
        if not obj1 or not obj2:
            return False
        return obj1.position[1] < obj2.position[1]
    
    def _is_back_of(self, world: World, args: List[str]) -> bool:
        obj1 = world.get_object(args[0])
        obj2 = world.get_object(args[1])
        if not obj1 or not obj2:
            return False
        return obj1.position[1] > obj2.position[1]

# Define the expression evaluator
class ExpressionEvaluator:
    def __init__(self, parser: ExpressionParser):
        self.parser = parser
    
    def evaluate(self, syntax_tree: dict, world: World) -> bool:
        """Evaluate the syntax tree against the world model"""
        if syntax_tree["type"] == "predicate":
            predicate_func = self.parser.predicates.get(syntax_tree["name"])
            if not predicate_func:
                raise ValueError(f"Unknown predicate: {syntax_tree['name']}")
            return predicate_func(world, syntax_tree["args"])
        
        elif syntax_tree["type"] == "binary":
            left_result = self.evaluate(syntax_tree["left"], world)
            right_result = self.evaluate(syntax_tree["right"], world)
            
            if syntax_tree["operator"] == "&":
                return left_result and right_result
            elif syntax_tree["operator"] == "|":
                return left_result or right_result
            elif syntax_tree["operator"] == "->":
                return (not left_result) or right_result
            elif syntax_tree["operator"] == "<->":
                return left_result == right_result
        
        elif syntax_tree["type"] == "unary" and syntax_tree["operator"] == "~":
            return not self.evaluate(syntax_tree["expression"], world)
        
        raise ValueError(f"Failed to evaluate syntax tree: {syntax_tree}")

# Main validator class
class TarskiValidator:
    def __init__(self):
        self.parser = ExpressionParser()
        self.evaluator = ExpressionEvaluator(self.parser)
        self.world = World()
    
    def add_object(self, obj: Object):
        self.world.add_object(obj)
    
    def validate_expression(self, expression: str) -> bool:
        """Validate a logical expression against the current world"""
        try:
            syntax_tree = self.parser.parse(expression)
            result = self.evaluator.evaluate(syntax_tree, self.world)
            return result
        except Exception as e:
            print(f"Error validating expression: {e}")
            return False
    
    def print_syntax_tree(self, expression: str):
        """Print the syntax tree of an expression (for debugging)"""
        try:
            syntax_tree = self.parser.parse(expression)
            import json
            print(json.dumps(syntax_tree, indent=2))
        except Exception as e:
            print(f"Error parsing expression: {e}")

# Example usage
def main():
    # Create a Tarski validator
    validator = TarskiValidator()
    
    # Define a simple world with objects
    validator.add_object(Object("a", "cube", "medium", (1, 1)))
    validator.add_object(Object("b", "cube", "small", (3, 2)))
    validator.add_object(Object("c", "tetrahedron", "medium", (2, 3)))
    
    # Test expressions
    expressions = [
        "IsCube(a)",
        "IsCube(a) & IsCube(b)",
        "IsSameShape(a, b) & isLeft(a, b) & IsTetrahedron(b)",
        "IsTetrahedron(c) & ~IsCube(c)",
        "IsSameShape(a, c)",
        "isLeft(a, b) & isLeft(b, c)"
    ]
    
    print("World setup:")
    for name, obj in validator.world.objects.items():
        print(f"  {name}: {obj.shape} {obj.size} at position {obj.position}")
    
    print("\nExpression validation results:")
    for expr in expressions:
        result = validator.validate_expression(expr)
        print(f"  {expr}: {result}")
    
    print("\nsyntax tree for 'IsSameShape(a, b) & isLeft(a, b) & IsCube(b)':")
    validator.print_syntax_tree("IsSameShape(a, b) & isLeft(a, b) & IsCube(b)")

if __name__ == "__main__":
    main()