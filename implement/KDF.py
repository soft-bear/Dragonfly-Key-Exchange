import hashlib

def dev(base,p):
    n = len(list(map(int,format(p,"b"))))+ 64
    string = base + "Dragonfly Hunting And Pecking"
    H = int(hashlib.shake_256(string.encode()).hexdigest(n), 16)

    S = format(H, 'x')
    assert('0x' + S == hex(H))
    assert (type(H) == int)
    return S
def main(base, p):
    Ans  = dev(base, p)
    return Ans

if __name__ == "__main__":
    base = 'faaaaaa'
    p = 27
    main(base,p)