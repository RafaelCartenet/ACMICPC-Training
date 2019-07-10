import os
from input_output_management import run_test
from data_structures.linked_list import list_to_dllist


def dllist_to_hashmap(node):
    ll_dict = {}
    while node:
        if node.value not in ll_dict:
            ll_dict[node.value] = [node]
        else:
            ll_dict[node.value].append(node)
        node = node.next
    return ll_dict


def sprinkler_dllist_to_str(dllist):
    if not dllist:
        return ''
    output = dllist.value
    dllist = dllist.next
    while dllist:
        if dllist.value not in [',', '.']:
            output += ' '
        output += dllist.value
        dllist = dllist.next

    return output + '\n'


def txt_to_sprinkler_list(s):
    output = []
    words = s.split()
    for word in words:
        if word[-1] in ['.', ',']:
            output += [word[:-1], word[-1]]
        else:
            output += [word]

    return output


def comma_sprinkler(text):
    text_as_list = txt_to_sprinkler_list(text)
    dllist_h, dllist_t = list_to_dllist(text_as_list)
    dllist_hashmap = dllist_to_hashmap(dllist_h)

    prec_candidates = set()
    succ_candidates = set()
    prec_visited = set()
    succ_visited = set()

    # Looking for first candidates
    commas = dllist_hashmap.get(',', [])
    for comma in commas:
        next_val = comma.next.value
        prev_val = comma.prev.value
        if next_val not in succ_visited:
            succ_candidates.add(next_val)
        if prev_val not in prec_visited:
            prec_candidates.add(prev_val)

    if not commas:
        return text

    while prec_candidates or succ_candidates:
        if prec_candidates:
            prec_candidate = prec_candidates.pop()
            # print('dealing with: %s' % prec_candidate)
            prec_visited.add(prec_candidate)

            # Adding commas on the right, creating succ candidates
            for node in dllist_hashmap[prec_candidate]:
                next_val = node.next.value
                if next_val not in [',', '.']:
                    if next_val not in succ_visited:
                        succ_candidates.add(next_val)
                    node.add_right(',')

        elif succ_candidates:
            succ_candidate = succ_candidates.pop()
            # print('dealing with: %s' % succ_candidate)
            succ_visited.add(succ_candidate)

            # Adding commas on the left, creating prec candidates
            for node in dllist_hashmap[succ_candidate]:
                if node.prev:
                    prev_val = node.prev.value
                    if prev_val not in [',', '.']:
                        if prev_val not in prec_visited:
                            prec_candidates.add(prev_val)
                        node.add_left(',')

    return sprinkler_dllist_to_str(dllist_h)


if __name__ == '__main__':
    path = 'icpc2018data/B-comma/'
    sample_name = 'sample-2'
    run_test(path, comma_sprinkler)
