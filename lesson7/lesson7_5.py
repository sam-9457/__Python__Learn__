import argparse

parser = argparse.ArgumentParser(description="猜數字遊戲")
parser.add_argument("-n", "--name",type=str, help = "姓名")
parser.add_argument("-f", "--frequency", type=int,help="玩的次數")
args = parser.parse_args()

if not args.name:
    name = input("請輸入姓名:")
else:
    name = args.name
freqency = args.frequency