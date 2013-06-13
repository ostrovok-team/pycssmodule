import os.path
from subprocess import check_call

def compile(module, js_ns_prefix, source_folder, target_folder, production_source_folder):
    cdir = os.path.abspath(os.path.dirname(__file__))
    cssmoduledir = os.path.join(cdir, 'cssmodule/bin/cssmoduledir')

    cmd = [
        cssmoduledir,
        js_ns_prefix,
        source_folder,
        target_folder,
        production_source_folder
    ]

    print "Running cssmodule: ", ' '.join(cmd)
    check_call(cmd)
    print "Done"

