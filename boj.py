from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime

# define header for urllib request
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/58.0.3029.110 Safari/537.36'
hds = {'User-Agent': user_agent}
hds_json = {'User-Agent': user_agent, 'Content-Type': 'Application/json'}

userInfoURL = "https://www.acmicpc.net/user/"

statusURL = "https://www.acmicpc.net/status?problem_id=&user_id=%s&language_id=-1&result_id=-1"
statusTitle = ["채점 번호", "아이디", "문제 번호", "결과", "메모리", "시간", "언어", "코드 길이", "제출한 시간"]

#req = Request(url, headers=hds)
#res = urlopen(req)
#html = res.read()

#bs = BeautifulSoup(html, 'html.parser')
#tags = bs.findAll('div', attrs={'class': 'col-md-3'})

'''
req = Request(url, headers=hds)
fp = urlopen(req, timeout=10)
source = fp.read()
fp.close()
soup = BeautifulSoup(source, "lxml")

table = soup.find(id="statics")
trs = table.tbody.find_all('td')


for title_text, t in zip(title, trs):
    print(title_text+" "+str(t.text).strip())

#for tag in tags :
    # 검색된 태그에서 a 태그에서 텍스트를 가져옴
#    aa = bs.findAll('a')
#    for a in aa:
#        print(a)
    #print(dir(tag))

'''

def isBOJUser(userID):
    try:
        req = Request(userInfoURL + userID, headers=hds)
        urlopen(req, timeout=5)
    except HTTPError:
        return False
    except UnicodeEncodeError:
        return False
    return True

def getUserInfo(userID):
    req = Request(userInfoURL + userID, headers=hds)
    fp = urlopen(req)
    source = fp.read()
    soup = BeautifulSoup(source, "lxml")

    table = soup.find(id="statics")
    result = []

    for k, v in zip(table.tbody.find_all('th'), table.tbody.find_all('td')):
        result.append((str(k.text).strip(), str(v.text).strip()))
    result[0] = ("랭킹", result[0][1] + " (상위 " + str((int(result[0][1]) * 1000 // 113006)/10) + "%)")
    return result

def getStatus(userID):
    url = statusURL % (userID)
    req = Request(url, headers=hds)
    fp = urlopen(req)
    source = fp.read()
    soup = BeautifulSoup(source, "lxml")

    table = soup.find(id="status-table")
    result = []

    for item in soup.find("tbody").find_all("tr"):
        data_containers = item.find_all("td")

        # [0] 채점 번호 [1] 아이디 [2] 문제 번호 [3] 채점 결과
        # [4] 메모리 (KB) [5] 시간(ms) [6] 언어 [7] 코드 길이
        # [8] 제출 시간
        try:
            result.append([
                "#" + data_containers[2].text,
                data_containers[2].find("a")["title"],
                data_containers[3].text,
                ('∞' if len(data_containers[4].text) == 0 else data_containers[4].text) + " KB",
                ('∞' if len(data_containers[5].text) == 0 else data_containers[5].text) + " ms",
                data_containers[6].text,
                data_containers[7].text + " B",
                data_containers[8].find("a")["title"]
            ])
        except Exception as e:
            print(e)

    return result

def getAcceptedData(userID):
    url = "https://www.acmicpc.net/status?problem_id=&user_id=%s&language_id=-1&result_id=4" % userID
    req = Request(url, headers=hds)
    fp = urlopen(req)
    source = fp.read()
    soup = BeautifulSoup(source, "lxml")

    table = soup.find(id="status-table")
    result = dict()

    last_status_num = 0
    cnt = 5
    day_range = 14

    today = datetime.date.today()
    for i in range(day_range):
        result[str(today.month) + "." + str(today.day)] = 0
        today -= datetime.timedelta(1)

    for i in range(cnt):
        for item in soup.find("tbody").find_all("tr"):
            data_containers = item.find_all("td")
            # [0] 채점 번호 [1] 아이디 [2] 문제 번호 [3] 채점 결과
            # [4] 메모리 (KB) [5] 시간(ms) [6] 언어 [7] 코드 길이
            # [8] 제출 시간
            try:
                last_status_num = int(data_containers[0].text)
                problem_date = str(data_containers[8].find("a")["title"])
                problem_date_token = problem_date.split()
                problem_date = datetime.date(int(problem_date_token[0][0:-1]), int(problem_date_token[1][0:-1]), int(problem_date_token[2][0:-1]))
                if problem_date - datetime.date.today() > datetime.timedelta(days=day_range):
                    return result
                # problem_date = ".".join(problem_date_token[0:3][0:-1])
                problem_date = str(problem_date.month) + "." + str(problem_date.day)
                if problem_date in result:
                    result[problem_date] += 1
            except Exception as e:
                print(e)
        req = Request(url + "&top=" + str(last_status_num - 1), headers=hds)
        fp = urlopen(req)
        source = fp.read()
        soup = BeautifulSoup(source, "lxml")

    return result
