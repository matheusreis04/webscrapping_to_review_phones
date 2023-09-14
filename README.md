# webscrapping_to_review_phones
I've been curious to known if a certain cell is good or not to buy it, so i started this code with a simples purpose: search a review in a site of my choice and extracts the main description and scores of the phone.
I reached the following conclusion how to do it:
Using python, i've import 3 libraries called BeautifulSoup(for treat mine url page), search from googlesearch (to catch the site's link) and requests(to catch the url)

At first, i ask the phone's name. Then i google it next to the name of the site, catch the first link that appears.
After that, my code use the request to get the url of this link and the beautifulSoup finds the informations that i want to know. Then i simply print the information on my terminal.
