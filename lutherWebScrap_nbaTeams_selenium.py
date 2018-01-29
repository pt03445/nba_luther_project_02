# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:53:22 2018

@author: dtalakala
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import collections
import time
import csv

driver = webdriver.Chrome('C:/Users/dtalakala/Desktop/chromeDriver/chromedriver_win32/chromedriver')
driver.get('http://stats.nba.com/teams/traditional/#!?sort=W_PCT&dir=-1')

time.sleep(2)

csv_file = open('nbateamstats_Final.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['TEAM', 'GP', 'W', 'L', 'WIN%', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', '+/-', 'YEAR'])

links = []
    
def get_team_details():
    return driver.find_elements_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')
    

def get_node_value(team, index):
    value = ''
    try:
        value = team.find_element_by_xpath('.//td['+str(index)+']').text
    except Exception as error:
        try:
            value = team.find_element_by_xpath('.//td['+str(index)+']/a').text
        except Exception as another_error:
            value = ''
            print(another_error)
    return value

def get_all_years():

    current_year_combo = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/label/select')    
    all_options = current_year_combo.find_elements_by_xpath('.//option')
    
    for option in all_options:
        option.click()
        
        time.sleep(5)
    
        #current_year = current_year_combo.find_element_by_xpath('.//option[@selected="selected"]').text
        current_year = option.text
        
        print('==> Loading for ', current_year)
        
        teams = get_team_details()
        
        for team in teams:
        
            teams_dict = collections.OrderedDict()
            link = team.find_element_by_xpath('.//td[2]/a').get_attribute('href')
            Team = get_node_value(team, 2)
            
            print ('Processing --> ' , Team)
            
            GP = get_node_value(team, 3)
            W = get_node_value(team, 4)
            L = get_node_value(team, 5)
            Winper = get_node_value(team, 6)
            Min = get_node_value(team, 7)
            Pts = get_node_value(team, 8)
            FGM = get_node_value(team, 9)
            FGA = get_node_value(team, 10)
            FGper = get_node_value(team, 11)
            threePM = get_node_value(team, 12)
            threePA = get_node_value(team, 13)
            threePper = get_node_value(team, 14)
            FTM = get_node_value(team, 15)
            FTA = get_node_value(team, 16)
            FTper = get_node_value(team, 17)
            OReb = get_node_value(team, 18)
            DReb = get_node_value(team, 19)
            Reb = get_node_value(team, 20)
            Ast = get_node_value(team, 21)
            TOv = get_node_value(team, 22)
            Stl = get_node_value(team, 23)
            Blk = get_node_value(team, 24)
            BlkA = get_node_value(team, 25)
            PF = get_node_value(team, 26)
            PFD = get_node_value(team, 27)
            plusMinus = get_node_value(team, 28)
            
            links.append([link, Team.replace(' ','')])
        
            teams_dict['Team'] = Team
            teams_dict['GP'] = GP
            teams_dict['W'] = W
            teams_dict['L'] = L
            teams_dict['Winper'] = Winper
            teams_dict['Min'] = Min
            teams_dict['Pts'] = Pts
            teams_dict['FGM'] = FGM
            teams_dict['FGA'] = FGA
            teams_dict['FGper'] = FGper
            teams_dict['threePM'] = threePM
            teams_dict['threePA'] = threePA
            teams_dict['threePper'] = threePper
            teams_dict['FTM'] = FTM
            teams_dict['FTA'] = FTA
            teams_dict['FTper'] = FTper
            teams_dict['OReb'] = OReb
            teams_dict['DReb'] = DReb
            teams_dict['Reb'] = Reb
            teams_dict['Ast'] = Ast
            teams_dict['TOv'] = TOv
            teams_dict['Stl'] = Stl
            teams_dict['Blk'] = Blk
            teams_dict['BlkA'] = BlkA
            teams_dict['PF'] = PF
            teams_dict['PFD'] = PFD
            teams_dict['plusMinus'] = plusMinus    
            teams_dict['YEAR'] = current_year
        
            writer.writerow(teams_dict.values())
get_all_years()
csv_file.close()
driver.close()

