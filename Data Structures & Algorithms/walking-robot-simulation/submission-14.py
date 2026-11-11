class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        def move(direction, x, y):
            if direction == 0:
                return x, y + 1
            elif direction == 1:
                return x + 1, y
            elif direction == 2:
                return x, y - 1
            elif direction == 3:
                return x - 1, y

        furthest = 0
        x, y = 0, 0
        direction = 0
        for command in commands:
            if command > 0:
                steps = command
                for step in range(steps):
                    new_cord = move(direction, x, y)
                    v, w = new_cord
                    if [v, w] not in obstacles:
                        x, y = new_cord
                        furthest = max(furthest, x*x + y*y)
                    else:
                        break
            elif command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4

        print(x,y)

        return furthest

            

            


