import turtle
import math

def draw_connected_hearts():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Connected Hearts")
    screen.bgcolor("white")
    
    # Create and set up the turtle
    t = turtle.Turtle()
    t.speed(5)
    t.hideturtle()
    
    def draw_heart(color, start_x):
        t.penup()
        t.goto(start_x, 0)
        t.pendown()
        
        t.color(color)
        t.fillcolor(color)
        t.begin_fill()
        
        t.left(140)
        t.forward(111)
        
        # Right curve
        for _ in range(200):
            t.right(1)
            t.forward(1)
            
        # Left curve
        t.left(120)
        for _ in range(200):
            t.right(1)
            t.forward(1)
            
        t.forward(111)
        t.end_fill()
        
        # Reset heading for next heart
        t.setheading(0)
    
    # Draw first heart (pink)
    draw_heart("#FF69B4", -100)
    
    # Draw second heart (red)
    draw_heart("#FF1493", 20)
    
    # Add text "PRADEEP"
    t.penup()
    t.goto(-40, 0)  # Position for text
    t.color("black")  # White color for contrast
    t.write("Nehir Kurt", align="center", font=("Arial", 20, "bold"))
    
    # Keep the window open
    screen.mainloop()

# Run the program
if __name__ == "__main__":
    draw_connected_hearts()