# Ex2
import click


# First Step:
@click.command()

# Second Step:
@click.argument('num', default=1, type=int)
# Third Step:
@click.option('--name', default="Thank you!")
# Boolean flag option, is provided for conditional statements.
@click.option('--upper', is_flag=True, help="Will print the name in Uppercase and thank the user if there is!")
def cli(num, upper, name):
    if upper:
        click.echo(f"Thank you {name.upper()}")
    else:
        click.echo(f"Thank you {name}")


    if num == 0:
        click.echo("You can't square zero!")
    else:
        click.echo(f"The square number of {num} is = {num**2}")


# Click supports both Python versions 2 & 3 while using echo instead of print()

if __name__ == '__main__':
    cli()
