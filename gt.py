import requests
from lxml import html
from lxml import etree
import re
class GT:
    def __init__(self,ip,port=""):
        self.ip = ip
        self.xpath = "-"
        if port == "":
            self.port =27015
        else:       
            try:
                self.port = int(port)
            except ValueError:
                raise TypeError("Port must be int")
        
    def req(self,types="",content=""):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125",}
        try:
            if types == "1":
                url = "top_players/"
            else:
                url=""
            req = requests.get("https://www.gametracker.com/server_info/"+str(self.ip)+":"+str(self.port)+"/"+url,headers=headers,timeout=3)
            if req.status_code==200 and content=="":
                
                return  html.fromstring(req.content)
            elif req.status_code==200 and content!="":          
                return req.text
            else:
                return False
        except:
            return False
    def getinfo(self):
        xpath_data = self.req()
        info = {}
        server_name = xpath_data.xpath('//a[@href="/server_info/'+str(self.ip)+':'+str(self.port)+'/"]/b')[0].text
        
        info["name"] = server_name
        status = xpath_data.xpath('//*[@class="item_color_success" and contains(text(),"Alive")]')
        if len(status) != 1:
            info["status"] = False
            return info
        else:
            info["status"] = True
        info["map"] = re.sub('\s+','',xpath_data.xpath('//*[@id="HTML_curr_map"]')[0].text)
        info["current_players"] = re.sub('\s+','',xpath_data.xpath('//*[@id="HTML_num_players"]')[0].text)
        info["max_players"] = re.sub('\s+','',xpath_data.xpath('//*[@id="HTML_max_players"]')[0].text)
        info["average_players"] = re.sub('\s+','',xpath_data.xpath('//*[@id="HTML_avg_players"]')[0].text)
        last_scan = re.sub('\s+','',xpath_data.xpath('//div[@id="last_scanned"]')[0].text)
        last_scan.replace("Last scanned ","")
        last_scan.replace(" ago ","")
        
        nums = ""
        for letter in last_scan:
            try:
                nums+=str(int(letter))
            except ValueError:
                pass
        
        if last_scan.find("minute") != -1:
            info["last_scan_mins"] = nums[0]
            info["last_scan_secs"] = nums[1:]
        else:
            info["last_scan_mins"] = "0"
            info["last_scan_secs"] = nums
        rank_xpath = xpath_data.xpath('//span[@class="item_color_title" and contains(text(),"Game Server Rank:")]/following-sibling::text()')
        if len(rank_xpath) > 4:
            info["rank"] = re.sub('\s+','',rank_xpath[0][:-4])
            info["rank_higest"] = re.sub('\s+','',rank_xpath[4][:-4])[:-2]
            info["rank_lowest"] = re.sub('\s+','',rank_xpath[-1])[:-2]
        else:
            info["rank"] = False
            info["rank_higest"] = False
            info["rank_lowest"] = False
       
        names = xpath_data.xpath('//*[@id="HTML_online_players"]/div/table/tr/td[2]/a')
        frags = xpath_data.xpath('//*[@id="HTML_online_players"]/div/table/tr/td[3]')
        times = xpath_data.xpath('//*[@id="HTML_online_players"]/div/table/tr/td[4]')
        info["players"] = []
        i=1
        for player in names:
            player_dict = {
                "name": re.sub('\s+','',player.text),
                "frag":re.sub('\s+','',frags[i].text),
                "time":re.sub('\s+','',times[i].text)
            }
            info["players"].append(player_dict)
            i+=1
        info["top_players"] = []
        xpath2 = xpath_data = self.req(types="1")
        top_names = xpath2.xpath('//table[@class="table_lst table_lst_spn"]/tr/td[2]/a')
        top_frags = xpath2.xpath('//table[@class="table_lst table_lst_spn"]/tr/td[4]')
        top_times = xpath2.xpath('//table[@class="table_lst table_lst_spn"]/tr/td[5]')
        
        info["top_players"] = []
        i=0
        for player in top_names:
            player_dict = {
                "name": re.sub('\s+','',player.text),
                "frag":re.sub('\s+','',top_frags[i].text),
                "time":re.sub('\s+','',top_times[i].text)
            }
            info["top_players"].append(player_dict)
            i+=1
        info["top_players"] = info["top_players"][1:-1]
        site = self.req(content="1")
        
        index1 = site.find("var GSID = ") + len("var GSID = ")
        gsid = ""
        for i in range(0,10):
            
            
            if site[index1+i] == ";":
                break
            elif " " in site[index1+i]:
                pass
            else:
                
                gsid+=site[index1+i]

	    
        
        info["img"] = {}
        info["img"]["server_map_api"] = "https://cache.gametracker.com/images/graphs/server_maps.php?GSID="+gsid
        info["img"]["server_rank_api"] = "https://cache.gametracker.com/images/graphs/server_rank.php?GSID="+gsid
        info["img"]["server_players_api_d"] = "https://cache.gametracker.com/images/graphs/server_players.php?GSID="+gsid+"&start=-1d"
        info["img"]["server_players_api_w"] = "https://cache.gametracker.com/images/graphs/server_players.php?GSID="+gsid+"&start=-1w"
        info["img"]["server_players_api_m"] = "https://cache.gametracker.com/images/graphs/server_players.php?GSID="+gsid+"&start=-1m"
        
        return info

        
        
if __name__ == "__main__":
    sinif = GT("185.198.75.17","27015")
    print(sinif.getinfo())
