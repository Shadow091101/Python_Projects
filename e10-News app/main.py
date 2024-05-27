import requests

# Replace 'API_KEY' with your actual NewsAPI key
def top_headlinefunction(country,category,Keywords,Max_news):
    api_key ='api_key'
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&q={Keywords}&pageSize={Max_news}&apiKey={api_key}'

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        # The request was successful
        data = response.json()

        if data['totalResults']==0:
            print("There are No News according to the given preferences.")
        else:

            i = 1
            for article in data['articles']:
                title = article.get('title', 'No title available')
                description = article.get('description', 'No description available')
                content = article.get('content', 'No content available')
                source = article.get('source', {}).get('name', 'No source name available')
                print(f"**************{source}***************")
                
                # Truncate the content to 100-200 characters
                

                print(f"{i}. Title: {title}")
                print(f"   Description: {description}\n")
                print(f"   Content: {content}\n")
                i += 1
    else:
        # The request failed
        print(f"Error: {response.status_code}")
def country_wisefunction(country,Keywords,Max_news):
    api_key = 'api_key'
    url = f'https://newsapi.org/v2/top-headlines?country={country}&q={Keywords}&pageSize={Max_news}&apiKey={api_key}'

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        # The request was successful
        data = response.json()
        if data['totalResults']==0:
            print("There are No News according to the given preferences.")
        else:

            i = 1
            for article in data['articles']:
                title = article.get('title', 'No title available')
                description = article.get('description', 'No description available')
                content = article.get('content', 'No content available')
                source = article.get('source', {}).get('name', 'No source name available')
                print(f"**************{source}***************")
                # Truncate the content to 100-200 characters
                

                print(f"{i}. Title: {title}")
                print(f"   Description: {description}\n")
                print(f"   Content: {content}\n")
                i += 1
    else:
        # The request failed
        print(f"Error: {response.status_code}")
def sourcefunction(sources,Keywords,fromdate,todate,Max_news):
    api_key = 'api_key'
    url = f'https://newsapi.org/v2/everything?sources={sources}&q={Keywords}&from={fromdate}&to={todate}&pageSize={Max_news}&apiKey={api_key}'

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        # The request was successful
        data = response.json()
        if data['totalResults']==0:
            print("There are No News according to the given preferences.")
        else:

            i = 1
            for article in data['articles']:
                title = article.get('title', 'No title available')
                description = article.get('description', 'No description available')
                content = article.get('content', 'No content available')
                source = article.get('source', {}).get('name', 'No source name available')
                print(f"**************{source}***************")
                
                # Truncate the content to 100-200 characters
                

                print(f"{i}. Title: {title}")
                print(f"   Description: {description}\n")
                print(f"   Content: {content}\n")
                i += 1
    else:
        # The request failed
        print(f"Error: {response.status_code}")
def categoryfunction(category,maxnews):
    api_key = 'api_key'
    url = f'https://newsapi.org/v2/top-headlines?category={category}&pageSize={maxnews}&language=en&apiKey={api_key}'

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        # The request was successful
        data = response.json()
        if data['totalResults']==0:
            print("There are No News according to the given preferences.")
        else:

            i = 1
            for article in data['articles']:
                title = article.get('title', 'No title available')
                description = article.get('description', 'No description available')
                content = article.get('content', 'No content available')
                source = article.get('source', {}).get('name', 'No source name available')
                print(f"**************{source}***************")
                
                

                print(f"{i}. Title: {title}")
                print(f"   Description: {description}\n")
                print(f"   Content: {content}\n")
                i += 1
    else:
        # The request failed
        print(f"Error: {response.status_code}")
def datefunction(keyword,fromdate,todate,maxpages):
    api_key = 'api_key'
    url = f'https://newsapi.org/v2/everything?q={keyword}&from={fromdate}&to={todate}&pageSize={maxpages}&apiKey={api_key}'

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        # The request was successful
        data = response.json()
        if data['totalResults']==0:
            print("There are No News according to the given preferences.")
        else:

            i = 1
            for article in data['articles']:
                title = article.get('title', 'No title available')
                description = article.get('description', 'No description available')
                content = article.get('content', 'No content available')
                source = article.get('source', {}).get('name', 'No source name available')
                print(f"**************{source}***************")
                
                # Truncate the content to 100-200 characters
                

                print(f"{i}. Title: {title}")
                print(f"   Description: {description}\n")
                print(f"   Content: {content}\n")
                i += 1
    else:
        # The request failed
        print(f"Error: {response.status_code}")
