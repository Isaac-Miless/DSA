class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        stack = []
        for student in students:
            stack.append(student)
            while stack and stack[-1] == sandwiches[0]:
                stack.pop()
                sandwiches.pop(0)
        return len(stack)
