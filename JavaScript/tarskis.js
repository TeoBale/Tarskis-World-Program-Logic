// Renamed "Object" to "WorldObject" to avoid conflicts with JavaScript's built-in Object
class WorldObject {
  static sizes = {
    "small": 0,
    "medium": 1,
    "large": 2
  };
  
  constructor(key, shape, size, pos) {
    this.key = key;
    this.shape = shape;
    this.size = size;
    this.pos = pos;
  }
}

class Validator {
  static _isSameShape(obj1, obj2) {
    return obj1.shape === obj2.shape;
  }
  
  static _isCube(obj) {
    return obj.shape === "cube";
  }
  
  static _isTet(obj) {
    return obj.shape === "tet";
  }
  
  static _isDodec(obj) {
    return obj.shape === "dodec";
  }
  
  static _isSmall(obj) {
    return obj.size === WorldObject.sizes["small"];
  }
  
  static _isMedium(obj) {
    return obj.size === WorldObject.sizes["medium"];
  }
  
  static _isLarge(obj) {
    return obj.size === WorldObject.sizes["large"];
  }
  
  static _isSameSize(obj1, obj2) {
    return obj1.size === obj2.size;
  }
  
  static _isSmaller(obj1, obj2) {
    return obj1.size < obj2.size;
  }
  
  static _isLarger(obj1, obj2) {
    return obj1.size > obj2.size;
  }
  
  static _isLeftOf(obj1, obj2) {
    return obj1.pos[0] < obj2.pos[0];
  }
  
  static _isRightOf(obj1, obj2) {
    return obj1.pos[0] > obj2.pos[0];
  }
  
  static _isFrontOf(obj1, obj2) {
    return obj1.pos[1] > obj2.pos[1];
  }
  
  static _isBackOf(obj1, obj2) {
    return obj1.pos[1] < obj2.pos[1];
  }
  
  static _isSameRow(obj1, obj2) {
    return obj1.pos[0] === obj2.pos[0];
  }
  
  static _isSameCol(obj1, obj2) {
    return obj1.pos[1] === obj2.pos[1];
  }
  
  static _isAdjacent(obj1, obj2) {
    return Math.abs(obj1.pos[0] - obj2.pos[0]) === 1 || Math.abs(obj1.pos[1] - obj2.pos[1]) === 1;
  }
  
  static _isBetweenOf(objT, obj1, obj2) {
    if (objT.pos[0] === obj1.pos[0] && obj1.pos[0] === obj2.pos[0]) {
      if ((obj1.pos[1] < objT.pos[1] && objT.pos[1] < obj2.pos[1]) || 
          (obj2.pos[1] < objT.pos[1] && objT.pos[1] < obj1.pos[1])) {
        return true;
      }
    } else if (objT.pos[1] === obj1.pos[1] && obj1.pos[1] === obj2.pos[1]) {
      if ((obj1.pos[0] < objT.pos[0] && objT.pos[0] < obj2.pos[0]) || 
          (obj2.pos[0] < objT.pos[0] && objT.pos[0] < obj1.pos[0])) {
        return true;
      }
    } else if (
      Math.abs((obj1.pos[1] - obj2.pos[1]) / (obj1.pos[0] - obj2.pos[0])) === 1 && 
      Math.abs((obj1.pos[1] - objT.pos[1]) / (obj1.pos[0] - objT.pos[0])) === 1
    ) {
      if ((obj1.pos[0] < objT.pos[0] && objT.pos[0] < obj2.pos[0] && obj1.pos[1] < objT.pos[1] && objT.pos[1] < obj2.pos[1]) || 
          (obj2.pos[0] < objT.pos[0] && objT.pos[0] < obj1.pos[0] && obj2.pos[1] < objT.pos[1] && objT.pos[1] < obj1.pos[1])) {
        return true;
      }
    }
    return false;
  }
  
