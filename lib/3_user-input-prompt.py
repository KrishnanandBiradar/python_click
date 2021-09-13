import click

@click.command()
# arguments to the command
@click.option('--name',prompt='Enter your name')
@click.option('--passwd',prompt='Enter your password',hide_input=True)
def main(name,passwd):
    """take inputs from user with prompt and hide input"""
    age = click.prompt("Enter your age")
    click.echo(f"name entered is: {name} and age: {age}")
    click.echo(f"your secret password is: {passwd}")

if __name__ == '__main__':    
    main()