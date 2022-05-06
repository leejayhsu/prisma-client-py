import click


@click.command('fetch', short_help='Download all required _binaries.')
@click.option(
    '--force',
    is_flag=True,
    help='Download all _binaries regardless of if they are already downloaded or not.',
)
def cli(force: bool) -> None:
    """Ensures all required _binaries are available."""
    from ... import _binaries

    if force:
        _binaries.remove_all()

    directory = _binaries.ensure_cached()
    click.echo(
        f'Downloaded _binaries to {click.style(str(directory), fg="green")}'
    )
