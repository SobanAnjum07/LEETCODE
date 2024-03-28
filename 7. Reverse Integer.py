class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31) - 1:
            return 0
        elif x < -(2**31):
            return 0
        else:

            if x < 0:
                x_s = str(x)
                x_s = x_s[1:]
                new_s = x_s[::-1]
                return_int = int(new_s) * -1
                if return_int < -(2**31):
                    return 0
                return return_int

            x_s = str(x)
            new_s = x_s[::-1]
            return_int = int(new_s)
            if return_int > (2**31) - 1:
                return 0
            return return_int
