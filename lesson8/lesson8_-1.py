Main = [{"player": "Hi", "ai": "Hi"},
            {"player": "Hello", "ai": "Hello"},
            {"player": "How are you?", "ai": "I`m fine"}
        ]
def get_player(main:dict):
    return Main['player']

def get_ai(main:dict):
    return Main['ai']
def main():
    player_ = input("Input")
    player = get_player(Main)
    answer = get_ai(Main)