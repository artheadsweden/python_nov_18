def combine(size, color, garment):
    #return '%s %s in size %s' % (color, garment, size)
    #return '{0} {1} in size {2}'.format(color, garment, size)
    return f'{color} {garment} in size {size}'


def main():
    sizes = ['small', 'medium', 'large']
    colors = ['red', 'blue', 'brown']
    garments = ['hat', 'shirt', 'pants']
    zip(sizes, colors)


    result = list(map(combine, sizes, colors, garments))
    print(result)

    result = [f'{c} {g} in size {s}' for s, c, g in zip(sizes, colors, garments)]
    print(result)




if __name__ == '__main__':
    main()
