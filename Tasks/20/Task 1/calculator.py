def make_operation(operation, *args):
    if operation not in ('+', '-', '*'):
        raise TypeError("This operation is not supported; Use one of +-*")

    for arg in args:
        if not isinstance(arg, int):
            raise ValueError(f"One of the arguments is not an integer: {arg}")

    if operation == '+':
        return sum(args)
    elif operation == '*':
        res = 1
        for x in args:
            res *= x
        return res
    elif operation == '-':
        if not args:
            return 0
        result = args[0]
        for x in args[1:]:
            result -= x
        return result


def test_sub_success(self):
    result = make_operation('-', 5, 5, -10, -20)
    expected_result = -30
    self.assertEqual(result, expected_result)