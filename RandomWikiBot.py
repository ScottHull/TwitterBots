import urllib2, time, twython, BeautifulSoup, datetime, sys
from pytz import timezone

#this bot generates a random Wikipedia link and tweets both the title of the article and the link
#this bot runs hourly if left open

APP_KEY = '#--INSERT APP KEY--'
APP_SECRET = '#--INSERT APP SECRET KEY--'
twitter = twython.Twython(APP_KEY, APP_SECRET, oauth_token='#--INSERT OAUTH TOKEN', oauth_token_secret='#--INSERT OAUTH TOKEN SECRET--')


def getarticle():
    try:
        print("\nFinding an article...")
        url = 'http://en.wikipedia.org/wiki/Special:Random'
        req = urllib2.urlopen(url) #opens the wikipedia randomly generated URL
        newurl = req.geturl()
        print("The random URL is: " + newurl)
        req2 = urllib2.urlopen(newurl).read()
        soup = BeautifulSoup.BeautifulSoup(req2) #Parses the page
        articletitle = soup.title.string[:-35] #Exctracts article title
        print("The article title is: " + articletitle + "\n")
        tweetline = articletitle + ": " + newurl
        print("Posting tweet: " + tweetline)
        twitter.update_status(status=tweetline)
        tz = timezone('US/Eastern')
        thetime = datetime.datetime.now(tz)
        futuretime = datetime.datetime.now(tz) + datetime.timedelta(hours=1) #Sets bot to repeat the process hourly
        print("Tweet posted at: " + str(thetime) + " EST")
        print("Next tweet will be posted at: " + str(futuretime) + " EST")
        print("\n_________________________\n")
        print("\n")
        time.sleep(3600)
    except KeyboardInterrupt:
        print("The user has interrupted the operation.  Exiting...\n\n")
        print("\n_________________________\n")
        sys.exit()
    except:
        print("\nError!  Retrying...\n")
        getarticle()

getarticle()


