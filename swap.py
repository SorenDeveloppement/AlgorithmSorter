def swap(_list: list, item1: any, item2: any) -> list:
    _list[_list.index(item1)], _list[_list.index(item2)] = _list[_list.index(item2)], _list[_list.index(item1)]
    
    return _list