# 3D Pong Game in Web VPython

Welcome to a 3D Pong-style game built entirely in **Web VPython 3.2**! This project simulates a two-player paddle game with physics-based collision and dynamic ball movement in a 3D scene.

---

## Description

This is a simplified version of **3D Pong** implemented using **VPython**, featuring two paddles, boundary walls, and a bouncing ball. The player controls the paddles using keyboard inputs, and the ball reflects realistically off the walls and paddles.

The game ends when the ball crosses the left or right walls — declaring the opponent as the winner.

---

## Features

- Real-time 3D physics simulation
- Wall and paddle collision detection
- Smooth paddle control for two players
- Randomized ball direction on serve
- Win condition detection and game reset

---

## Controls

| Key        | Action                      |
|------------|-----------------------------|
| `W`        | Move left paddle up         |
| `S`        | Move left paddle down       |
| `↑ (Up)`   | Move right paddle up        |
| `↓ (Down)` | Move right paddle down      |
| `Space`    | Restart the game with new random ball direction |

---

## Getting Started

### Run Online

You can run this directly in a browser using the **Web VPython environment**. Recommended environment:

👉 [https://www.glowscript.org](https://www.glowscript.org)

Just copy and paste the code into a **GlowScript VPython 3.2** program.

### Run Locally (optional)

If you prefer to run locally:
1. Install **VPython**:
    ```bash
    pip install vpython
    ```
2. Use a basic web server or Jupyter notebook to render the scene (not all VPython functions work outside web contexts).

---

## Educational Value

This project helps reinforce understanding of:
- 3D vector motion and collisions
- Real-time event handling in VPython
- Game loop logic
- User input handling via `keydown` and `click` bindings


---

## Author

Developed by **Brij Patel**  
For fun and educational use!

