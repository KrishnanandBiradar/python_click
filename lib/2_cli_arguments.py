import click

@click.command()
# arguments to the command
@click.argument('num1',type=int)
@click.argument('num2',type=int)
@click.argument('method',default='add')
def main(num1, num2, method):
    """ add number 1 and 2"""
    if method == 'add':
        result = num1 + num2
    elif method == 'mul':
        result = num1 * num2
    print(result)


@click.command()
# supply n number of arguments with nargs=-1 to the command
@click.argument('src',nargs=-1)
@click.argument('dest',nargs=1)
def move_files(src, dest):
    """ DESC: move source files to destination folder """
    for sr, f in enumerate(src, start=1):
        print(f'{sr}.Moving {f} to folder {dest}')



if __name__ == '__main__':
    ## arguments
    # main()
    ## usage of n arguments
    move_files()