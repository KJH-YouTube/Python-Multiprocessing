class SMT(object):
    def __init__(self) -> None:
        self._something = True
        return
    
    def __enter__(self):
        print('open')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('close')
        return


class TEMP(SMT):
    __all__ = ['val']

    def __init__(self) -> None:
        self.val = True
        return


if __name__ == '__main__':
    t = TEMP()
    with TEMP() as t:
        print(t.val)