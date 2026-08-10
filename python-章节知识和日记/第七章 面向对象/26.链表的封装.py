


    def __get_index(self,index):
        _index = index
        if index < 0:
            #将 负索引 转成 正索引
            _index  = self.__size + index
        #检查 索引的取值范围
        if _index < 0 or _index >= self.__size:
            raise IndexError(f'索引{index }超出范围')
        #返回 计算后的正索引
        return  _index

    def __get_node(self,index):
        """获取指定索引位置的节点"""
        #检查 索引的取值范围、并返回正索引
        _index = self.__get_index(index)
        #判断 索引 是否超出了 长度的一半
        if _index <= self.__size >>1 :
            #获取 第一个节点
            node = self.__head
            #