def countryname():
    valid_countries = {
       
        "ae": ["ae", "uae", "united arab emirates"],
        "us": ["us", "usa", "united states", "united states of america", "america"],
        "bg":["bg","bulgaria"],
        "gb": ["gb", "uk", "united kingdom", "great britain", "england"],
        "in": ["in", "india"],
        "au": ["au", "aus", "australia"],
        "cu": ["cu","cuba"],
        "ca": ["ca", "canada"],
        "fr": ["fr", "france"],
        "de": ["de", "germany"],
        "it": ["it", "italy"],
        "jp": ["jp", "japan"],
        "cn": ["cn", "china"],
        "ru": ["ru", "russia"],
        "br": ["br", "brazil"],
        "mx": ["mx", "mexico"],
        "za": ["za", "south africa"],
        "es": ["es", "spain"],
        "kr": ["kr", "south korea","sk","s korea"],
        "id": ["id", "indonesia"],
        "ar": ["ar", "argentina"],
        "tr": ["tr", "turkey"],
        "th": ["th", "thailand","thai"],
        "nl": ["nl", "netherlands"],
        "sa": ["sa", "saudi arabia","arab","arabia"],
        "sg": ["sg", "singapore"],
        "ch": ["ch", "switzerland","swiz"],
        "co": ["co", "colombia"],
        "se": ["se", "sweden"],
        "my": ["my", "malaysia"],
        "eg": ["eg", "egypt"],
        "ph": ["ph", "philippines"],
        "pl": ["pl", "poland"],
        "vn": ["vn", "vietnam"],
        "hk": ["hk", "hong kong"],
        "be": ["be", "belgium"],
        "il": ["il", "israel"],
        "ua": ["ua", "ukraine"],
        "pk": ["pk", "pakistan"],
        "ro": ["ro", "romania"],
        "pt": ["pt", "portugal"],
        "dk": ["dk", "denmark"],
        "no": ["no", "norway"],
        "fi": ["fi", "finland"],
        "at": ["at", "austria"],
        "gr": ["gr", "greece"],
        "cz": ["cz", "czech republic","czr"],
        "ng": ["ng", "nigeria"],
        "ie": ["ie", "ireland"],
        "nz": ["nz", "new zealand","zealand"],
        "hu": ["hu", "hungary"],
        "lt": ["lt","lithuania"],
        "lv": ["lv","latvia"],
        "ma":["ma","morocco"],
        "rs":["rs","serbia"],
        "si":["si","slovenia"],
        "sk":["sk","slovakia"],
        "tw":["tw","taiwan"],
        "ve":["ve","venezuela"]
    }

    while True:
        ctryname = input("Country: ").strip().lower()
        if ctryname=='':
            return ''
        for code, names in valid_countries.items():
            if ctryname in names:
                return code
        print("Please provide the Country Name Correctly.")

def sourcefunc():
    sourcechoice=int(input("Which Countries News Source You want To Read : \n 1)India \t 2)Britain\t 3)USA\n Or if you just want to go to previous page press 9 or if you want to quit press 0\n"))
    if sourcechoice==1:
        print("Select Which Source You Wants From India : \n")
        indiansourcechoice=int(input("1)TOI(The Times Of India)\n 2)The Hindu\n or if you want to go back press 9 or if you want to quit press 5\nEnter Your Choice : "))
       
        if(indiansourcechoice==1):
            return 'the-times-of-india'
        if(indiansourcechoice==2):
            return 'the-hindu'
        if(indiansourcechoice==9):
            sourcefunc()
        if(indiansourcechoice==0):
            quit()
        
    if(sourcechoice==2):
        return 'bbc-news'
        
        
    if(sourcechoice==3):
        print("Selevct which source You Wants From USA : \n")
        usasourcechoice=int(input("1)The Washington Post\n2)Wired\n3)CNN\n4)Fox News\n5)NBC News\nor if you want to go back press 9 or if you want to quit press 5\nEnter your Choice : "))
        if(usasourcechoice==1):
            return 'the-washington-post'
        if(usasourcechoice==2):
            return 'wired'
        if(usasourcechoice==3):
            return 'cnn'
        if(usasourcechoice==4):
            return 'fox-news'
        if(usasourcechoice==5):
            return 'nbc-news'
        if(usasourcechoice==9):
            sourcefunc()
        if(usasourcechoice==0):
            quit()
        
    if(sourcechoice==9):
        mainmenu()
    if(sourcechoice==0):
        quit()  
        
