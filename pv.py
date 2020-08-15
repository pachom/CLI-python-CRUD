import click  # framework for create a command line aplications

from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'


@click.group()
@click.pass_context
def cli(ctx):    #This function is the entry point. 
                 #To do this we use de @click.group decorator.
                 #Also use de decorator @click.pass_context to obtain an object context ctx
    ctx.obj = {}  # initialize the context object with an empty dictionary
    ctx.obj['clients_table'] = CLIENTS_TABLE

cli.add_command(clients_commands.all)
