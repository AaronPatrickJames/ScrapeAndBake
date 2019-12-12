#THIS IS NOT MY OWN WORK THIS WAS A FOLLOW ALONG LESSON
#https://www.youtube.com/watch?v=N0ph2a6Vd7M&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=12


from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

#random 3 letter website
def random_starting_url():
    starting=''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))#random 3 letter gen
    url = ''.join(['http://',starting,'.com'])#makelink
    return url


def handle_local_links(url, link):
    if link.startswith('/'):
        return ''.join([url,link])
    else:
        return link

def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]#get all the A Tags, or if it finds no tags runs exception
        links = [handle_local_links(url,link) for link in links]
        links = [str(link.encode("ascii")) for link in links]
        return links
    except TypeError as e:
        print(e)
        print('got a typeError, prob a none type')
        return[]
    except IndexError as e:
        print(e)
        print('no useful links')
        return []
    except AttributeError as e:
        print(e)
        print('No links found')
        return []
    except Exception as e:
        print(str(e))
        #add error if any found to log no log made for right now
        return[]

def main():
    #amount of processes we run
    how_many = 20
    p = Pool(processes=how_many)#process pool
    parse_us = [random_starting_url() for _ in range(how_many)]#process 20 links as fast as possible (20 processes) slap them into a list
    data = p.map(get_links, [link for link in parse_us])#get links with arguments that each link in parse us gets pushed into it maps each one to a process 
    data = [url for url_list in data for url in url_list]#for statment worked backwards(look below to see the same thing commented out
    #for url_list in data:
    #   for url in url_list:
    #       data.appened(url)
    p.close()

    #open and close write file stream to write file
    with open('urls_list.txt', 'w') as f:
        f.write(str(data))

if __name__ == "__main__":
    main()
