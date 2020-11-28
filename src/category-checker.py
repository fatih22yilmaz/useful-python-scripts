category_list = {'RUGS:::RUGS///HANDWOVEN KILIM RUGS:::RUGS///HANDWOVEN KILIM RUGS///Colorful Kilims',
                 'RUGS:::RUGS///HANDWOVEN KILIM RUGS:::RUGS///HANDWOVEN KILIM RUGS///Vintage Modern Kilims',
                 'RUGS:::RUGS///HANDWOVEN KILIM RUGS:::RUGS///HANDWOVEN KILIM RUGS///Embroidered Kilims',
                 'RUGS:::RUGS///HANDWOVEN KILIM RUGS:::RUGS///HANDWOVEN KILIM RUGS///Rag Rugs',
                 'RUGS:::RUGS///HANDWOVEN KILIM RUGS:::RUGS///HANDWOVEN KILIM RUGS///Hemp Kilims',
                 'RUGS:::RUGS///HANDKNOTTED RUGS:::RUGS///HANDKNOTTED RUGS///Khotan | Caucasian Rugs',
                 'RUGS:::RUGS///HANDKNOTTED RUGS:::RUGS///HANDKNOTTED RUGS///Turkish Anatolian Rugs',
                 'RUGS:::RUGS///HANDKNOTTED RUGS:::RUGS///HANDKNOTTED RUGS///Persian Rugs',
                 'RUGS:::RUGS///HANDKNOTTED RUGS:::RUGS///HANDKNOTTED RUGS///Turkish Oushak Rugs',
                 'MINI RUGS | DOOR MATS',
                 'PILLOWS:::PILLOWS///16"x16"(40x40cm) Pillows',
                 'PILLOWS:::PILLOWS///16"x24"(40x60cm) Pillows',
                 'PILLOWS:::PILLOWS///20"x20"(50x50cm) Pillows',
                 'PILLOWS:::PILLOWS///14"x20"(35x50cm) Pillows',
                 'PILLOWS:::PILLOWS///20"x28"(50x70cm) Pillows',
                 'PILLOWS:::PILLOWS///12"x24"(30x60cm) Pillows',
                 'PILLOWS:::PILLOWS///18"x18"(45x45cm) Pillows',
                 'PILLOWS:::PILLOWS///12"x20"(30x50cm) Pillows', }


def check_categories(category_file):
    categories = open(category_file, 'r')
    for index, category in enumerate(categories):
        category = category.rstrip()
        if category not in category_list:
            print('Inappropriate category name: "' + category + '" on line: ' + str(index + 1))
    print("\nFinished Successfully!..")


check_categories('../resources/categories.txt')
