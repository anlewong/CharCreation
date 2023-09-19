# CharCreation
building a better character creator
The goal of this project is to build a better character creator that includes all information off of wikidot 5e and an intuitive creator with links to optimization and role playing suggestions.

stat roller: the basic stat roller provides either a standard stat spread or randomized roll stats with options to show indiivdual rolls or end scores.

char search: uses webscraping to pull info from wiki-dot 5e and use it in order to have descriptions and greator ability to create characters for free compared to the DND Beyond or Roll 20

Auto leveler uses char search to have more sub-classes and more customizability

char search updated methodology:
    it will likley be extremely slow to utilize web scraping as an active way to search and create characters. Based on looking at the charactermancer on roll20 the dictionaries are hardcoded per game and imported if enabled by other website code.

    As such the way I will implement it is to simply web scrape all data, and parse it into a format that enables me to have it in a database to pull from. 

    Right now with just the basics I think I will start by learning how to pull race data and then format it. we will start with the common races. Right now the basic data I want to extract from each page is

    Race, class bonues, size, walking speed

    
