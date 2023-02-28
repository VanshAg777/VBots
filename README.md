# VBots

The goal of the **3D Creature (Random 3D Creature Morphologies)** is to reach the block.
3D Creature moves toward the block. **Euclidean distance** between the block and the snake is used as fitness. Lower the distance, better the fitness.

**locationMatrix** is used to create a virtual 3D space which fils up area as cubes are sent. This helps in preventing the cubes in overlapping each other.

Links and jointPositionAxis(x, y, z) place are randomly selected for the new link to join. If the selected combination results in overlapping, a new combination is generated.

It is randomly selected if a new link is to be added or an existing link has to be removed or only weights have to be changed. If a link has to be removed, it is made sure that the link does not have an extending link.

## How to Run:
Run **search.py** to simulate the results.
<img width="878" alt="3dAILife" src="https://user-images.githubusercontent.com/114874910/220258239-2e1e63d0-18e3-41b8-a610-55a132432249.png">

## Graph 1:
![GraphFinal1](https://user-images.githubusercontent.com/114874910/221763195-3ca975b6-aba3-4674-ba24-7000adf2eaf0.png)

## Graph 2:
![Graph2Final](https://user-images.githubusercontent.com/114874910/221763244-a21c516a-315d-4d8e-9d0a-367da0f0eaa2.png)

## Graph 3:
![figure3final](https://user-images.githubusercontent.com/114874910/221763302-b852d1d0-ec54-4fe1-9206-811247fd94d0.png)

## Graph 4:
![GraphFinal4](https://user-images.githubusercontent.com/114874910/221763335-f055982c-521f-431e-bab5-88862789f746.png)

## Graph 5:
![graph5final](https://user-images.githubusercontent.com/114874910/221763386-8570daf6-0579-478d-9307-e9bd504518b5.png)

## References:
1. [Northwestern University - COMP_SCI 396: Artificial Life](https://www.mccormick.northwestern.edu/computer-science/academics/courses/descriptions/396-2.html). 
2. [Professor Sam Kriegman](https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/kriegman-sam.html) 
3. [Pyrosim](https://github.com/jbongard/pyrosim.git)
4. [Education in Evolutionary Robotics](https://www.reddit.com/r/ludobots/wiki/). 
