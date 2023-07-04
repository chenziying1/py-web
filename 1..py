import random
import tkinter as tk

# 定义游戏规则
RULES = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

# 创建主窗口
root = tk.Tk()
root.title("Rock Paper Scissors")

# 创建标签和按钮
choice_label = tk.Label(root, text="Choose rock, paper or scissors:")
rock_button = tk.Button(root, text="Rock")
paper_button = tk.Button(root, text="Paper")
scissors_button = tk.Button(root, text="Scissors")
play_again_button = tk.Button(root, text="Play again", state=tk.DISABLED)
quit_button = tk.Button(root, text="Quit")

# 布局
choice_label.pack()
rock_button.pack(side=tk.LEFT, padx=5, pady=10)
paper_button.pack(side=tk.LEFT, padx=5, pady=10)
scissors_button.pack(side=tk.LEFT, padx=5, pady=10)
play_again_button.pack(side=tk.LEFT, padx=5, pady=10)
quit_button.pack(side=tk.RIGHT, padx=5, pady=10)

# 定义按钮点击事件
def play(player_choice):
    # 禁用出拳按钮，启用再来一局和退出按钮
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)
    play_again_button.config(state=tk.NORMAL)
    quit_button.config(state=tk.NORMAL)

    # 玩家出拳
    if player_choice == 'rock':
        player_choice_label.config(text="You choose rock")
    elif player_choice == 'paper':
        player_choice_label.config(text="You choose paper")
    else:
        player_choice_label.config(text="You choose scissors")

    # 电脑出拳
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    computer_choice_label.config(text="Computer chooses " + computer_choice)

    # 判断胜负
    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif RULES[player_choice] == computer_choice:
        result_label.config(text="You win!")
    else:
        result_label.config(text="You lose!")

def play_rock():
    play('rock')

def play_paper():
    play('paper')

def play_scissors():
    play('scissors')

def play_again():
    # 启用出拳按钮，禁用再来一局和退出按钮
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)
    play_again_button.config(state=tk.DISABLED)
    quit_button.config(state=tk.DISABLED)

    # 清空标签内容
    player_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")

def quit_game():
    root.quit()

# 创建标签
player_choice_label = tk.Label(root, text="")
computer_choice_label = tk.Label(root, text="")
result_label = tk.Label(root, text="")

# 布局
player_choice_label.pack()
computer_choice_label.pack()
result_label.pack()

# 绑定按钮事件
rock_button.config(command=play_rock)
paper_button.config(command=play_paper)
scissors_button.config(command=play_scissors)
play_again_button.config(command=play_again)
quit_button.config(command=quit_game)

# 进入主
root.mainloop()