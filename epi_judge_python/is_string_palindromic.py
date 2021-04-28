from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    if len(s) <= 1:
        return True
    half_indices = len(s) // 2
    for i in range(half_indices):
        if s[i] != s[-1 - i]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