print("*************Welcome to the News WorldWide Center.************\n")
def mainmenu():
    print("Select Want You Want To read for Today:\n")
    mainmenuchoice=int(input("1)Top-Headlines\n 2)Country-wise-top-news\n 3)Top-Sources\n  4)Category\n 5)Search the news by Date: \n Enter Your Choice : "))
    if(mainmenuchoice==1):
        print("Put Your Input as per the following preferences to search:\n")
        country = countryname()
        category=input("Category(business,entertainment,health,science,sports,technology) : ")
        
        Keywords=input("Keyword : ").strip().lower()
        Max_news=int(input("Maximum news to be recieved upto 100 : "))
        confirm=int(input(("If You want to continue press 1\n or if you want to go back press 9\n or if you want to quit press 0")))
        if(confirm==1):
            top_headlinefunction(country,category,Keywords,Max_news)
        elif(confirm==9):
            mainmenu()
        elif(confirm==0):
            quit()
    elif(mainmenuchoice==2):
        print("Put Your Input as per the following preferences to search:\n")
        country = countryname()
        Keywords=input("Keyword : ").strip().lower()
        Max_news=int(input("Maximum news to be recieved upto 100 : "))
        confirm=int(input(("If You want to continue press 1\n or if you want to go back press 9\n or if you want to quit press 0")))
        if(confirm==1):
            country_wisefunction(country,Keywords,Max_news)
        elif(confirm==9):
            mainmenu()
        elif(confirm==0):
            quit()
        
        
    elif(mainmenuchoice==3):
        print("Put Your Input as per the following preferences to search:\n")
        sources=sourcefunc()
        Keywords=input("Keyword : ").strip().lower()
        fromdate=input("Enter the Date from which you want the news(YYYY-MM-DD) : ")
        todate=input("Enter the Date till which you want the news(YYYY-MM-DD) : ")
        
        
        Max_news=int(input("Maximum news to be recieved upto 100 : "))
        confirm=int(input(("If You want to continue press 1\n or if you want to go back press 9\n or if you want to quit press 0")))
        if(confirm==1):
            sourcefunction(sources,Keywords,fromdate,todate,Max_news)
            
        elif(confirm==9):
            mainmenu()
        elif(confirm==0):
            quit()
        
    elif(mainmenuchoice==4):
        print("Put Your Input as per the following preferences to search:\n")
        category=input("Category ( business,entertainment,health,science,sports,technology ) : ")
        Max_news=int(input("Maximum news to be recieved upto 100 : "))
        confirm=int(input(("If You want to continue press 1\n or if you want to go back press 9\n or if you want to quit press 0")))
        if(confirm==1):
            categoryfunction(category,Max_news)
            
        elif(confirm==9):
            mainmenu()
        elif(confirm==0):
            quit()
    elif(mainmenuchoice==5):
        print("Put Your Input as per the following preferences to search:\n")
        Keywords=input("Keyword : ").strip().lower()
        fromdate=input("Enter the Date from which you want the news(YYYY-MM-DD) : ")
        todate=input("Enter the Date till which you want the news(YYYY-MM-DD) : ")
        Max_news=int(input("Maximum news to be recieved upto 100 : "))
        confirm=int(input(("If You want to continue press 1\n or if you want to go back press 9\n or if you want to quit press 0")))
        if(confirm==1):
            datefunction(Keywords,fromdate,todate,Max_news)
            
        elif(confirm==9):
            mainmenu()
        elif(confirm==0):
            quit()
    

mainmenu()