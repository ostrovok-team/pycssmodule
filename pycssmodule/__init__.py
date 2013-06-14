import os
import shutil
from subprocess import check_call

def install(target_dir):
    source_dir = os.path.abspath(os.path.dirname(__file__))
    source_dir = os.path.join(source_dir, 'cssmodule/client')
    shutil.rmtree(target_dir, ignore_errors=True)
    shutil.copytree(source_dir, target_dir)

def compile(js_ns_prefix, source_folder, target_folder, production_source_folder):
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

