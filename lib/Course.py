class Course:
    def __init__(self, title="", schedule="", description=""):  # initialize default ("") values to pass the test
        self.title = title
        self.schedule = schedule
        self.description = description
        
    def __str__(self):
        output = ''
        output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n'
        output += '------------------'
        return output

# To use the Courses class above:
    
# def main():
#     course = Course(title="Programming Robots for Outer Space", schedule="Full-Time", description="Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover")
#     print(course)

# main()
