

fp = open('input.txt')

def load_data(fp):
    page = {}

    for line in fp:
        line = line.strip()

        if not line:
            break

        x, y = tuple(map(int, line.split(',')))
        page[(x, y)] = 1

    folds = []

    for line in fp:
        fdir, n = line.strip().split(' ')[2].split('=')
        folds.append((fdir, int(n)))

    return page, folds

def print_page(page):

    max_x = 0
    max_y = 0
    for x, y in page:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    for y in range(max_y+1):
        for x in range(max_x+1):
            print("#" if (x, y) in page else ".", end='')
        print()
    print()

def fold(page, folds):
    page = page.copy()

    for fold_dir, fold_line in folds:
        if fold_dir == 'x':
            for x, y in list(page):
                if x > fold_line:
                    page.pop((x, y))
                    x = fold_line - (x - fold_line)
                    page[(x, y)] = 1
        elif fold_dir == 'y':
            for x, y in list(page):
                if y > fold_line:
                    page.pop((x, y))
                    y = fold_line - (y - fold_line)
                    page[(x, y)] = 1

    return page



page, folds = load_data(fp)

part1 = len(fold(page, folds[:1]))
part2 = fold(page, folds)

print('Part1:', part1)
print('Part2:')

print_page(part2)
