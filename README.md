# VBots

The goal of the **3D Creature (Random 3D Creature Morphologies)** is to reach the block.
3D Creature moves toward the block. **Euclidean distance** between the block and the snake is used as fitness. Lower the distance, better the fitness.

**locationMatrix** is used to create a virtual 3D space which fils up area as cubes are sent. This helps in preventing the cubes in overlapping each other.

Links and jointPositionAxis(x, y, z) place are randomly selected for the new link to join. If the selected combination results in overlapping, a new combination is generated.

It is randomly selected if a new link is to be added or an existing link has to be removed or only weights have to be changed. If a link has to be removed, it is made sure that the link does not have an extending link.

## How to Run:
Run **search.py** to simulate the results.

## GIF
![AILifeFinal](https://user-images.githubusercontent.com/114874910/225197330-44ed8c57-24db-419f-8170-7f0c12045863.gif)

## YouTube
https://youtu.be/byaxfnLWE7k

## Parallel Hill climbing
Each parent and child compete with the other. Ultimately, the bot with the best fitness is selected out of the population.
<img width="448" alt="PHC" src="https://user-images.githubusercontent.com/114874910/225202111-fe6b8bb7-8517-45c9-8e37-01e946d08587.png">

## Phenotype 
The creature is made randomly.
<img width="878" alt="3dAILife" src="https://user-images.githubusercontent.com/114874910/220258239-2e1e63d0-18e3-41b8-a610-55a132432249.png">

## Genotype 
As the links are cuboids, each face can have a link attached to it by a joint. Therefore six links can be attached to a single link.
<img width="237" alt="Fig3" src="https://user-images.githubusercontent.com/114874910/225195358-cd15c0e6-9977-4b1f-a237-979b1345f89e.png">

## Mutation
Green - Sensors/Blue - Motor
<img width="751" alt="FinalBeneficial" src="https://user-images.githubusercontent.com/114874910/225206123-3aedcda4-3185-4ea6-9734-dbe65a744479.png">


## Graph 
![GraphFinal](https://user-images.githubusercontent.com/114874910/225210789-d59ae60a-de83-4121-b90f-43e5ca0294c4.png)

## References:
1. [Northwestern University - COMP_SCI 396: Artificial Life](https://www.mccormick.northwestern.edu/computer-science/academics/courses/descriptions/396-2.html). 
2. [Professor Sam Kriegman](https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/kriegman-sam.html) 
3. [Pyrosim](https://github.com/jbongard/pyrosim.git)
4. [Education in Evolutionary Robotics](https://www.reddit.com/r/ludobots/wiki/). 
