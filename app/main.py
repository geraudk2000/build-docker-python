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

    
    # tempfile.mkdtemp(): This function creates a new temporary directory and returns the path to that directory.
    tmp_dir = tempfile.mkdtemp()
    # This function copies a file from the source path (src) to the destination path (dst).
    shutil.copy(command, tmp_dir)
    # This function changes the root directory of the current process to the directory specified by path.
    os.chroot(tmp_dir)

    # os.path.basename(path): This function returns the final component of a pathname. For example, given a path "/path/to/file", it would return "file".
    # This function joins one or more path components intelligently. The first argument is the initial part of the path, and subsequent arguments are appended to it.
    command = os.path.join("/", os.path.basename(command))

    # This function runs the command described by command and args
    completed_process = subprocess.run([command, *args], capture_output=True)
    # Writes the captured standard output and error output of the command to the standard output stream of the Python script.
    sys.stdout.buffer.write(completed_process.stdout)
    sys.stderr.buffer.write(completed_process.stderr)

    # exits the script with the same return code as the subprocess
    sys.exit(completed_process.returncode)
   
if __name__ == "__main__":
    main()
