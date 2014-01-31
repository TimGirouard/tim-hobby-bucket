import threading
import winsound
def action1():
    print("We are being attacked!")
def alarm():
    # 500 hz sound for 9 seconds
    winsound.Beep(500, 9000)
def action2():
    print("Wake up our troops!")
def action3():
    print("Our troops are ready!")
# after 0.1 seconds do action1
t1 = threading.Timer(0.1, action1)
# after 3.5 seconds do action2
# and after 10.0 seconds do action3
t2 = threading.Timer(3.5, action2)
t3 = threading.Timer(10.0, action3)
# this will wake the troops after action2 has been called
t4 = threading.Timer(4.5, alarm)
t1.start()
t2.start()
t3.start()
#t4.start()