  static functionsNamespace = {
    isSameShape: (obj1, obj2) => Validator._isSameShape(obj1, obj2),
    isCube: (obj) => Validator._isCube(obj),
    isTet: (obj) => Validator._isTet(obj),
    isDodec: (obj) => Validator._isDodec(obj),
    isSmall: (obj) => Validator._isSmall(obj),
    isMedium: (obj) => Validator._isMedium(obj),
    isLarge: (obj) => Validator._isLarge(obj),
    isSameSize: (obj1, obj2) => Validator._isSameSize(obj1, obj2),
    isSmaller: (obj1, obj2) => Validator._isSmaller(obj1, obj2),
    isLarger: (obj1, obj2) => Validator._isLarger(obj1, obj2),
    isLeftOf: (obj1, obj2) => Validator._isLeftOf(obj1, obj2),
    isRightOf: (obj1, obj2) => Validator._isRightOf(obj1, obj2),
    isFrontOf: (obj1, obj2) => Validator._isFrontOf(obj1, obj2),
    isBackOf: (obj1, obj2) => Validator._isBackOf(obj1, obj2),
    isSameRow: (obj1, obj2) => Validator._isSameRow(obj1, obj2),
    isSameCol: (obj1, obj2) => Validator._isSameCol(obj1, obj2),
    isAdjacent: (obj1, obj2) => Validator._isAdjacent(obj1, obj2),
    isBetweenOf: (objT, obj1, obj2) => Validator._isBetweenOf(objT, obj1, obj2)
  };
}

class World {
  constructor() {
    this.objects = {};
  }
  
  addObject(key, shape, sizeKey, pos) {
    // TODO: Fix same position objects
    if (!this.objects[key]) {
      this.objects[key] = new WorldObject(key, shape, WorldObject.sizes[sizeKey], pos);
    }
  }
  
  printWorld() {
    console.log(`Shapes: ${Object.keys(this.objects).length}`);
    
    for (const [key, value] of Object.entries(this.objects)) {
      console.log(`${key} -> Shape:${value.shape}, X:${value.pos[0]}, Y:${value.pos[1]}`);
    }
  }
}

// Evaluate expression
const evaluateExpression = (expression, context) => {
  // Create a function with the given context variables
  const keys = Object.keys(context);
  const values = Object.values(context);
  
  // Create a new function with the context variables
  return new Function(...keys, `return ${expression};`)(...values);
};

// Create a new world
const bw = new World();

// Add objects
bw.addObject("A", "cube", "small", [0, 0]);
bw.addObject("B", "tet", "medium", [1, 0]);
bw.addObject("C", "dodec", "large", [2, 0]);

bw.addObject("D", "dodec", "large", [2, 0]);
bw.addObject("E", "dodec", "large", [3, 1]);
bw.addObject("F", "dodec", "large", [4, 2]);

// Print world
bw.printWorld();

// Merge objects and functions
const evalContext = {
  A: bw.objects["A"],
  B: bw.objects["B"],
  C: bw.objects["C"],
  D: bw.objects["D"],
  E: bw.objects["E"],
  F: bw.objects["F"],
  ...Validator.functionsNamespace
};

// Expressions to evaluate
const expressions = [
  "isBetweenOf(B, C, A) && (!isCube(B))",
  "isCube(A)",
  "isTet(A)",
  "isDodec(A)",
  "isCube(B)",
  "isTet(B)",
  "isDodec(B)",
  "isCube(C)",
  "isTet(C)",
  "isDodec(C)",
  "isRightOf(B, A) && isLeftOf(B, C)",
  "isSameRow(A, B) && isSameRow(B, C)",
  "isSameCol(A, B)",
  "isSameShape(A, C)",
  "isBetweenOf(E, D, F) && isBetweenOf(E, F, D) && isSameShape(D, E) && isDodec(F) && isSameShape(F, E) && (!isLeftOf(F, A))"
]

for (const e of expressions) {
    console.log(e, "-", evaluateExpression(e, evalContext))
}

/* 
// Evaluate the expression
const result = evaluateExpression(
  "isBetweenOf(B, C, A) && (!isCube(B))", 
  evalContext
);

console.log(result);
*/