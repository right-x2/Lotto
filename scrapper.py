import requests
import random
from bs4 import BeautifulSoup



def extract_num(no):
    result = requests.get(f"https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={no}")
    soup = BeautifulSoup(result.text,"html.parser")
    win_num = soup.find("div", {"class":"num win"}).find_all("span")

    win = []
    for i in win_num:
      win.append(int(i.string))
    print(win)
    print(no)

def select_num():
  arr = []
  while(len(arr)<6):
    num = random.randrange(1,45)
    if(num in arr):
      continue
    else:
      arr.append(num)
  return arr

def get_nums():
  jobs = []
  nums = []
  temp =[]
  for i in range(1,908):
    print("haha")
    temp = extract_num(i)
    if(temp in jobs):
      nums.append(temp)
    else:
      jobs.append(extract_num(i))
  return jobs

def my_choice():
  total_num = get_nums()
  arr = []
  temp = []
  while(len(arr)<5):
    temp = select_num()
    if(temp in total_num):
      continue
    else:
      arr.append(temp)
  return arr