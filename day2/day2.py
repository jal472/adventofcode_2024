from typing import List, Tuple

def read_inputs() -> List[List[int]]:
    reports = []
    f = open("input", "r")
    for line in f:
        levels = [int(x) for x in line.split()]
        reports.append(levels)
    f.close
    return reports

def is_safe_report(report: List[int]) -> Tuple[bool, int]:
    increasing = False
    decreasing = False
    for i in range(1, len(report)):
        # increasing, decreasing, or difference of 1 - 3
        if report[i] == report[i-1]:
            return False, i
        difference = report[i] - report[i-1]
        # establish increasing or decreasing
        if i == 1:
            if difference < 0: # decreasing
                decreasing = True
            else:
                increasing = True
        # check if increase or decrease has changed
        else:
            if (decreasing and difference > 0) or (increasing and difference < 0):
                return False, i
        # Check difference
        if abs(difference) > 3:
            return False, i

    return True, None

# Part 1
def get_safe_report_count(reports: List[List[int]]) -> int:
    safe_count = 0
    for report in reports:
        print("=========================")
        safe, bad_level = is_safe_report(report)
        # if deemed not safe at first, try removing the bad level or the level following the bad level and reevaluate
        if not safe:
            print(report)
            # print(f'Safe Before: {safe}')
            # remove bad level
            report_mut = report[:bad_level] + report[bad_level+1:]
            print(report_mut)
            safe, _ = is_safe_report(report_mut)
            # remove level after bad level
            if not safe and (bad_level < len(report)):
                report_mut = report[:bad_level+1] + report[bad_level+2:]
                print(report_mut)
                safe, _ = is_safe_report(report_mut)
            # remove level before bad level
            if not safe:
                report_mut = report[:bad_level-1] + report[bad_level:]
                print(report_mut)
                safe, _ = is_safe_report(report_mut)
            # print(f'Safe After: {safe}')
        
        if safe:
            safe_count += 1
            
    return safe_count

if __name__ == "__main__":
    reports = read_inputs()
    # reports = [
    #     [7, 6, 4, 2, 1],
    #     [1, 2, 7, 8, 9],
    #     [9, 7, 6, 2, 1],
    #     [1, 3, 2, 4, 5],
    #     [8, 6, 4, 4, 1],
    #     [1, 3, 6, 7, 9]
    # ]
    safe_report_count = get_safe_report_count(reports)
    print(safe_report_count)