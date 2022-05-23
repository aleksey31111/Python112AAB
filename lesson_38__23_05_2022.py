### LESSON 38 ###
## Continue Parsin via OOP

from parser import Parser

def main():
    pars = Parser("https://www.ixbt.com/live/index/type/news/",
                   "news_38.txt")
    # pars.get_html()
    pars.run()

if __name__ == '__main__':
    main()