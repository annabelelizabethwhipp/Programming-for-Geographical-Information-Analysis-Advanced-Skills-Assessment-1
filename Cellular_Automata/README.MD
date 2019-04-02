In this practical a simple cellular automata model was built to represent a small forest fire

There is one file needed which is called ca.py

- An environment is created

- Loop through number_of_iterations

- Loop through height with variable h

- Loop through width with variable w

- Check values around environment[h][w] for fire

- If fire found, and value in [h][w] > 1, reduce value by 1

- A stopping condition is added 


In the command line the output can be saved to a text file:
python ca.py >> output.txt
