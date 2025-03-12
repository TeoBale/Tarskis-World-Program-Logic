from .trarskis_world import World, Validator
 
bw = World()

bw.add_object("A","cube", "small", (0, 0))
bw.add_object("B","tet", "medium", (1, 0))
bw.add_object("C","dodec", "large", (2, 0))

bw.print_world()

print(eval("isBetweenOf(B, C, A) & (not isCube(B))", bw.objects | Validator.functions_namepsaces))
