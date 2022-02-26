# H - index
"""
Output Case #x: y
1 <= x (Test case)
y = space-seperated list of N integers
"""
import heapq

# def h_index(Papers, citations):
#     """
#     Brute Force Method - O(N^2)
#     list A = Store count of citations = Calculate cumulative sum
#     j = count of papers published
#     """
#     hindex = 0
#     A = [0 for _ in range(Papers + 1)]
#     ans = []
#     for i in range(Papers):
#         A[
#             Papers if citations[i] > Papers else citations[i]
#         ] += 1  # 1 at position determined by statement
#         j = i + 1  # count of papers publsihed
#         while j > hindex:  # Check for j value till previous found hindex
#             # sum(A[j:]) = Return no of papers in set with at least x citiations
#             if sum(A[j:]) >= j:
#                 hindex = j
#                 break
#             j -= 1
#         ans.append(hindex)
#     return ans


def h_index(Papers, citations):
    """
    Return H-index value for each addition of paper
    Time Complexity:
    list A - O(logN) time for 1 operation [A number added & removed at most once]
    Call list A N times
    O(NlogN)
    """
    hindex = 0
    ans = []
    A = []
    for i in range(Papers):
        if citations[i] > hindex:
            # Push citations[i] to list A
            heapq.heappush(A, citations[i])
        while A and A[0] <= hindex:
            # Remove lower values from A
            heapq.heappop(A)
        if len(A) >= hindex + 1:
            hindex += 1
        ans.append(hindex)
    return ans


def main():
    """
    Main Loop
    """
    T = int(input())
    if (1 <= T) and (T <= 100):
        for i in range(1, T + 1):
            N = int(input())
            citations = map(int, input().split(" "))
            h_index_scores = h_index(N, list(citations))
            print("Case #{}: {}".format(i, " ".join(map(str, h_index_scores))))


if __name__ == "__main__":
    main()
