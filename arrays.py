def array_test():
    
    ar = [1,2,3,4]
    #項目数
    print("list size:",len(ar))
    #pop
    print("pop",ar.pop())
    #pop後
    print(ar)
    #is_empty
    if not str(ar):
        print("empty!")
    #indexで指定。なかった時の処理も
    try:
        print("index of 2",ar[2])
    except IndexError:
        print("ない！！！")
    #追加 appendはリスト自体を変更する破壊的メソッドでlist,appendはNoneTypeになる
    ar.append(4)
    print("append後",ar)
    #insert indexで指定し、そのインデックスと末尾の要素を右側にシフトさせる
    #prependの時はinsert(o,x)
    ar.insert(2,10)
    print("insert後",ar)
    #indexで指定し削除、左シフト
    del ar[1]
    print("delete後",ar)
    #値を探し、それを保持するindexを削除
    ar.remove(10)
    print("remove後",ar)
    #値を探し、それを持つindexを取得
    print("3の値を持つindex",ar.index(3))
    
    
def main():
    array_test()
       
if __name__ == "__main__":
    main()

