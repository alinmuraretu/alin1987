def get_total_count(inventory):
    return sum(inventory.values())


def get_max_column_widths(inventory):
    max_name_width = None
    max_count_width = None
    for name, count in inventory.items():
        name_width = len(name)
        count_width = len(str(count))

        if max_name_width == None or max_name_width < name_width:
            max_name_width = name_width

        if max_count_width == None or max_count_width < count_width:
            max_count_width = count_width
    return (max_name_width, max_count_width)


def display_inventory(inventory):
    print('Inventory:')
    for name, count in inventory.items():
        print(count, name)
    total_count = get_total_count(inventory)
    print('Total number of items: {}'.format(total_count))


def add_to_inventory(inventory, added_items):
    for added_item in added_items:
        if added_item in inventory:
            inventory[added_item] += 1
        else:
            inventory[added_item] = 1

def print_table(inventory, order=None):
    max_name_width, max_count_width = get_max_column_widths(inventory)

    name_label = 'item name'
    count_label = 'count'

    name_width = max(max_name_width, len(name_label))
    count_width = max(max_count_width, len(count_label))

    # Ordering
    inventory_list = list(inventory.items())
    if order != None and order.startswith('count'):
        reverse = order.endswith('desc')
        inventory_list.sort(key=lambda item: (item[1], item[0]), reverse=reverse)

    # Header
    print('Inventory:')
    print('  {}    {}'.format(
        count_label.center(count_width),
        name_label.center(name_width)))

    # Separator
    print('--{}----{}'.format('-' * count_width, '-' * name_width))

    # Rows
    for name, count in inventory_list:
        print('  {}    {}'.format(
            str(count).rjust(count_width),
            name.rjust(name_width)))

    # Separator
    print('--{}----{}'.format('-' * count_width, '-' * name_width))
    print('Total number of items: {}'.format(get_total_count(inventory)))


def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename) as f:
        line = f.read()
        items = line.split(',')
        add_to_inventory(inventory, items)


def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, 'w') as f:
        total_count = get_total_count(inventory)
        current_count = 0
        for name, count in inventory.items():
            for _ in range(count):
                f.write(name)
                current_count += 1
                if not current_count == total_count:
                    f.write(',')


def main():
    my_inventory = {'cat': 1, 'dog': 2, 'bat': 3}
    display_inventory(my_inventory)
    add_to_inventory(my_inventory, ['eel', 'eel'])
    display_inventory(my_inventory)
    import_inventory(my_inventory, filename='test_inventory.csv')
    display_inventory(my_inventory)
    export_inventory(my_inventory, filename='my_inventory.csv')
    print_table(my_inventory)
    print_table(my_inventory, 'count,asc')
    print_table(my_inventory, 'count,desc')


if __name__ == '__main__':
    main()
