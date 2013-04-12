'''
Created on 8 avr. 2013

lit un fichier et l'execute comme s'il était lu sur la console

repris de : http://pydoc.net/Python/coverage/3.3/coverage.execfile/

!!!! CE FICHIER N'EST PAS ENCORE AU POINT !!!!!!!!!!!
!!!! POUR L'INSTANT, UTILISER PLUTOT simpleRunFile  !!!!!!!!!!

@author: francois
'''
import imp, os, sys

MAINPATH = "/media/KeyBeuvron/beuvron/cours/modP3D/programmes/pyBlenderLinuxWorkspace/modP3D/src/"

SCRIPT = "modP3D/utilsBlender/primitivesGeometriques.py"  

class CoverageException(Exception):
    """An exception specific to Coverage."""
    pass

class NoSource(CoverageException):
    """Used to indicate we couldn't find the source for a module."""
    pass

class ExceptionDuringRun(CoverageException):
    """An exception happened while running customer code.

    Construct it with three arguments, the values from `sys.exc_info`.

    """
    pass

try:
    # In Py 2.x, the builtins were in __builtin__
    BUILTINS = sys.modules['__builtin__']
except KeyError:
    # In Py 3.x, they're in builtins
    BUILTINS = sys.modules['builtins']


def run_python_file(filename, args):
    """Run a python file as if it were the main program on the command line.

    `filename` is the path to the file to execute, it need not be a .py file.
    `args` is the argument array to present as sys.argv, including the first
    element representing the file being executed.

    """
    # Create a module to serve as __main__
    old_main_mod = sys.modules['__main__']
    main_mod = imp.new_module('__main__')
    sys.modules['__main__'] = main_mod
    main_mod.__file__ = filename
    main_mod.__builtins__ = BUILTINS

    # Set sys.argv and the first path element properly.
    old_argv = sys.argv
    old_path0 = sys.path[0]
    sys.argv = args
    sys.path[0] = os.path.dirname(filename)

    try:
        # Open the source file.
        try:
            source = open(filename, 'rU').read()
        except IOError:
            raise NoSource("No file to run: %r" % filename)

        # We have the source.  `compile` still needs the last line to be clean,
        # so make sure it is, then compile a code object from it.
        if source[-1] != '\n':
            source += '\n'
        code = compile(source, filename, "exec")

        # Execute the source file.
        try:
            exec(code, main_mod.__dict__)
        except:
            # Something went wrong while executing the user code.
            # Get the exc_info, and pack them into an exception that we can
            # throw up to the outer loop.  We peel two layers off the traceback
            # so that the coverage.py code doesn't appear in the final printed
            # traceback.
            typ, err, tb = sys.exc_info()
            raise ExceptionDuringRun(typ, err, tb.tb_next.tb_next)
    finally:
        # Restore the old __main__
        sys.modules['__main__'] = old_main_mod

        # Restore the old argv and path
        sys.argv = old_argv
        sys.path[0] = old_path0

if __name__ == "__main__":
    run_python_file(SCRIPT,[])
