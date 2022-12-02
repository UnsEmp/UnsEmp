from werkzeug.datastructures import FileStorage
from Block import Block
from PerInf import PersonalInformation
from PerInf import PersonalInformationEncoder
import time
import json
from flask import Flask, jsonify, request
import os
import pytrie


class BlockChain:
    def __init__(self):
        # 初始化链，添加创世区块
        self.chain = [self._create_genesis_block()]
        # 设置初始难度
        self.difficulty = 3
        # # 用户信息
        # self.personalinformation = []

    @staticmethod
    def _create_genesis_block():
        '''
        生成创世区块
        :return: 创世区块
        '''
        timestamp = time.mktime(time.strptime('2018-06-11 00:00:00', '%Y-%m-%d %H:%M:%S'))
        block = Block(0, timestamp, [], '')
        return block

    def get_latest_block(self):
        '''
        获取链上最后一个也是最新的一个区块
        :return:最后一个区块
        '''
        return self.chain[-1]

    def add_personalInformation(self, personal):
        # 添加用户文件著作信息
        block = Block(self.chain[-1].index + 1, self.chain[-1].name, time.time(), personal, self.chain[-1].hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)

        # 将该用户的文件hash值存储到字典树中
        t.__setitem__(block.hash, block.index)

    def verify_blockchain(self):
        '''
        校验区块链数据是否完整 是否被篡改过
        :return: 校验结果
        '''
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]  # 当前遍历到的区块
            previous_block = self.chain[i - 1]  # 当前区块的上一个区块
            if current_block.hash != current_block.calculate_hash():
                # 如果当前区块的hash值不等于计算出的hash值，说明数据有变动
                return False
            if current_block.previous_hash != previous_block.calculate_hash():
                # 如果当前区块记录的上个区块的hash值不等于计算出的上个区块的hash值 说明上个区块数据有变动或者本区块记录的上个区块的hash值被改动
                return False
        return True


app = Flask(__name__, static_url_path='/file', static_folder='static')
blockChain = BlockChain()
t = pytrie.Trie()


@app.route('/', methods=['GET'])
def get_blockchain():
    arr = []
    for chain in blockChain.chain:
        l = {"index": chain.index, "timestamp": chain.timestamp, "current_hash": chain.hash,
             "previous_hash": chain.previous_hash}
        arr.append(l)
    return jsonify(arr)


@app.route('/', methods=['POST'])
def check():
    ha = request.values['hash']
    if request.values['method'] == 1:
        key = t.longest_prefix_value(ha, default=-1)
        # print(key)
        # print(blockChain.chain[key].hash)
        if key == -1 or blockChain.chain[key].hash != ha:
            return jsonify({'status': 'Not your file !'})

        li = {"name": request.values['name'],
              "index": blockChain.chain[key].index,
              "timestamp": blockChain.chain[key].timestamp,
              "current_hash": blockChain.chain[key].hash,
              "previous_hash": blockChain.chain[key].previous_hash}
        return jsonify(li)
    else:
        key = -1
        for chain in blockChain.chain:
            if chain.hash == ha:
                key = chain.index
                break

        if key == -1 or blockChain.chain[key].hash != ha:
            return jsonify({'status': 'Not your file !'})

        li = {"name": request.values['name'],
              "index": blockChain.chain[key].index,
              "timestamp": blockChain.chain[key].timestamp,
              "current_hash": blockChain.chain[key].hash,
              "previous_hash": blockChain.chain[key].previous_hash}
        return jsonify(li)


@app.route('/upload/', methods=['POST'])
def upload():
    # file1 = requests_file.FileAdapter.__getattribute__('file1')
    file1: FileStorage = request.files.get('file1')

    # save file
    file1.save(f'static/{file1.filename}')
    print(str(os.path.abspath('static')) + str(f'/{file1.filename}'))
    blockChain.add_personalInformation(PersonalInformation(request.values['name'], time.strftime('%Y/%m/%d %H:%M'),
                                                           str(os.path.abspath('static')) + str(f'/{file1.filename}')))
    return jsonify({'status': 'ok', 'hash': blockChain.chain[-1].hash})


if __name__ == '__main__':
    app.run(debug=True, host='127.1.1.1', port=5000)