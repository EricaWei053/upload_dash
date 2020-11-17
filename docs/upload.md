

## How to upload your code? 

Use git worklflow to create a Pull Request to this folder. 

Step 1:

Press the Fork button in the upper left in this repository. 

Step 2: 

GitHub will automatically redirect you to the forked repository under your username. Then clone to your local development environment

For example: 
```
git clone git@github.com:jakejarvis/react-native.git
```

Step 3: 
Track original repository
```
git remote add --track master upstream git@github.com:facebook/react-native.git
git fetch upstream 
```

Step 4: 

Add your dash code file to /users folder, make sure your file name is different with others. 
Then, 
```
git add .
git commit -m "Upload dash code file"
```

Step 5:
Push back the repository, 
```
git push -u origin upload-file
``` 
