# VBots

The goal of the **3D Creature (Random 3D Creature Morphologies)** is to reach the block.
3D Creature moves toward the block. **Euclidean distance** between the block and the snake is used as fitness. Lower the distance, better the fitness.

**locationMatrix is used to create a virtual 3D space which fils up area as cubes are sent. This helps in preventing the cubes in overlapping each other.

Links and jointPositionAxis(x, y, z) place are randomly selected for the new link to join. If the selected combination results in overlapping, a new combination is generated.

## How to Run:
Run **search.py** to simulate the results.
<img width="878" alt="3dAILife" src="https://user-images.githubusercontent.com/114874910/220258239-2e1e63d0-18e3-41b8-a610-55a132432249.png">

## References:
1. [Northwestern University - COMP_SCI 396: Artificial Life](https://www.mccormick.northwestern.edu/computer-science/academics/courses/descriptions/396-2.html). 
2. [Professor Sam Kriegman](https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/kriegman-sam.html) 
3. [Pyrosim](https://github.com/jbongard/pyrosim.git)
4. [Education in Evolutionary Robotics](https://www.reddit.com/r/ludobots/wiki/). 
