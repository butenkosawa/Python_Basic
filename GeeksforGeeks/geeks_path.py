from pathlib import Path

p = Path('C:\\Users\\SecAdmin\\PycharmProjects\\PythonBasic\\GeeksforGeeks')

files = p.rglob('*.py')

sp = p / 'example.txt'
print(sp)

print("Is absolute:", sp.is_absolute())

# Get the file name
print("File name:", sp.name)

# Get the extension
print("Extension:", sp.suffix)

# Get the parent directory
print("Parent directory:", sp.parent)
