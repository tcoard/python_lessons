from other_file import upper_case_trim
from other_other_file import sort_and_double

def main():
    value = "teeeeeeest"

    breakpoint()
    # we expect this to return "TE"
    uptrimed = upper_case_trim(value, trim_amount=2)

    # we expect this to return "EETT"
    sort_doubled = sort_and_double(uptrimed)
    for letter in sort_doubled:
        if letter == "T":
            breakpoint()
            print('t')

    print(sort_doubled)


if __name__ == "__main__":
    main()
