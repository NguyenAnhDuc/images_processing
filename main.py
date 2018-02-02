import pandas
from PIL import Image, ImageDraw, ImageFont

def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

def generate_text(text, output, fontname):
    #fontname = "Arial.ttf"
    #fontname = "Times New Roman.ttf"
    fontsize = 30
    colorText = "black"
    colorBackground = "white"
    fillcolor = "black"
    shadowcolor = "black"

    font = ImageFont.truetype(fontname, fontsize)
    width, height = getSize(text, font)
    x, y = 20 , 20
    #1: Font generate
    img = Image.new('RGB', (width + 50, height + 50), colorBackground)
    draw1 = ImageDraw.Draw(img)
    draw1.text((x, y), text, font=font, fill=shadowcolor)
    img.save(output+text+'_1.png')

    #2: Shadow thin border
    draw2 = ImageDraw.Draw(img)
    draw2.text((x - 1, y), text, font=font, fill=shadowcolor)
    draw2.text((x + 1, y), text, font=font, fill=shadowcolor)
    draw2.text((x, y - 1), text, font=font, fill=shadowcolor)
    draw2.text((x, y + 1), text, font=font, fill=shadowcolor)
    draw2.text((x, y), text, font=font, fill=fillcolor)
    img.save(output+text+'_2.png')

    #3: thicker border
    draw3 = ImageDraw.Draw(img)
    draw3.text((x - 1, y - 1), text, font=font, fill=shadowcolor)
    draw3.text((x + 1, y - 1), text, font=font, fill=shadowcolor)
    draw3.text((x - 1, y + 1), text, font=font, fill=shadowcolor)
    draw3.text((x + 1, y + 1), text, font=font, fill=shadowcolor)
    draw3.text((x, y), text, font=font, fill=fillcolor)
    img.save(output + text + '_3.png')

    #4: rotate:
    img5 = img.rotate(25)
    img5.save(output + text + '_4.png')
    #5: rotate:
    img5 = img.rotate(-25)
    img5.save(output + text + '_5.png')

    # 6: composite
    # Image.composite()

def normalizeName(name):
    return ''.join(e for e in name if e.isalpha())

def checkValidName(name):
    return len(name) <= 7 & len(name) > 0


def generate_image_2(text, output, background_path='input/images/background/background2.png'):
    img = Image.open(background_path)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("Arial.ttf", 25)
    draw.text((0, 0), text, font=font, fill="black")
    img.save(output)

def get_names(excel_file):
    df = pandas.read_excel(excel_file)
    names = df['Hoten'].values
    set_name = set()
    print(len(names))
    for name in names:
        try:
            word_names = name.split()
            for word_name in word_names:
                set_name.add(word_name.upper())
                #generate_image_2(word_name.upper(), output_full + word_name.upper() + '.png')
        except Exception as ex:
            print(ex)
    return set_name

def test():
    img = Image.open('input/images/background/cmt_background.png')


    pass

if __name__ == '__main__':
    # excel_file = 'input/Book1_1.xlsx'
    # excel_file_2 = 'input/HINHCMND.xlsx'
    # set_name = get_names(excel_file)
    # set_name_2 = get_names(excel_file_2)
    # set_name = set_name.union(set_name_2)

    # fonts = ['Times New Roman.ttf','Arial.ttf','Courier New.ttf']
    # set_name = set()
    # file_name = 'input/name'
    # with open(file_name) as f:
    #     lines = f.read().splitlines()
    # for line in lines:
    #     words = line.split()
    #     for word in words:
    #         normalized_name = normalizeName(word)
    #         if checkValidName(normalized_name):
    #          set_name.add(normalized_name.upper())
    #
    # set_word = set()
    # thefile = open('output/words_normalize_lower', 'w')
    # for item in set_name:
    #     for word in item:
    #         set_word.add(word)
    #     #thefile.write("%s\n" % item)
    #
    # print(len(set_word))
    # for word in set_word:
    #     thefile.write("%s\n" % word.lower())

    # count = 0
    # for font in fonts:
    #     for name in set_name:
    #         try:
    #             print("Process Image: " + str(count))
    #             count += 1
    #             output = 'output/generate/' + font[:3]+ '/'
    #             generate_text(name,output,font)
    #         except Exception as ex:
    #             pass
    pass

