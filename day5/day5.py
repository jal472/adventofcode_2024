from typing import Tuple, List, Dict

def read_inputs() -> Tuple[Dict[int, List[int]], List[List[int]]]:
    page_order_dict = {}
    update_prod_list = []
    f = open("input", "r")
    page_order_read = False
    for line in f:
        # We know we finished reading the page order when we hit the line that only has the newline char
        if line == "\n":
            page_order_read = True
            continue
        # For all other lines we need to remove the newline char; needs to be an if statement because the last line likely won't have one
        if line[-1] == "\n":
            line = line[:-1]
        # If the page order data has not been read, read it
        if not page_order_read:
            page_nums = line.split("|")
            if int(page_nums[0]) not in page_order_dict:
                page_order_dict[int(page_nums[0])] = [int(page_nums[1])]
            else:
                page_order_dict[int(page_nums[0])].append(int(page_nums[1]))
        # If the page order data has been read, start reading the update production lists
        else:
            update = []
            for page_num in line.split(","):
                update.append(int(page_num))
            update_prod_list.append(update)
    f.close()

    return (page_order_dict, update_prod_list)


def is_position_valid(page_order_dict: Dict[int, List[int]], update: List[int], curr_idx: int) -> bool:
    # Check for rule that curr number must be before any number before it
    if update[curr_idx] in page_order_dict.keys():
        for i in range(curr_idx):
            if update[i] in page_order_dict[update[curr_idx]]:
                return False
    # Check for rule that curr number must be after any number after it
    for i in range(curr_idx+1, len(update)):
        if update[i] in page_order_dict.keys():
            if update[curr_idx] in page_order_dict[update[i]]:
                return False
    # If there is no rule then it is considered valid
    return True


def correct_bad_update(page_order_dict: Dict[int, List[int]], update: List[int]) -> int:
    # print("=========================")
    # print(update)
    corrected_update = []
    for page in update:
        # print(f'Checking {page}')
        if corrected_update == []:
            # print("Empty list, adding...")
            corrected_update.append(page)
        else:
            # Get before idx - loop from back to front
            before_idx = len(corrected_update)
            for i in range(len(corrected_update))[::-1]:
                if page in page_order_dict.keys():
                    if corrected_update[i] in page_order_dict[page]:
                        before_idx = i
            # print(f'Before idx found: {before_idx}')
            # Get after idx - loop from front to before_idx
            after_idx = -1
            for i in range(before_idx):
                if corrected_update[i] in page_order_dict.keys():
                    if page in page_order_dict[corrected_update[i]]:
                        after_idx = i
            # print(f'After idx found: {after_idx}')
            # Insert page after the after_idx
            if after_idx == len(corrected_update)-1:
                corrected_update.append(page)
            else:
                corrected_update.insert(after_idx+1, page)
    #     print(f'Corrected Update: {corrected_update}')
    # print(f'Returning: {corrected_update[int((len(corrected_update)-1)/2)]}')
    return corrected_update[int((len(corrected_update)-1)/2)]


def review_update_order(page_order_dict: Dict[int, List[int]], update_prod_list: List[List[int]]) -> Tuple[int, int]:
    correct_sum = 0
    incorrect_sum = 0
    for update in update_prod_list:
        valid_update = True
        for i in range(len(update)):
            valid_update = is_position_valid(page_order_dict, update, i)
            if not valid_update:
                break
        
        if valid_update:
            # Get middle element and add to sum
            correct_sum += update[int((len(update)-1)/2)]
        else:
            # Correct the incorrect update list and add its mid to the incorrect sum
            incorrect_sum += correct_bad_update(page_order_dict, update)
    
    return (correct_sum, incorrect_sum)



if __name__ == "__main__":
    page_order_dict, update_prod_list = read_inputs()
    # print("PAGE ORDER DICT")
    # for k, v in page_order_dict.items():
    #     print(f'{k}: {v}')
    correct__sum, incorrect_sum = review_update_order(page_order_dict, update_prod_list)
    print(f'Part1: {correct__sum}')
    print(f'Part2: {incorrect_sum}')