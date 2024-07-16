vote_num = 0:
def vote():
    print("投票")
    global vote_num
    vote_num += 1

def reset_box():
    global vote_num
    print("空箱")
    vote_num = 0

def check_box():
    global vote_num
    print("票数是{}".format(vote_num))

vote()
check_box()
vote()
check_box()
for i in range():
    vote()
check_box()
reset_box()
check_box()
