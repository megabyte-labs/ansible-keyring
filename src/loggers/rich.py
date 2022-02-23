from rich.console import Console
from rich.table import Table


def rich_print():
    """ Prints some beautifully formatted data to the terminal """
    console = Console()
    console.print("\nPython CLI", ":snake:", style="bold blue")

    table = Table.grid(padding=1, pad_edge=True)
    table.add_column(
        "Feature", no_wrap=True, justify="center", style="bold magenta")
    table.add_column("Info")

    # Description row
    table.add_row(
        "Description",
        "Python CLI is a boilerplate project that will give your new project "
        "a great headstart! It is built on top on amazing Open Source, commun"
        "ity-maintained libraries and packages."
    )

    # Dependencies
    table.add_row(
        "Packages",
        "✓ [bold green]Poetry as a dependency manager.[/]\n"
        "✓ [bold blue]Sphinx and Themes documentation.[/]\n"
        "✓ [bold magenta]Rich for logging and text formatting.[/]\n"
        "✓ [bold yellow]Click to create command line interfaces.[/]\n"
        "✓ [bold cyan]Fire to generate CLIs from Python objects."
    )

    console.print(table)
