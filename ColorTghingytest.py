import click
import random

for x in range(10):
    colors = ["red","yellow","green", "blue"]
    click.secho('Hallo', fg=colors[ random.randint(0,3)] )