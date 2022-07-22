import json
import time


class PersonalInformation:
    def __init__(self, _name, _time, _file):
        '''
        初始化交易
        :param _name: 姓名
        :param _time: 时间
        :param _file: 文件
        '''
        self._name = _name
        self._time = _time
        try:
            f = open(_file, 'r')
            self._file = str(_file)
        except FileNotFoundError:
            print("no find file %s !" % (str(_file).split('/')[-1]))
        except FileExistsError:
            print("Open file %s have fault !" % (str(_file).split('/')[-1]))


class PersonalInformationEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, PersonalInformation):
            return o.__dict__
        return json.JSONEncoder.default(self, o)


# if __name__ == '__main__':
#     # 测试
#     tran = PersonalInformation('jake', time.strftime('%Y/%m/%d %H:%M:%S'), "D:/MyPhone/1.jpg")
#     print(tran)
#     print(json.dumps(tran, ensure_ascii=False, cls=PersonalInformationEncoder))


