# Asylum-restaurant-map
將這類社會企業( 庇護餐廳、庇護工場 )的旅遊行程變成一個方便的一條龍旅遊模式，將光顧這些店面成為國內假日觀光慣性、熱門的選擇
## 網頁資料
[喜憨兒社會福利基金會](https://www.c-are-us.org.tw/ "游標顯示")、[善耕harvest365公益媒合平台](https://www.harvest365.org/posts/7648 "游標顯示")
### Python爬取方法
透過 Beautiful Soup  、 string、 regular expression爬取網頁中有關社會事業的資料，獲取烘焙工坊、庇護餐廳、工廠的地址， 並運用dictionary、list，將位置資訊、店家型態分類。
### 喜憨兒社會福利基金會：
找尋網頁上各地區庇護餐廳名稱與位置地址，將資料抓取出來對應成相映字典。
### 善耕harvest365公益媒合平台：
1. 抓取網頁上各庇護餐廳名稱與位置地址，將資料對應成相映字典。
2. 爬取一些報導的名稱與內文裡的地址，將資料對應成相映字典。
## Run
1.	下載和import：  pandas、urllib.request 、 json 、 re 、 Translator 、 urllib.request, urllib.parse, urllib.error 、 BeautifulSoup 、  requests
2.	運行 tatal.py
3.	輸入地址：EX.臺北市(臺北、臺南的臺要跟氣象局一樣使用「臺」)
4.	輸入預計啟程日期(約當日起一個禮拜內)
5.	根據顯現的天氣狀況，挑選心儀地點，並輸入一個按ENTER一次，跳至下個環節按Q 。  
  EX.溫古咖啡 Wengu cafe →築地鮮魚→ Dancing Pig Bistro→Q
6.	出現庇護餐廳名稱與地址，根據地址選取較鄰近之店家，輸入店家名(不要輸入地址)一個按一次ENTER，跳至下個環節按Q。  
  EX. 未來咖啡→Q
7.	出現烘焙坊名稱與地址，根據地址選取較鄰近之店家，輸入店家名(不要輸入地址)一個按一次ENTER，跳至下個環節按Q。  
  EX. 立德烘焙屋→Q
9.	出現每個點之間的開車應花費的距離，可供使用者排行程之使用
10.	若要退出直接按大寫B

