import logging,os

from app.config import project_root


class Logger():
    _instance = None
    _initialized = False
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self,path= rf'./log/',logfile = 'AllLog.log'):
        if not Logger._initialized:
            self.logger = None
            self.set_path(path,logfile)
            Logger._initialized = True

    def set_path(self,path,logfile):
        if not os.path.exists(path):
            os.mkdir(path)
        self.loggerpath = path
        self.logfile = logfile
        #日志格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        c = logging.FileHandler(f'{self.loggerpath}/{self.logfile}', mode='a', encoding='utf8')
        self.logger = logging.getLogger('frame log')
        self.logger.setLevel(logging.DEBUG)
        c.setFormatter(formatter)
        self.logger.addHandler(c)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)


    # 打印debug级别日志
    def debug(self,str):
        logger = self.logger
        try:
            logger.debug(str)
            #print(str)
        except:
            return

    # 打印info级别日志
    def info(self,str):
        logger = self.logger
        try:
            logger.info(str)
            #print(str)
        except:
            return

    # 打印warn级别日志
    def warn(self,str):
        logger = self.logger
        try:
            logger.warning(str)
            #print(str)
        except:
            return

    # 打印error级别日志，错误日志增加！！！高亮显示
    def error(self,str):
        logger = self.logger
        try:
            logger.error(f'!!! {str}')
            #print(str)
        except:
            return

    # 打印异常日志，异常日志增加！！！高亮显示
    def exception(self,e):
        logger = self.logger
        try:
            logger.exception(f'!!! {e}')
            #print(str)
        except:
            return

logger = Logger(project_root)
# 调试
if __name__ == '__main__':
    logdrive = Logger('testlog.log')
    logdrive.debug('test debug')
    logdrive.info('test info')
    logdrive.warn('test warn')
    logdrive.error('test error')
    logdrive.exception('test exception')


