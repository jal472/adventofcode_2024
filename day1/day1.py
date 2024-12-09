from typing import Tuple, List

def read_inputs() -> Tuple[List[int], List[int]]:
    a = []
    b = []
    f = open("input", "r")
    for line in f:
        inputs = line.split()
        a.append(int(inputs[0]))
        b.append(int(inputs[1]))
    f.close()
    return a, b

# Part 1
def get_list_distance(a: List[int], b: List[int]) -> int:
    total_distance = 0
    # Modified Selection Sort
    for i in range(len(a)):
        # if we reach the end of the list, no more comparisons needed to sort the list. Just calculate the distance.
        if i == len(a)-1:
            total_distance += abs(a[i] - b[i])
            break
        # find the index of the min number of the rightside of the list
        min_a_idx = min(range(len(a[i+1:])), key=a[i+1:].__getitem__)
        min_b_idx = min(range(len(b[i+1:])), key=b[i+1:].__getitem__)
        # adjust index to account for elements to the left that were omitted in the min search
        min_a_idx += (i+1)
        min_b_idx += (i+1)
        # compare and swap
        if a[min_a_idx] < a[i]:
            a[i], a[min_a_idx] = a[min_a_idx], a[i]
        if b[min_b_idx] < b[i]:
            b[i], b[min_b_idx] = b[min_b_idx], b[i]
        # Calculate total distance
        total_distance += abs(a[i] - b[i])
    return total_distance

# Part 2
def get_similarity_score(a: List[int], b: List[int]) -> int:
    similarity_score = 0
    for num in a:
        count = b.count(num)
        similarity_score += (num * count)
    return similarity_score

if __name__ == "__main__":
    a, b = read_inputs()
    total_distance = get_list_distance(a, b)
    print(f'Total distance: {total_distance}')
    similarity_score = get_similarity_score(a, b)
    print(f'Similarity score: {similarity_score}')
    