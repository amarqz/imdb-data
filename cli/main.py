from application import app, console
from rich.panel import Panel

def repl():
    console.print(Panel.fit("[bold yellow]IMDb Data[/bold yellow]\n[i]The database for movies, documentaries, actors...[/i]", title="🎬 Welcome"))
    app(args='check'.split(), standalone_mode=False)

    while True:
        try:
            command = console.input("\n[bold gold1]IMDb-data[/bold gold1][yellow]>[/yellow] ").strip()
            if command in ['exit', 'quit']:
                break

            args = command.split()
            if args:
                app(args=args, standalone_mode=False)
        except Exception as e:
            print(f'An error ocurred: {e}')

if __name__ == "__main__":
    repl()