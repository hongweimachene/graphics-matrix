from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print_matrix(matrix);

id = ident(matrix);
print_matrix(id);

draw_lines( matrix, screen, color )
display(screen)
