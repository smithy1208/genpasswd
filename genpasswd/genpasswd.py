#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

import click


def randomStringDigits(stringLength=16):
    """Generate a random string of letters and digits"""
    lettersAndDigits = string.ascii_letters + string.digits
    return "".join(random.choice(lettersAndDigits) for i in range(stringLength))


@click.command()
@click.option("--length", "-l", default=20, help="Length of passwd.")
def cli(length):
    click.echo(randomStringDigits(length))


if __name__ == "__main__":
    cli()
