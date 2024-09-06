import time
import sys
sys.stdout = open("./file_per_le_print", "w+")

for i in range(10):
    time.sleep(3)
    sys.stdout.flush()
    print("pisello freestyle")

sys.stdout.close()