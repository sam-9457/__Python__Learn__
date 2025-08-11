import random, time

def printt():
    print("Premium lua language provide!")
    print("Loading")
    time.sleep(1)
    a = ["local", "function", "for", "while"]
    b = ["num", "random", "part", "i"]
    c = ["=", "()", "in", "true"]
    d = ["workspace", "", "pairs", "do"]
    e = ["", "", "(folder:GetChildren()) do", ""]
    for r in range(10):
        ai1 = random.randint(0,3)
        ai2 = random.randint(0,3)
        ai3 = random.randint(0,3)
        ai4 = random.randint(0,3)
        ai5 = random.randint(0,3)
        print(f"\n{a[ai1]} {b[ai2]} {c[ai3]} {d[ai4]} {e[ai5]}")
        time.sleep(.3)
printt()