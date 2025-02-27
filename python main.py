
#### main.py

```python
#!/usr/bin/env python3
import random

battles = [
    "A siege on a mountain fortress, where defenders must hold against a powerful empire.",
    "A clash between rival knightly orders over a sacred relic.",
    "A coastal raid by Viking warriors seeking gold and glory.",
    "A last stand by a small village against an invading army.",
    "A surprise ambush in a dense forest, where tactics determine victory."
]

def get_random_battle():
    return random.choice(battles)

def main():
    print("Welcome to Excalibur Battle Scenarios!")
    print("Here's a random medieval battle scenario:")
    print(get_random_battle())

if __name__ == "__main__":
    main()
