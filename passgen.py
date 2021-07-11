import typer
import f_gen
import pyperclip

# default password length
DEFAULT_LENGTH = 10


app = typer.Typer()


@app.command()
def gen_pass(gen: int = typer.Option(DEFAULT_LENGTH, "--length", "-l")):
    try:
        password = f_gen.gen_pass(gen)
        pyperclip.copy(password)
        typer.echo(password)
    except ValueError as error:
        error_message = typer.style('Error', fg=typer.colors.WHITE,
                                    bg=typer.colors.RED)
        typer.echo(f'{error_message}: {error}')


if __name__ == "__main__":
    app()
