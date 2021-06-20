from hashlib import sha256
import time

def _SHA256(val):
    return sha256(val.encode()).hexdigest()

def mine(transactions,previous_hash,difficutly):
    prefix_zeros = '0'*difficutly
    nonce = 0
    while True:
        nonce += 1
        val = transactions + previous_hash + str(nonce)
        hash = _SHA256(val)
        if(hash.startswith(prefix_zeros)):
            print(f"Nonce bulundu: {nonce}")
            return hash

def main():
    difficulty = 4
    transactions = '' #oluşan oluşturulan hash kodu 64 lük
    previous_hash = '' #hash numaran
    start_time = time.time()
    print('Mining Basladi....')
    hash = mine(transactions,previous_hash,difficulty)
    total_time = str(time.time() - start_time)
    print(f"Mining {total_time} surede bulundu")
    print(f"Hash : {hash}")

main()