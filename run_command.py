import io
import time
import subprocess
import sys

def run(command, filename, widget=None):

    filename = "logs/"+filename
    if widget != None:
        widget.config(state='normal')
        widget.delete(1.0, 'end')

    with io.open(filename, 'wb') as writer, io.open(filename, 'rb') as reader:
        process = subprocess.Popen(command, stdout=writer)

        while process.poll() is None:
            outline = reader.read().decode("utf-8").replace("[K", "\n")
            sys.stdout.write(outline)

            if widget != None:
                widget.insert('end', outline)
                widget.see('end')

            time.sleep(0.5)

        # Read the remaining
        outline = reader.read().decode("utf-8").replace("[K", "\n")
        sys.stdout.write(outline)

        if widget != None:
                widget.insert('end', outline)
                widget.see('end')
                widget.config(state='disabled')

