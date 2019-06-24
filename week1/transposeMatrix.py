# Given a matrix, return the transpose if it


class TransposeMatrix:
    def transpose(self, A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
