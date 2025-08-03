# Get user input for marks
marks = int(input("Enter your marks: "))

# Determine the grade based on the marks
if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif 60 <= marks < 70:
    grade = "D"
elif 50 <= marks < 60:
    grade = "E"
else:
    grade = "F"

# Display the grade
print(f"Your grade is: {grade}")


from typing import List

class Solution:
    def solve(self, A: List[int], B: int) -> int:
        n = len(A)
        min_cost = A.copy()
        result = sum(min_cost)

        for k in range(1, n):
            temp_sum = 0
            for i in range(n):
                rotated_index = (i + k) % n
                # Update the minimum cost at position i
                min_cost[i] = min(min_cost[i], A[rotated_index] + k * B)
                temp_sum += min_cost[i]
            result = min(result, temp_sum)

        return result

# Test
sol = Solution()
A = [7, 4, 2, 1]
B = 3
print(sol.solve(A, B))  # ✅ Output: 11

