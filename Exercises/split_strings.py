# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace
# the missing second character of the final pair with an underscore ('_').
#
# Examples:
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

# def solution(s):
#     if len(s) % 2 != 0:
#         s = s + '_'
#     split_s = []
#     i = 1
#     while i < len(s):
#         if i % 2 != 0:
#             split_s.append(s[i-1] + s[i])
#         i += 1
#     return split_s

def solution(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s + "_"]
    else:
        return [s[:2]] + solution(s[2:])

print(solution('abc'))
print(solution('abcdef'))

