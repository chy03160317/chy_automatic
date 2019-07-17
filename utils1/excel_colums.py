class excelvariables:
	caseID=0
	URL=2
	requestData=3
	expectResult=4
	actualResult=5

def getCaseID():
	return excelvariables.caseID
def getUrl():
	return excelvariables.URL
def getRequestData():
	return excelvariables.requestData
def getExpectResult():
	return excelvariables.expectResult
def getActualResult():
	return excelvariables.actualResult

def getLagouHeader():
	headers={
		"Content - Type":"application / x - www - form - urlencoded;charset = UTF - 8",
		"User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
		"Referer":"https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=",
		"Cookie":"_ga=GA1.2.1903137.1550031907; user_trace_token=20190213122508-5860c9a4-2f47-11e9-b4a4-525400f775ce; LGUID=20190213122508-5860cc26-2f47-11e9-b4a4-525400f775ce; LG_HAS_LOGIN=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a8ac7e0b2370-06ab60bd731671-9393265-1327104-16a8ac7e0b332b%22%2C%22%24device_id%22%3A%2216a8ac7e0b2370-06ab60bd731671-9393265-1327104-16a8ac7e0b332b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAAGFABEF6445C3D8520A61BD722741447842A3A7; _gid=GA1.2.1600398941.1562821413; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562821413; LG_LOGIN_USER_ID=5ff76eb3512091e217a73b9389b54521dd5fad97d0b0ab2f; _putrc=A586D67552BA8518; login=true; unick=%E9%99%88%E4%BC%9A%E8%89%B3; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=401; gate_login_token=f2c8c8ef4bed1b46b28d55fc8ebc60c520cd6cf1ff99828d; privacyPolicyPopup=false; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; _gat=1; LGSID=20190711215814-ed501319-a3e3-11e9-a4de-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; X_HTTP_TOKEN=a49681895d82320c4153582651b5e4f2fc4eebe512; LGRID=20190711215834-f905602e-a3e3-11e9-be7f-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562853513; SEARCH_ID=122f5ee92eac4de392dc7b0807051f6b"
	}
	return headers