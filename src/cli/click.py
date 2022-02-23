import click


@click.command()
@click.option(
    "--example",
    prompt='Example function',
    help="Example function",
    type=click.STRING
)
def boilerplate(example: click.STRING) -> None:
    """
    This is a regular click command.

    Args:
        example (click.STRING): example function
    """
    click.echo(f"You're example function is {example}")


@click.group()
def boilerplate_group():
    """ This is a group of commands that allows for script nesting. """
    pass


@click.command()
def start():
    click.echo("Starting...")


@click.command()
def stop():
    click.echo("Stopping...")


boilerplate_group.add_command(start)
boilerplate_group.add_command(stop)



