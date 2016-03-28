COLORS = ['red', 'green', 'blue']


def get_number_rows_cols(image):
    return len(image), len(image[0])


def create_new_image_matrix(rows, cols):
    new_image = [
        [() for x in range(cols)] for y in range(rows)
    ]
    return new_image


def invert_pixel(pixel):
    return [255 - x for x in pixel]


def light_pixel(pixel, number):
    return [int(x + (255 - x) * number) for x in pixel]


def dark_pixel(pixel, number):
    return [int(x - (x - 0) * number) for x in pixel]


def grayscale(func):
    def helper(image, *args):
        rows, cols = len(image), len(image[0])
        for i in range(rows):
            for j in range(cols):
                gray = int(sum([x for x in image[i][j]]) / len(COLORS))
                image[i][j] = tuple([gray for x in range(len(COLORS))])
        if len(args) != 0:
            return func(image, args[0])
        return func(image)
    return helper


@grayscale
def rotate_left(image):
    rows, cols = get_number_rows_cols(image)
    rotated_image = create_new_image_matrix(cols, rows)
    for i in range(cols):
        for j in range(rows):
            rotated_image[i][j] = image[j][- (i - cols + 1)]
    return rotated_image


@grayscale
def rotate_right(image):
    rows, cols = get_number_rows_cols(image)
    rotated_image = create_new_image_matrix(cols, rows)
    for i in range(cols):
        for j in range(rows):
            rotated_image[i][j] = image[- (j - rows + 1)][i]
    return rotated_image


@grayscale
def invert(image):
    rows, cols = get_number_rows_cols(image)
    inverted_image = create_new_image_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            inverted_image[i][j] = tuple(invert_pixel(image[i][j]))
    return inverted_image


@grayscale
def lighten(image, number):
    rows, cols = get_number_rows_cols(image)
    lighten_image = create_new_image_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            lighten_image[i][j] = tuple(light_pixel(image[i][j], number))
    return lighten_image


@grayscale
def darken(image, number):
    rows, cols = get_number_rows_cols(image)
    darken_image = create_new_image_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            darken_image[i][j] = tuple(dark_pixel(image[i][j], number))
    return darken_image
