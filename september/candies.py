class Solution:
    def distributeCandies(self,
                    candies: int,
                    num_people: int) -> list:
        people = [0] * num_people
        people[0] = 1
        candz = candies
        while True:
            for i in range(len(people)):
                if candz <= 0:
                    break
                people[i] = people[i - 1] + 1
                candz -= people[i]
                print(people, candz)
            if candz < 0:
                break
        return people

if __name__ == '__main__':
    sol = Solution()
    print(sol.distributeCandies(7, 4))
    print(sol.distributeCandies(10, 3))
        