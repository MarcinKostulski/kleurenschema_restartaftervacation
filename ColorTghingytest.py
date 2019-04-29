import click
import random

# for x in range(10):
#     colors = ["red","yellow","green", "blue"]
#     click.secho('Hallo', fg=colors[random.randint(0,3)])

colorScheme = {
    10:"red",
    20:"white",
    30:"yellow",
    40:"black",
    50:"green",
    60:"cyan",
    70:"magenta",
    80:"blue"
}

x = colorScheme.items()
print(x)

ns = [random.randint(0,80) for x in range(100)]

for n in ns:
    color =""
    #SHORTER ALGORITHM TODO
    for k,v in colorScheme.items():
        if n < k:
            color=v
            click.secho(str(n), fg=color)
        else:
            continue

    #UNNECESSARILY LONG TEMPORARY IFELSE SOLUTION
    # if n<10:
    #     color="red"
    # elif n<20:
    #     color="white"
    # elif n<30:
    #     color="yellow"
    # elif n<40:
    #     color="black"
    # elif n<50:
    #     color="green"
    # elif n<60:
    #     color="cyan"
    # elif n<70:
    #     color="magenta"
    # elif n<80:
    #     color="blue"
        
    # click.secho(str(n), fg=color)