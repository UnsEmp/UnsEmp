针对当前著作权保护时等级成本过高和登记证明效力低等问题，提出了一种基于区块链的文件著作保护系统。首先，用户上传一份文件由本地服务器接收到后，使用共识算法pow生成区块，区块包含当前区块的哈希值，前一个区块的哈希值以及生成区块的时间戳，引入Hash算法对用户数据进行单向数据Hash加密，通过与时间戳结合，构建不可篡改的区块链数据，然后再将得到的哈希值通过Gossip协议广播给每一位用户，并运用redis分布式数据库储存起来。且在查询用户文件的过程中，通过上传文件的hash值，运用字典树查询方式以方便用户查找。