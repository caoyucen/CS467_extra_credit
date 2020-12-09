def reverse_search(l, res, rev_pos, last_rev_pos):
    curr = rev_pos - 1
    # find the pos before rev_pos that needs to be reversed to maintain lexical order
    while curr > last_rev_pos:
        to_compare = l[curr + 1] if res[curr + 1] == 0 else l[curr + 1][::-1]
        # print('rev search: ', res, rev_pos, last_rev_pos, curr, l[curr], to_compare)
        if l[curr] > to_compare:
            if l[curr][::-1] <= to_compare:
                res[curr] = 1
                curr -= 1
            else:
                # if reversing still can't maintain the order, then return false
                return False
        else:
            break
    return True

def reverse_str(l):
    if not l or len(l) <= 1:
        return True
    res = [0] * len(l)
    rev_pos = 1 # current position that has to be flipped
    last_rev_pos = -1 # last position that has to be flipped
    curr = 1
    while rev_pos < len(l) and curr < len(l):
        to_compare = l[curr - 1] if res[curr - 1] == 0 else l[curr - 1][::-1]
        # print(res, rev_pos, last_rev_pos, curr, l[curr], to_compare)
        if l[curr] >= to_compare:
            curr += 1
            rev_pos += 1
        # if reversed l[i] can keep l[:i] lexical
        elif l[curr][::-1] >= to_compare:
            # print('revert lexical')
            res[curr] = 1
            curr += 1
            # if curr >= len(l):
            #     return False
            rev_pos += 1
        else:
            # print('rev: ', res, rev_pos, last_rev_pos, curr, l[curr], to_compare)
            if not reverse_search(l, res, rev_pos, last_rev_pos):
                res[curr] = 1
                if not reverse_search(l, res, rev_pos, last_rev_pos):
                    return False

            last_rev_pos = rev_pos
            rev_pos += 1
            curr = rev_pos
    return "".join([str(x) for x in res])


import os
import sys
files_prefix = sorted(list(set([os.path.splitext(x)[0] for x in os.listdir('./shared/')])))
print(files_prefix)
for prefix in files_prefix:
    in_file = './shared/' + prefix + '.in'
    out_file = './shared/' + prefix + '.out'
    # run test cases
    with open(in_file, 'r') as infp, open(out_file, 'r') as ofp:
        # print('currently processing data: {}'.format(prefix))
        num_cases = int(infp.readline())
        for i in range(num_cases):
            num_words = int(infp.readline())
            L = []
            for j in range(num_words):
                L.append(infp.readline().strip('\n'))
            # print(L)
            res = reverse_str(L)
            pres = 'IMPOSSIBLE' if res == False else res
            # print(pres)
            expected = ofp.readline().strip('\n')
            if expected == pres:
                print('PASSED')
            else:
                # print('FAILED TEST CASE #{}: {}, expected {}, actual {}'.format(i, L, expected, pres))
                print('FAILED')
