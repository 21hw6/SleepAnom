import os
import re
import sys
import time
import pathlib
import argparse
import urllib.request

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.6+
    count = len(it)
    start = time.time() # time estimate start
    def show(j):
        x = int(size*j/count)
        # time estimate calculation and string
        remaining = ((time.time() - start) / j) * (count - j)        
        mins, sec = divmod(remaining, 60) # limited to minutes
        time_str = f"{int(mins):02}:{sec:03.1f}"
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count} Est wait {time_str}", end='\r', file=out, flush=True)
    show(0.1) # avoid div/0 
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

def get_dir_and_name(url):
    path = re.search(r'path=([^&]+)', url).group(1)
    name = path.split('/')[-1]
    dir = os.path.dirname(path)
    return dir, name

def load_data():
    for i in progressbar(range(15), "Downloading Dataset: ", 40):
        url="https://download.scidb.cn/download?fileId=62295e16d7561b594fb67f58&path=/V3/APNEA_RML/00001631-100507.rml&fileName=00001631-100507.rml"
        urllib.request.urlretrieve(url, "00001631-100507.rml")

def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("-f", "--file", type=str, default="data/778740145531650048.txt")
    args = arg.parse_args()

    data_urls = args.file

    load_data()
    test_dir = "data/V3/APNEA_RML/"
    os.makedirs(test_dir, exist_ok=True)

if __name__ == "__main__":
    main()