import click

@click.command()
# basic option with default value
@click.option('--name','-n',default='Krish',help='your first name')
# option with multiple values (max 2), ex. -s 100 500
@click.option('--salary','-s',nargs=2,help='your monthly salary range [from - to]',type=int)
# option with multiple values, ex -ls A -ls B -ls C
@click.option('--locations','-ls',help='option city names used multiple times',multiple=True)


def main(name, salary, locations):
    print(f'Hello My name is : {name}')
    print(f'My salary range is from {salary[0]} - {salary[1]}')
    print(f"locations: {locations}")



if __name__ == '__main__':
    main()