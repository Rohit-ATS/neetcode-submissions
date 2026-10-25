from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwich_index = 0
        skipped = 0

        while students and skipped < len(students):
            student = students.popleft()
            sandwich = sandwiches[sandwich_index]

            if student == sandwich:
                sandwich_index += 1
                skipped = 0
            
            else:
                students.append(student)
                skipped += 1
            
        return len(students)