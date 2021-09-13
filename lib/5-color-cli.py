import click

@click.command()
@click.option('--name','-n')
def main(name):
    '''colored cli'''
    click.echo(click.style((f'Welcome to command line app'), bold=True, fg='black', bg='white'))
    click.echo(click.style((f'Hello My name is : {name}'), fg='red', bg='white'))



if __name__ == '__main__':
    main()