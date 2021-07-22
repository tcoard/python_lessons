import time

def divide_evens(num):
    # print(f"calculating {num}...")
    # time.sleep(0.5)
    if num % 2 == 0:
        return int(num/2)
    return num

def mass_divide_evens(nums):
    to_return = list()
    for num in nums:
        to_return.append(divide_evens(num))
    return to_return

def gen_divide_evens(nums):
    for num in nums:
        yield divide_evens(num)

def main():
    nums = [1, 2, 3, 8, 9]

    #--------------section 1--------------
    # These three loops all do the same thing, but the last one computes numbers that it does not use
    for num, divided_num in zip(nums, gen_divide_evens(nums)):
        if num > divided_num:
            print(num, divided_num)
            break

    for num, divided_num in zip(nums, map(divide_evens, nums)):
        if num > divided_num:
            print(num, divided_num)
            break

    for num in nums:
        divided_num = divide_evens(num)
        if num > divided_num:
            print(num, divided_num)
            break

    #--------------section 2--------------
    # These both do the same thing. The first one is more terse, but less readable
    print(max(filter(lambda x: x % 2 == 0, nums), key=lambda x: x % 8))

    max_num = 0
    for num in nums:
        if num % 2 == 0:
            if num % 8 > max_num:
                max_num = num
    print(max_num)


if __name__ == "__main__":
    main()
