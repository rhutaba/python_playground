import argparse

parser = argparse.ArgumentParser(
        prog='argparseTest.py', # プログラム名
        usage='Demonstration of argparser', # プログラムの利用方法
        description='description', # 引数のヘルプの前に表示
        epilog='end', # 引数のヘルプの後で表示
        add_help=True, # -h/–help オプションの追加
    )

# 引数の追加実装
parser.add_argument('-v', '--verbose', help='select mode', action='store_true')
parser.add_argument('i', help='integer', type=int)
# 引数を解析する
args = parser.parse_args()

if args.verbose:
    if args.i & 2 == 1:
        print(str(args.i) + ' : Odd')
    else:
        print(str(args.i) + ' : Even')
else:
    if args.i % 2 == 1:
        print(str(args.i) + ' : 奇数')
    else:
        print(str(args.i) + ' : 偶数')
