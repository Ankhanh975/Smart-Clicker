import time
def Sleep(duration): #High accurate sleep
    now = time.perf_counter()
    end = now + duration
    while now < end:
        if end-now >= 1/61:
            time.sleep(1/1000)
        now = time.perf_counter()


def SmallestRunFPS(List):
    # List is a list of n number to find GCD
    def GCD(a, b):
        if a%b==0:
            return b
        else:
            return GCD(b, a % b)

    def GCDn(list):
        g = GCD(List[0], List[1])
        for i in range(2, len(List)):
            g=GCD(g, List[i])
        return g

    return GCDn(List)

