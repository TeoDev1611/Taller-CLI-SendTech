import click
from functions import *

@click.group()
def app():
    """
    A simple basic Calculator of Multplication and divide
    """
    pass

@app.command("sum", short_help= "Sum the numbers")
@click.option("--num1", help="Parse the first number", type=int)
@click.option("--num2", help="Parse the second argument", type=int)
def sumCommand(num1= None,num2= None):
    """
    Sum the numbers
    """
    Validate(num1,num2)
    print(sum(num1,num2))

@app.command("subs", short_help= "Substract the numbers")
@click.option("--num1", help="Parse the first number", type=int)
@click.option("--num2", help="Parse the second argument", type=int)
def substractCommand(num1= None,num2= None):
    """
    Substract the numbers
    """
    Validate(num1,num2)
    print(substract(num1,num2))


@app.command("multi", short_help= "Multiply the numbers")
@click.option("--num1", help="Parse the first number", type=int)
@click.option("--num2", help="Parse the second argument", type=int)
def multiCommand(num1= None,num2= None):
    """
    Multiply the numbers
    """

    Validate(num1,num2)
    print(multi(num1,num2))

@app.command("divide", short_help= "Divide the numbers")
@click.option("--num1", help="Parse the first number", type=int)
@click.option("--num2", help="Parse the second argument", type=int)
def divideCommand(num1= None,num2= None):
    """
    Divide the numbers
    """

    Validate(num1,num2)
    print(divide(num1,num2))

app()
