def parse_links():
    with open('yas_links.txt', 'r', encoding="utf-8") as f:
        links = f.readlines()
        # links = ['https://www.youtube.com/watch?v=5MGypvg7zf0\n', 'https://www.youtube.com/watch?v=92aSNiVleYo\n', 'https://www.youtube.com/watch?v=5DjFpPSuGR0']
        return links


if __name__=="__main__":
    parse_links()
    


#How to use: 
# put youtube vid links in links.txt file
# type: python yas_loader.py > result.txt in command line.