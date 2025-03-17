from window import *

def main():
    wow = Window(800, 800)
    a = Point(15, 15)
    b = Point(300, 300)
    c = Line(a, b)
    wow.draw_line(c, "blue")
    wow.wait_for_close()

main()