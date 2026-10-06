print("SCORE LIST EXPLORER")

score_list = [45, 60, 75, 88, 92]
print("Full list:", score_list)
print("Head:", score_list[0])
print("Tail:", score_list[1:])
def show_shrink(score_list):
    print(score_list)
    if len(score_list) <= 1:
        return
    show_shrink(score_list[1:])

show_shrink(score_list)
def is_sorted(score_list):
    if len(score_list) <= 1:
        return True
    if score_list[0] > score_list[1]:
        return False
    return is_sorted(score_list[1:])

print(score_list, "is sorted:", is_sorted(score_list))
unsorted_list = [45, 75, 60, 88, 92]
print(unsorted_list, "is sorted:", is_sorted(unsorted_list))
def recursive_sum(score_list):
    if len(score_list) == 0:
        return 0
    return score_list[0] + recursive_sum(score_list[1:])

total = recursive_sum(score_list)
print("Scores:", score_list)
print("Total:", total)

def find_largest(score_list):
    if len(score_list) == 1:
        return score_list[0]
    largest_tail = find_largest(score_list[1:])
    if score_list[0] > largest_tail:
        return score_list[0]
    else:
        return largest_tail
    
largest = find_largest(score_list)
print("Scores:", score_list)
print("Largest score:", largest)