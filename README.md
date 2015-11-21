# Python-Tag-Parser
Small tag parsing Utility written in Python

__Usage:__
```
python tagparser.py "TAGHERE" "STRING HERE"
```
Make sure you encapsulate your arguments inside double quoted marks.

__Example:__
```bash
python tagparser.py "*" "Python is *awesome* and *fast*"
# ['awesome', 'fast']
```

You can also import it and use the __parsetag(tag, string)__ function
__Example:__
```python
print(parsetag('*', 'Python is *awesome* and *fast*'))
# ['awesome', 'fast']
```
