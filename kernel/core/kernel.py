class Kernel:

    def __init__(self):
        self.started = False

    def boot(self):
        self.started = True
        print("[KERNEL] Sistema iniciado")

    def shutdown(self):
        self.started = False
        print("[KERNEL] Sistema apagado")


kernel = Kernel()
