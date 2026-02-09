import turtle

# Create turtle
t = turtle.Turtle()
t.speed(5)

# Draw a colorful spiral
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(36):
    t.color(colors[i % 6])
    t.forward(i * 5)
    t.right(60)

print("Spiral complete!")
