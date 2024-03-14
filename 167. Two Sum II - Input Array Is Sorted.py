# This uses the two pointer approach and this is the simplest implementation of that
def twoSum(numbers: list[int], target: int) -> list[int]:
    left_index , right_index = 0 ,len(numbers) -1

    while left_index <= right_index:
        check = numbers[left_index] + numbers[right_index]
        if check == target:
            return [left_index+1, right_index +1]
        if check < target:
            left_index += 1
        elif check > target:
            right_index -= 1
