from typing import List

def read_inputs() -> List[List[int]]:
    reports = []
    f = open("input", "r")
    for line in f:
        levels = [int(x) for x in line.split()]
        reports.append(levels)
    f.close
    return reports

# Part 1
def get_safe_report_count(reports: List[List[int]]) -> int:
    safe_count = 0
    for report in reports:
        safe = True
        increasing = False
        decreasing = False
        for i in range(1, len(report)):
            # increasing, decreasing, or difference of 1 - 3
            if report[i] == report[i-1]:
                safe = False
                break
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
                    safe = False
                    break
            # Check difference
            if abs(difference) > 3:
                safe = False
                break
        
        if safe:
            safe_count += 1
            
    return safe_count

if __name__ == "__main__":
    reports = read_inputs()
    safe_report_count = get_safe_report_count(reports)
    print(safe_report_count)