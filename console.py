import click

from .main import SaveReddit


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option("--comments", is_flag=True, help="get saved comments")
@click.option("--titles", is_flag=True, help="get titles of saved items")
@click.pass_context
def saved(comments, titles):
    reddit = SaveReddit()
    if comments:
        click.echo(reddit.extract_comments())
    if titles:
        click.echo(reddit.extract_title())


@cli.command()
@click.option("--thread-id", help="the thread id")
@click.option("--url", help="url")
@click.option("--save", is_flag=True, help="save to file (default is stdout)")
@click.pass_context
def comments(thread_id, url, save):
    click.echo(f"Getting comments for {thread_id=}")
    if url is not None:
        click.echo("WARN: url not supported yet")
    reddit = SaveReddit()
    click.echo("TODO")
