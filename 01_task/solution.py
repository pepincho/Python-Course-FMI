from collections import defaultdict


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


def generate_histogram_numbers(pixel, histogram):
    for i in range(len(COLORS)):
        histogram[COLORS[i]][pixel[i]] += 1
    return histogram


def rotate_left(image):
    rows, cols = get_number_rows_cols(image)
    rotated_image = create_new_image_matrix(cols, rows)
    for i in range(cols):
        for j in range(rows):
            rotated_image[i][j] = image[j][- (i - cols + 1)]
    return rotated_image


def rotate_right(image):
    rows, cols = get_number_rows_cols(image)
    rotated_image = create_new_image_matrix(cols, rows)
    for i in range(cols):
        for j in range(rows):
            rotated_image[i][j] = image[- (j - rows + 1)][i]
    return rotated_image


def invert(image):
    rows, cols = get_number_rows_cols(image)
    inverted_image = create_new_image_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            inverted_image[i][j] = tuple(invert_pixel(image[i][j]))
    return inverted_image


def lighten(image, number):
    rows, cols = get_number_rows_cols(image)
    lighten_image = create_new_image_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            lighten_image[i][j] = tuple(light_pixel(image[i][j], number))
    return lighten_image


def darken(image, number):
    rows, cols = get_number_rows_cols(image)
    darken_image = create_new_image_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            darken_image[i][j] = tuple(dark_pixel(image[i][j], number))
    return darken_image


def create_histogram(image):
    rows, cols = get_number_rows_cols(image)
    histogram = {
        key: defaultdict(int) for key in COLORS
    }
    for i in range(rows):
        for j in range(cols):
            pixel = image[i][j]
            generate_histogram_numbers(pixel, histogram)
    return histogram
