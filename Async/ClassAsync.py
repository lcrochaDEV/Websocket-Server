import asyncio

class AssyncExec:

    @classmethod
    async def __asyncfunction(self, args=None, kwargs=None):
        try:
            await asyncio.gather(*args, **kwargs)
        except:
            print("\033[91mErro ao Executar Ordem\033[0m")

    @classmethod
    def asyncAction(self, *args, **kwargs):
        asyncio.run(self.__asyncfunction(args, kwargs))