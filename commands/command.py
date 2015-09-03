# -*- coding: utf-8 -*-
"""
Commands

Commands describe the input the player can do to the game.

"""

from evennia import Command as BaseCommand
from evennia import default_cmds



class Command(BaseCommand):
    """
    Inherit from this if you want to create your own
    command styles. Note that Evennia's default commands
    use MuxCommand instead (next in this module).

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    """
    # these need to be specified

    key = "MyCommand"
    aliases = []
    locks = "cmd:all()"
    help_category = "General"

    # optional
    # auto_help = False      # uncomment to deactive auto-help for this command.
    # arg_regex = r"\s.*?|$" # optional regex detailing how the part after
                             # the cmdname must look to match this command.

    # (we don't implement hook method access() here, you don't need to
    #  modify that unless you want to change how the lock system works
    #  (in that case see evennia.commands.command.Command))

    def at_pre_cmd(self):
        """
        This hook is called before `self.parse()` on all commands.
        """
        pass

    def parse(self):
        """
        This method is called by the `cmdhandler` once the command name
        has been identified. It creates a new set of member variables
        that can be later accessed from `self.func()` (see below).

        The following variables are available to us:
           # class variables:

           self.key - the name of this command ('mycommand')
           self.aliases - the aliases of this cmd ('mycmd','myc')
           self.locks - lock string for this command ("cmd:all()")
           self.help_category - overall category of command ("General")

           # added at run-time by `cmdhandler`:

           self.caller - the object calling this command
           self.cmdstring - the actual command name used to call this
                            (this allows you to know which alias was used,
                             for example)
           self.args - the raw input; everything following `self.cmdstring`.
           self.cmdset - the `cmdset` from which this command was picked. Not
                         often used (useful for commands like `help` or to
                         list all available commands etc).
           self.obj - the object on which this command was defined. It is often
                         the same as `self.caller`.
        """
        pass

    def func(self):
        """
        This is the hook function that actually does all the work. It is called
        by the `cmdhandler` right after `self.parser()` finishes, and so has access
        to all the variables defined therein.
        """
        self.caller.msg("Command called!")

    def at_post_cmd(self):
        """
        This hook is called after `self.func()`.
        """
        pass


class MuxCommand(default_cmds.MuxCommand):
    """
    This sets up the basis for Evennia's 'MUX-like' command style.
    The idea is that most other Mux-related commands should
    just inherit from this and don't have to implement parsing of
    their own unless they do something particularly advanced.

    A MUXCommand command understands the following possible syntax:

        name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]

    The `name[ with several words]` part is already dealt with by the
    `cmdhandler` at this point, and stored in `self.cmdname`. The rest is stored
    in `self.args`.

    The MuxCommand parser breaks `self.args` into its constituents and stores them
    in the following variables:
        self.switches = optional list of /switches (without the /).
        self.raw = This is the raw argument input, including switches.
        self.args = This is re-defined to be everything *except* the switches.
        self.lhs = Everything to the left of `=` (lhs:'left-hand side'). If
                     no `=` is found, this is identical to `self.args`.
        self.rhs: Everything to the right of `=` (rhs:'right-hand side').
                    If no `=` is found, this is `None`.
        self.lhslist - `self.lhs` split into a list by comma.
        self.rhslist - list of `self.rhs` split into a list by comma.
        self.arglist = list of space-separated args (including `=` if it exists).

    All args and list members are stripped of excess whitespace around the
    strings, but case is preserved.
    """

    def func(self):
        """
        This is the hook function that actually does all the work. It is called
        by the `cmdhandler` right after `self.parser()` finishes, and so has access
        to all the variables defined therein.
        """
        # this can be removed in your child class, it's just
        # printing the ingoing variables as a demo.
        super(MuxCommand, self).func()
from evennia import Command

class CmdSmile(Command):
        """
        A smile command

        Usage: 
          smile [at] [<someone>]
          grin [at] [<someone>] 

        Smiles to someone in your vicinity or to the room
        in general.

        (This initial string (the __doc__ string)
        is also used to auto-generate the help 
        for this command)
        """ 

        key = "smile"
        aliases = ["приветик", "grin at"] 
        locks = "cmd:all()"
        help_category = "General"

        def parse(self):
            "Very trivial parser" 
            self.target = self.args.strip() 

        def func(self):
            "This actually does things"
            caller = self.caller
            if not self.target or self.target == "here":
                string = "%s smiles." % caller.name
                caller.location.msg_contents(string, exclude=caller)
                caller.msg("You smile.")
            else:
                target = caller.search(self.target)
                if not target: 
                    # caller.search handles error messages
                    return
                string = "%s smiles to you." % caller.name
                target.msg(string)
                string = "You smile to %s." % target.name
                caller.msg(string)
                string = "%s smiles to %s." % (caller.name, target.name)           
                caller.location.msg_contents(string, exclude=[caller,target])




class CmdFap(Command):
        """
        A smile command

        Usage: 
          smile [at] [<someone>]
          grin [at] [<someone>] 

        Smiles to someone in your vicinity or to the room
        in general.

        (This initial string (the __doc__ string)
        is also used to auto-generate the help 
        for this command)
        """ 

        key = "фап"
        aliases = ["фап-фап"] 
        locks = "cmd:all()"
        help_category = "General"

        def parse(self):
            "Very trivial parser" 
            self.target = self.args.strip() 

        def func(self):
            "This actually does things"
            caller = self.caller
            if not self.target or self.target == "here":
                string = "%s фапает." % caller.name
                caller.location.msg_contents(string, exclude=caller)
                caller.msg("Ты фапаешь")
            else:
                target = caller.search(self.target)
                if not target: 
                    # caller.search handles error messages
                    return
                string = "%s фапает на тебя." % caller.name
                target.msg(string)
                string = "Ты фапаешь на %s." % target.name
                caller.msg(string)
                string = "%s фапает на %s." % (caller.name, target.name)           
                caller.location.msg_contents(string, exclude=[caller,target])





from evennia import create_object

class CmdCreateNPC(Command):
    """
    create a new npc

    Usage:
    +createNPC <name>

    Creates a new, named NPC. The NPC will start with a Power of 1.
    """ 
    key = "+createnpc"
    aliases = ["+createNPC"]
    locks = "call:not perm(nonpcs)"
    help_category = "mush" 

    def func(self):
        "creates the object and names it"
        caller = self.caller
        if not self.args:
            caller.msg("Usage: +createNPC <name>")
            return
        if not caller.location:
            # may not create npc when OOC
            caller.msg("You must have a location to create an npc.")
            return
        # make name always start with capital letter
        name = self.args.capitalize()
        # create npc in caller's location
        npc = create_object("characters.Character", 
                      key=name, 
                      location=caller.location,
                      locks="edit:id(%i) and perm(Builders)" % caller.id)
        # announce 
        message = "%s created the NPC '%s'."
        caller.msg(message % ("You", name)) 
        caller.location.msg_contents(message % (caller.key, name), 
                                                exclude=caller)      
