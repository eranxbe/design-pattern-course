class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance
