import click
from stegocli.core import encode_image, decode_image

@click.group()
def cli():
    """Simple CLI Steganography Tool"""
    pass

@cli.command()
@click.argument('image')
@click.argument('output')
@click.argument('message')
def encode(image, output, message):
    """Encode a MESSAGE into an IMAGE"""
    success = encode_image(image, output, message)
    if success:
        click.echo(f"Message encoded into {output}")

@cli.command()
@click.argument('image')
def decode(image):
    """Decode and reveal hidden message from an IMAGE"""
    message = decode_image(image)
    click.echo(f"Hidden message: {message}")

if __name__ == '__main__':
    cli()
