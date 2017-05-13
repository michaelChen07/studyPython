# encoding=utf-8
from multiprocessing import Process, Manager

def f( shareDict, shareList ):
    shareDict[1] = '1'
    shareDict['2'] = 2
    shareDict[0.25] = None
    shareList.reverse() # 翻转列表

if __name__ == '__main__':
    manager = Manager()
    shareDict = manager.dict() # 创建共享的字典类型
    shareList = manager.list( range( 10 ) ) # 创建共享的列表类型
    p = Process( target = f, args = ( shareDict, shareList ) )
    p.start()
    p.join()
    print shareDict
    print shareList
