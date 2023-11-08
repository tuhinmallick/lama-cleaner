from loguru import logger


class BasePlugin:
    def __init__(self):
        if err_msg := self.check_dep():
            logger.error(err_msg)
            exit(-1)

    def __call__(self, rgb_np_img, files, form):
        ...

    def check_dep(self):
        ...
