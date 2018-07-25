import sys
import requests
from bs4 import BeautifulSoup

# Import, Parse arguments
args = sys.argv
params = args[1:]

for param in params:
    if 'domain' in param:
        domain = param[param.find('=')+1:]
        #print("domain="+domain)
    elif 'id' in param:
        domain_id = param[param.find('=')+1:]
        #print("id="+domain_id)
    elif 'user' in param:
        user = param[param.find('=')+1:]
        #print("user="+user)
    elif 'password' in param:
        password = param[param.find('=')+1:]
        #print("password="+password)
    elif 'name1' in param:
        name1 = param[param.find('=')+1:]
        #print("name1="+name1)
    elif 'ip1' in param:
        ip1 = param[param.find('=')+1:]
        #print("ip1="+ip1)
    elif 'name2' in param:
        name2 = param[param.find('=')+1:]
        #print("name2="+name2)
    elif 'ip2' in param:
        ip2 = param[param.find('=')+1:]
        #print("ip2="+ip2)


session = requests.session()

url = "https://my.freenom.com/clientarea.php?managedns="+domain+"&domainid="+domain_id
res1 = session.get(url)
cont1 = res1.content
soup1 = BeautifulSoup(cont1, 'html.parser')
token1 = soup1.find('input',{'name':'token'})
#print(token1.get('value'))

session.headers.update({
    'Host':'my.freenom.com',
    'Connection':'keep-alive',
    'Content-Length':'104',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Origin':'https://my.freenom.com',
    'Upgrade-Insecure-Requests':'1',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': url,
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ja,en-US;q=0.9,en;q=0.8'})
payload1 = {
    'token':token1.get('value'),
    'username':user,
    'password':password}
res2 = session.post("https://my.freenom.com/dologin.php", payload1)
res2.raise_for_status()

cont2 = res2.content
soup2 = BeautifulSoup(cont2, 'html.parser')
token2 = soup2.find('input',{'name':'token'})
#print(token2.get('value'))

session.headers.update({
    'Host':'my.freenom.com',
    'Connection':'keep-alive',
    'Content-Length':'104',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Origin':'https://my.freenom.com',
    'Upgrade-Insecure-Requests':'1',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': url,
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ja,en-US;q=0.9,en;q=0.8'})
payload2 = {
    'token':token2.get('value'),
    'dnsaction':'modify',
    'records[0][line]':'',
    'records[0][type]':'A',
    'records[0][name]':name1,
    'records[0][ttl]':'300',
    'records[0][value]':ip1,
    'records[1][line]':'',
    'records[1][type]':'A',
    'records[1][name]':name2,
    'records[1][ttl]':'300',
    'records[1][value]':ip2}
res3 = session.post(url, payload2)
res3.raise_for_status()

#print(res3.text)
cont3 = res3.content
soup3 = BeautifulSoup(cont3, 'html.parser')
messages = soup3.find_all('li', {'class':'dnssuccess'})

for msgstr in messages:
    print("    ["+domain+"] "+name1+":"+ip1+', '+name2+":"+ip2+"=>"+msgstr.text)

print("    fin.")
