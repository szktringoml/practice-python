{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "list size: 4\n",
      "pop 4\n",
      "[1, 2, 3]\n",
      "index of 2 3\n",
      "append後 [1, 2, 3, 4]\n",
      "insert後 [1, 2, 10, 3, 4]\n",
      "delete後 [1, 10, 3, 4]\n",
      "remove後 [1, 3, 4]\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def array_test():\n",
    "    ar = [1,2,3,4]\n",
    "    #項目数\n",
    "    print(\"list size:\",len(ar))\n",
    "    #pop\n",
    "    print(\"pop\",ar.pop())\n",
    "    #pop後\n",
    "    print(ar)\n",
    "    #is_empty\n",
    "    if not str(ar):\n",
    "        print(\"empty!\")\n",
    "    #indexで指定。なかった時の処理も\n",
    "    try:\n",
    "        print(\"index of 2\",ar[2])\n",
    "    except IndexError:\n",
    "        print(\"ない！！！\")\n",
    "    #追加 appendはリスト自体を変更する破壊的メソッドでlist,appendはNoneTypeになる\n",
    "    ar.append(4)\n",
    "    print(\"append後\",ar)\n",
    "    #insert indexで指定し、そのインデックスと末尾の要素を右側にシフトさせる\n",
    "    #prependの時はinsert(o,x)\n",
    "    ar.insert(2,10)\n",
    "    print(\"insert後\",ar)\n",
    "    #indexで指定し削除、左シフト\n",
    "    del ar[1]\n",
    "    print(\"delete後\",ar)\n",
    "    #値を探し、それを保持するindexを削除\n",
    "    ar.remove(10)\n",
    "    print(\"remove後\",ar)\n",
    "    #値を探し、それを持つindexを取得\n",
    "    print(\"3の値を持つindex\",ar.index(3))\n",
    "    \n",
    "    \n",
    "def main():\n",
    "    array_test()\n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
