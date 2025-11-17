class Robot:
    def __init__(self, name = " "):
        self.name = name
        # print(self)
        # self.walking = False
        # self.speed = 10
        self.type = "drone"
        self.mass_grams = 249

    def say_hello(self):
        print(f"Hello, I'm {self.name}!")
        print(f"I'm a {self.type}")
        print(f"I have a mass of {self.mass_grams}g")
        print(self.__dict__)
              
    # print(self)
    # def walk(self, camina):
    #     self.walking = camina
    #     if self.walking:
    #         return "Esta caminando"
    #     else:
    #         return "No esta caminando"

miRobot = Robot("William")
# miRobot2 = Robot("WALL-E")
# # miRobot3 = Robot()
# print(miRobot)
# print(miRobot2)
# print(miRobot3)
miRobot.say_hello()
# miRobot2.say_hello()
# print(miRobot.walk(True))
# miRobot.speed += 10
# print(miRobot.speed)

# my_robot_army = [Robot() for _ in range(3)]
# print(my_robot_army)


# my_robot_army = []
# for _ in range(1_000):
#     new_robot = Robot()
# my_robot_army.append(new_robot)
# print(my_robot_army)
