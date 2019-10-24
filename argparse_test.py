import argparse

parser = argparse.ArgumentParser(
        prog='argparseTest.py', # プログラム名
        usage='Demonstration of argparser', # プログラムの利用方法
        description='description', # 引数のヘルプの前に表示
        epilog='end', # 引数のヘルプの後で表示
        add_help=True, # -h/–help オプションの追加
    )

# 引数の追加実装
parser.add_argument('mul', help='multiply', type=float, nargs=2)

# 引数を解析する
args = parser.parse_args()

n1 = args.mul[0]
n2 = args.mul[1]
calc = n1 * n2
print(str(n1) + ' x ' + str(n2) + ' = ' + str(calc))
