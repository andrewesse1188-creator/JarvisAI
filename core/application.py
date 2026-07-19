from kernel.core.kernel import kernel


class JarvisApplication:

    def start(self):
        kernel.boot()

    def stop(self):
        kernel.shutdown()


app = JarvisApplication()
