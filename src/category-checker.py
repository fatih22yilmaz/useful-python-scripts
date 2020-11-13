category_list = {'Colorful Kilims',
                 'Vintage Modern Kilims',
                 'Embroidered Kilims',
                 'Rag Rugs',
                 'Hemp Kilims',
                 'Khotan | Caucasian Rugs',
                 'Turkish Anatolian Rugs',
                 'Persian Rugs',
                 'Turkish Oushak Rugs',
                 'Mini Rugs | Door Mats',
                 '16"x16"(40x40cm) Pillows',
                 '16"x24"(40x60cm) Pillows',
                 '20"x20"(50x50cm) Pillows',
                 '14"x20"(35x50cm) Pillows',
                 '20"x28"(50x70cm) Pillows',
                 '12"x24"(30x60cm) Pillows',
                 '18"x18"(45x45cm) Pillows',
                 '12"x20"(30x50cm) Pillows', }


def check_categories(category_file):
    categories = open(category_file, 'r')
    for index, category in enumerate(categories):
        category = category.rstrip()
        if category not in category_list:
            print('Inappropriate category name: ' + category + ' index: ' + str(index))


check_categories('../resources/categories.txt')
