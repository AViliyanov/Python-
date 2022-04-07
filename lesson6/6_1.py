import time


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self):
        while True:
            time.sleep(7)
            if TrafficLight.__color[0] == "Red":
                print(TrafficLight.__color[0])
                time.sleep(2)
            if TrafficLight.__color[1] == "Yellow":
                print(TrafficLight.__color[1])
                time.sleep(2)
            if TrafficLight.__color[2] == "Green":
                print(TrafficLight.__color[2])
                time.sleep(7)
            if TrafficLight.__color[0] == "Red":
                print(TrafficLight.__color[0])
                break


total = TrafficLight()

total.running()
