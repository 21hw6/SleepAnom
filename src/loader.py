import urllib.request
import regex as re

def load_data():
    url="https://download.scidb.cn/download?fileId=62295e16d7561b594fb67f58&path=/V3/APNEA_RML/00001631-100507.rml&fileName=00001631-100507.rml"
    urllib.request.urlretrieve(url, "00001631-100507.rml")

def main():
    load_data()

if __name__ == "__main__":
    main()