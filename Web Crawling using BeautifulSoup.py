# Firstly install this command [ python.exe -m pip install --upgrade pip] from CMD
# after installing this Then again install [pip install BeautifulSoup4] command ::--

# import  requests
# from  import BeautifulSoup
# response=requests.get("https://www.magicbricks.com/")
# print(response.status_code)


# soup = BeautifulSoup(response.content,"html.parser")
# print(soup.prettyfy())


# find('a')
# find_all("img")
# find_parent("a")
# find_next_siblings("a")

cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})
# print(card)
for card in cards:

    price = card.find("div",attrs={"class":"m-srp-card__price"})
    # print(price.txt)
    title = card.find("span",attrs={"class":"m-srp-card__title__bhk"})
    print(title.text.strip("\n"))

    carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
    print(carpet_area.text)


    data = " {} {} {}".format(title.text.strip("\n"),price.text,carpet_area.text)
    print(data)






