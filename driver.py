import subprocess
# ...
print("Moving files...")
subprocess.call(["./move_files.sh"], shell=True)
print("Processing files...")
subprocess.call('python to_plain.py', shell=True)
print("Collecting txts...")
subprocess.call(["./collect_txt.sh"], shell=True)
print("TDMifying plain text...")
subprocess.call('python tdm.py', shell=True)
print("Calling R!")
subprocess.call('python tdm.py', shell=True)
