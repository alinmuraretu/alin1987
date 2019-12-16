
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def get_total_count(inv):
    return sum(inv.values())


def get_max_column_widths(inv):
    max_name_width = None
    max_count_width = None
    for name, count in inv.items():
        name_width = len(name)
        count_width = len(str(count))

        if max_name_width == None or max_name_width < name_width:
            max_name_width = name_width

        if max_count_width == None or max_count_width < count_width:
            max_count_width = count_width
    return (max_name_width, max_count_width)


def display_inv(inv):
    print('Inv:')
    for name, count in inv.items():
        print(count, name)
    total_count = get_total_count(inv)
    print('Total number of items: {}'.format(total_count))