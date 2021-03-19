### We need to create the Template to store in Github Repository
### It must be easy to understandable by the Whole Team

import os

# Folder
dirs = [
    "data_given",
    os.path.join("data","raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]
#Files
files = [
    ".gitignore",
    os.path.join("src", "__init__.py"),
    "dvc.yaml",
    "params.yaml"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass

for file_ in files:
    with open(file_, "w") as f:
        pass