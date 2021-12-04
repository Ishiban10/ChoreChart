from random import randint  # need to import randint from random

# creates the class for ChoreChart
class ChoreChart:
    chores_list = ["Upper Bathroom", "Lower Bathroom", "Kitchen", "Surfaces", "Floors", "Free"]. # class variable
    def __init__(self, names, weeks):  # takes in two user inputs of number of weeks and a list of names
        self.__weeks = weeks
        self.__names = names

    def set_freeweeklist(self):  # first set method for self.__freeweeklist
        self.__freeweeklist = []

    def set_choresweeklist(self):  # second set method self.__choresweeklist
        self.__choresweekslist = []

    # first method that generates a chore for each person in the inputted names list and states who has a free week
    def choreweeklistgenerator(self):
        self.__freeweekcounter = {}
        for i in range(1, self.__weeks + 1):
            self.__choresassigned = {}
            for name in self.__names:
                while True:
                    self.__chore = self.chores_list[randint(0, len(self.chores_list) - 1)]
                    if self.__chore in self.__choresassigned.values():
                        continue
                    else:
                        self.__choresassigned[name] = self.__chore
                        break
            for item in self.__choresassigned.keys():
                if self.__choresassigned[item] == "Free":
                    self.__free = f"{item} has a free week."  # saves who has a free week to self.__free
            counter = 1
            for key in self.__choresassigned.keys():
                if self.__choresassigned[key] == "Free":
                    if key in self.__freeweekcounter:
                        self.__freeweekcounter[key] += 1  # adds one to the counter for free weeks for each person
                    else:
                        self.__freeweekcounter[key] = counter
            # adds the chore list for the week to the list self.__choresweekslist
            self.__choresweekslist.append(f"Week {i}: {self.__choresassigned}")
            # adds the who has a free week to the list self.__freeweeklist
            self.__freeweeklist.append(f"Week {i}: {self.__free}")

    # second method that returns the number of free weeks people have
    def finalfreeweekcounter(self):
        self.__finalfreeweekcounter = []
        for key in self.__freeweekcounter:
            self.__finalfreeweekcounter.append(f"{key} has {self.__freeweekcounter[key]} week(s) off.")
        return "\n".join(self.__finalfreeweekcounter)

    def get_choresweekslist(self):  # first get method for self.__choresweeklist
        return "\n".join(self.__choresweekslist)

    def get_freeweeklist(self):  # second get method for self.__freeweeklist
        return "\n".join(self.__freeweeklist)


def main():
    # sets chore equal to the class ChoreChart with an inputted list of names and the number of weeks to generates the
    # chores for
    chore = ChoreChart(["Ishaan", "Rahul", "Anthony", "Seb", "Christian", "Rikuu"], 6)
    chore.set_freeweeklist()  # runs the method set_freeweeklist from class ChoreChart
    chore.set_choresweeklist()  # runs the method set_choresweeklist from class ChoreChart
    chore.choreweeklistgenerator()  # runs the method choreweeklistgenerator from class ChoreChart
    # runs and prints the output from the method get_choresweeklist from class ChoreChart
    print(chore.get_choresweekslist())
    print(chore.get_freeweeklist())  # runs and prints the output from the method get_freeweeklist from class ChoreChart
    # runs and prints the output from the method finalfreeweekcounter from class ChoreChart
    print(chore.finalfreeweekcounter())


# runs the main function
if __name__ == "__main__":
    main()
