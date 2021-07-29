import argparse
import requests
import json
from prettytable import PrettyTable


class Quake_360:
    key = '932d86eb-cb01-4a52-ae8e-c94db51cb77f'

    # 搜索模块
    def Search(self, key, search, size, page):
        headers = {"X-QuakeToken": key}

        data = {
            "query": search,
            "start": page,
            "size": '2'
        }
        print(search)
        response = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
        r_json = json.loads(response.text)
        # print(r_json)
        self.Print_search(r_json, page, size)

    def Print_search(self, r_json, page, size):
        print("\n")
        print("页码：第{}页  共{}页  数量：{}个".format(r_json['meta']['pagination']['page_index'], r_json['meta']['pagination']['page_size'], r_json['meta']['pagination']['total']))

    # 版权信息
    def Copyright(self):
        bn = """
               _____ _____ ____     ____              __           ___    ____  _ 
              |__  // ___// __ \   / __ \__  ______ _/ /_____     /   |  / __ \(_)
               /_ </ __ \/ / / /  / / / / / / / __ `/ //_/ _ \   / /| | / /_/ / / 
             ___/ / /_/ / /_/ /  / /_/ / /_/ / /_/ / ,< /  __/  / ___ |/ ____/ /  
            /____/\____/\____/   \___\_\__,_/\__,_/_/|_|\___/  /_/  |_/_/   /_/    
            author: Xc1Ym
            github: https://github.com/Xc1Ym/360_quake_api
            """
        print(bn)
        self.Terminal()

    # 命令行查询
    def Terminal(self):
        parser = argparse.ArgumentParser(
            description="e.g：python quake_api.py --search IP or domain\t python quake_api.py --search \"domain=xx.com\" or \"city=Beijing\"",
            prog="quake_api.py")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--version", "-V", help="Show version of 360 quake api", action='version',
                           version="| %(prog)s v1.0 |")
        group.add_argument("--search", "-S", help="Search key word", type=str)
        parser.add_argument("--size", help="Show the number of results.(default=100)", default=100)
        parser.add_argument("--page", help="Show the page of results.(default=1)", default=1)
        # parser.add_argument('word_search', help="search key word")
        args = parser.parse_args()
        if args.search:
            self.Search(self.key, args.search, args.size, args.page)


# main
if __name__ == '__main__':
    Quake_360().Copyright()
