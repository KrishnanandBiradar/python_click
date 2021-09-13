import click

@click.group()
def main():
    '''use click.group for grouping commands to function'''
    pass

@main.command()
@click.argument('text')
def reverse(text):
    '''reverse a text'''
    click.echo(text[::-1])

@main.command()
@click.argument('text')
def getovels(text):
    '''extract ovels'''
    ovels = [i for i in text if i in ['a','e','i','o','u']]
    click.echo(ovels)

@main.command()
@click.argument('text')
def getlength(text):
    '''get length of text'''
    click.echo(len(text))



if __name__ == '__main__':
    main()