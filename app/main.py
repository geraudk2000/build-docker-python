import subprocess
import sys
import tempfile
import shutil
import os

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    command = sys.argv[3]
    args = sys.argv[4:]

    
    
    tmp_dir = tempfile.mkdtemp()
    shutil.copy(command, tmp_dir)
    os.chroot(tmp_dir)
    command = os.path.join("/", os.path.basename(command))

    # This function runs the command described by command and args
    completed_process = subprocess.run([command, *args], capture_output=True)
    # Writes the captured standard output and error output of the command to the standard output stream of the Python script.
    sys.stdout.buffer.write(completed_process.stdout)
    sys.stderr.buffer.write(completed_process.stderr)
    sys.exit(completed_process.returncode)
   
if __name__ == "__main__":
    main()
