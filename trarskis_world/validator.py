from collections.abc import Callable
from world import Object

class Validator:
    
    @staticmethod
    def _is_same_shape(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.shape == obj_2.shape:
            return True
        return False
    
    @staticmethod
    def _is_cube(obj: Object) -> bool:
        if obj.shape == "cube":
            return True
        return False
    
    @staticmethod
    def _is_tet(obj: Object) -> bool:
        if obj.shape == "tet":
            return True
        return False
        
    @staticmethod
    def _is_dodec(obj: Object) -> bool:
        if obj.shape == "dodec":
            return True
        return False
        
    @staticmethod
    def _is_small(obj: Object) -> bool:
        if obj.size == Object.sizes["small"]:
            return True
        return False
    
    @staticmethod
    def _is_medium(obj: Object) -> bool:
        if obj.size == Object.sizes["medium"]:
            return True
        return False
        
    @staticmethod
    def _is_large(obj: Object) -> bool:
        if obj.size == Object.sizes["large"]:
            return True
        return False
        
    @staticmethod
    def _is_same_size(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.size == obj_2.size:
            return True
        return False
    
    @staticmethod
    def _is_smaller(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.size < obj_2.size:
            return True
        return False
        
    @staticmethod
    def _is_larger(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.size > obj_2.size:
            return True
        return False
    
    @staticmethod
    def _is_left_of(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.pos[0] < obj_2.pos[0]:
            return True
        return False
    
    @staticmethod
    def _is_right_of(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.pos[0] > obj_2.pos[0]:
            return True
        return False
        
    @staticmethod
    def _is_front_of(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.pos[1] > obj_2.pos[1]:
            return True
        return False
    
    @staticmethod
    def _is_back_of(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.pos[1] < obj_2.pos[1]:
            return True
        return False
    
    @staticmethod
    def _is_same_row(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.pos[0] == obj_2.pos[0]:
            return True
        return False
    
    @staticmethod
    def _is_same_col(obj_1: Object, obj_2: Object) -> bool:
        if obj_1.pos[1] == obj_2.pos[1]:
            return True
        return False
    
    @staticmethod 
    def _is_adjacent(obj_1: Object, obj_2: Object) -> bool:
        if abs(obj_1.pos[0] - obj_2.pos[0]) == 1 or abs(obj_1.pos[1] - obj_2.pos[1]) == 1:
            return True
        return False
    
    @staticmethod 
    def _is_between_of(obj_t: Object, obj_1: Object, obj_2: Object) -> bool:
        if obj_t.pos[0] == obj_1.pos[0] == obj_2.pos[0]:
            if obj_1.pos[1] < obj_t.pos[1] < obj_2.pos[1] or obj_2.pos[1] < obj_t.pos[1] < obj_1.pos[1]:
                return True
        elif obj_t.pos[1] == obj_1.pos[1] == obj_2.pos[1]:
            if obj_1.pos[0] < obj_t.pos[0] < obj_2.pos[0] or obj_2.pos[0] < obj_t.pos[0] < obj_1.pos[0]:
                return True
        elif abs((obj_1.pos[1] - obj_2.pos[1])/(obj_1.pos[1] - obj_2.pos[1])) == 1 and abs((obj_1.pos[1] - obj_t.pos[1])/(obj_1.pos[1] - obj_t.pos[1])) == 1 :
            if (obj_1.pos[0] < obj_t.pos[0] < obj_2.pos[0] and obj_1.pos[1] < obj_t.pos[1] < obj_2.pos[1]) or (obj_2.pos[0] < obj_t.pos[0] < obj_1.pos[0] and obj_2.pos[1] < obj_t.pos[1] < obj_1.pos[1]) :
                return True
        return False
    
        
    functions_namepsaces: dict[str, Callable] = {
        "isSameShape": _is_same_shape,
        "isCube": _is_cube,
        "isTet": _is_tet,
        "isDodec": _is_dodec,
        "isSmall": _is_small,
        "isMedium": _is_medium,
        "isLarge": _is_large,
        "isSameSize": _is_same_size,
        "isSmaller": _is_smaller,
        "isLarger": _is_larger,
        "isLeftOf": _is_left_of,
        "isRightOf": _is_right_of,
        "isFrontOf": _is_front_of,
        "isBackOf": _is_back_of,
        "isSameRow": _is_same_row,
        "isSameCol": _is_same_col,
        "isAdjacent": _is_adjacent,
        "isBetweenOf": _is_between_of,
    }
    