
# -*- coding: utf-8 -*-
# Script developed by Ashish Ghori
# Version 1.0

import csv
import html
import os
import random
import re
import time
import unicodedata
from lxml import html
import sys
import requests


class JamabandiName:
    def __init__(self):
        self.output_file = 'Output'
        self.PNF_file = 'PNF'
        self.current_path = os.path.dirname(os.path.abspath(__file__) + "/")
        self.current_path = '\\'.join(self.current_path.split('\\')[:-1]) + '\\'

    def Initiate(self):

        try:
            print(self.current_path)
            with open(self.current_path + "Input.txt", "r", encoding='utf-8') as f:
                inputs = f.readlines()
            try:
                with open(self.current_path + "Resume.txt", "r", encoding='utf-8') as f:
                    temp_data = f.readlines()
                self.resume = inputs.index(temp_data[0]) + 1

            except Exception as e:
                self.puse_data_to_file("district_name\tdistrict_code\ttehsil_name\ttehsil_code\tvillage_name\tvillage_code\tjamabandi_Year\tkhasra_number\tkhewat_no\tkhatoni_no\thtml_link\tinner_details\n")
                # self.puse_data_to_file_others_domain("Phone_Number\tDomain\tInput\n"
                with open(self.current_path + "Resume.txt", "w", encoding='utf-8') as f:
                    pass
                self.resume = 0
                pass
            i = self.resume
            for data in inputs[self.resume:]:

                if data[0] != "#":
                    line = data.split("\t")
                    url = 'https://jamabandi.nic.in/land%20records/NakalRecord'
                    district_name_input = line[0]
                    tehsil_name_input  = line[1]
                    village_name_input  = line[2]
                    khasra_number = line[3].replace('\n','')
                    if url != " ":
                        self.input_url = url.rstrip()
                        print("\n khasra_number-----", khasra_number)
                        # print("-------------{}/{}------\n".format(str(i)))
                        self.Hitting_url(self.input_url,district_name_input,tehsil_name_input,village_name_input,khasra_number, False, False)
                    with open(self.current_path + '/' + "Resume.txt", "w", encoding='utf-8') as f:
                        f.write(str(data))
                i += 1

        except Exception as e:
            print(e)

    def Hitting_url(self, url,district_name_input,tehsil_name_input,village_name_input,khasra_number, Main, is_paginated):
        self.retries = 0
        while True:
            try:

                headers = {
                    "authority": "jamabandi.nic.in",
                    "method": "GET",
                    "path": "/land%20records/NakalRecord",
                    "scheme": "https",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Cache-Control": "max-age=0",
                    "Cookie": "jamabandiID=t1bmfhugh5wxbqtt5zynmajy",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",

                }

                domain_response = requests.get(url, headers=headers)
                tree = html.fromstring(domain_response.text)
                VIEWSTATE = tree.xpath('//input[@ id="__VIEWSTATE"]//@value')[0]
                EVENTVALIDATION = tree.xpath('//input[@id="__EVENTVALIDATION"]//@value')[0]
                session = requests.Session()
                session.headers.update({"authority": "jamabandi.nic.in",
                                        "method": "POST",
                                        "path": "/land%20records/NakalRecord",
                                        "scheme": "https",
                                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                        "Accept-Encoding": "gzip, deflate, br",
                                        "Accept-Language": "en-US,en;q=0.9",
                                        "Cache-Control": "max-age=0",
                                        "Content-Length": "3423",
                                        "Content-Type": "application/x-www-form-urlencoded",
                                        "Cookie": "jamabandiID=t1bmfhugh5wxbqtt5zynmajy",
                                        "Origin": "https://jamabandi.nic.in",
                                        "Referer": "https://jamabandi.nic.in/land%20records/NakalRecord",
                                        "Sec-Ch-Ua-Mobile": "?0",
                                        "Sec-Fetch-Dest": "document",
                                        "Sec-Fetch-Mode": "navigate",
                                        "Sec-Fetch-Site": "same-origin",
                                        "Sec-Fetch-User": "?1",
                                        "Upgrade-Insecure-Requests": "1",
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                                        })
                payload_main = {
                    "__EVENTTARGET": "ctl00$ContentPlaceHolder1$RdobtnKhasra",
                    "__EVENTARGUMENT": "",
                    "__LASTFOCUS": "",
                    "__VIEWSTATE": f"{VIEWSTATE}",
                    "__VIEWSTATEGENERATOR": "9C91F57C",
                    "__SCROLLPOSITIONX": "0",
                    "__SCROLLPOSITIONY": "0",
                    "__VIEWSTATEENCRYPTED": "",
                    "__EVENTVALIDATION": f"{EVENTVALIDATION}",
                    "ctl00$ContentPlaceHolder1$a": "RdobtnKhasra",
                    "ctl00$ContentPlaceHolder1$ddldname": "-1",
                }
                main_response = session.post(url, data=payload_main)
                main_tree = html.fromstring(main_response.text)
                VIEWSTATE_main = main_tree.xpath('//input[@ id="__VIEWSTATE"]//@value')[0]
                EVENTVALIDATION_main = main_tree.xpath('//input[@id="__EVENTVALIDATION"]//@value')[0]

                '''------district--------'''

                check_total_district = main_tree.xpath("//*[contains(text(),'Select District')]//..//select//option")

                for i in range(2, len(check_total_district)):
                    district_name = main_tree.xpath(f"//*[contains(text(),'Select District')]//..//select//option[{i}]//text()")[0]
                    district_code = main_tree.xpath(f"//*[contains(text(),'Select District')]//..//select//option[{i}]//@value")[0]
                    if district_name_input == district_name:
                        break
                district_payload = {
                    "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddldname",
                    "__EVENTARGUMENT": "",
                    "__LASTFOCUS": "",
                    "__VIEWSTATE": f"{VIEWSTATE_main}",
                    "__VIEWSTATEGENERATOR": "9C91F57C",
                    "__SCROLLPOSITIONX": "0",
                    "__SCROLLPOSITIONY": "0",
                    "__VIEWSTATEENCRYPTED": "",
                    "__EVENTVALIDATION": f"{EVENTVALIDATION_main}",
                    "ctl00$ContentPlaceHolder1$a": "RdobtnKhasra",
                    "ctl00$ContentPlaceHolder1$ddldname": f"{district_code}",
                    # "ctl00$ContentPlaceHolder1$ddltname": "006",
                }
                district_response = session.post(url, data=district_payload)

                district_tree = html.fromstring(district_response.text)
                VIEWSTATE_district = district_tree.xpath('//input[@ id="__VIEWSTATE"]//@value')[0]
                EVENTVALIDATION_district = district_tree.xpath('//input[@id="__EVENTVALIDATION"]//@value')[0]

                """------tehsil----"""

                check_total_tehsil = district_tree.xpath("//*[contains(text(),'Select Tehsil/ Sub-Tehsil')]//..//select//option")
                for j in range(1, len(check_total_tehsil)):
                    tehsil_name = district_tree.xpath(f"//*[contains(text(),'Select Tehsil/ Sub-Tehsil')]//..//select//option[{j}]//text()")[0]
                    tehsil_code = district_tree.xpath(f"//*[contains(text(),'Select Tehsil/ Sub-Tehsil')]//..//select//option[{j}]//@value")[0]
                    if tehsil_name_input == tehsil_name:
                        break

                tehsil_payload = {
                    "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddltname",
                    "__EVENTARGUMENT": "",
                    "__LASTFOCUS": "",
                    "__VIEWSTATE": f"{VIEWSTATE_district}",
                    "__VIEWSTATEGENERATOR": "9C91F57C",
                    "__SCROLLPOSITIONX": "0",
                    "__SCROLLPOSITIONY": "0",
                    "__VIEWSTATEENCRYPTED": "",
                    "__EVENTVALIDATION": f"{EVENTVALIDATION_district}",
                    "ctl00$ContentPlaceHolder1$a": "RdobtnKhasra",
                    "ctl00$ContentPlaceHolder1$ddldname": f"{district_code}",
                    "ctl00$ContentPlaceHolder1$ddltname": f"{tehsil_code}",
                }
                tehsil_response = session.post(url, data=tehsil_payload)
                # print(tehsil_response.text)
                tehsil_tree = html.fromstring(tehsil_response.text)
                # print(tehsil_response.text)
                VIEWSTATE_tehsil = tehsil_tree.xpath('//input[@ id="__VIEWSTATE"]//@value')[0]
                EVENTVALIDATION_tehsil = tehsil_tree.xpath('//input[@id="__EVENTVALIDATION"]//@value')[0]


                """--------village-----------"""
                check_total_village = tehsil_tree.xpath("//*[contains(text(),'Select Village')]//..//select//option")
                for k in range(2, len(check_total_village)):
                    village_name = tehsil_tree.xpath(f"//*[contains(text(),'Select Village')]//..//select//option[{k}]//text()")[0]
                    village_code = tehsil_tree.xpath(f"//*[contains(text(),'Select Village')]//..//select//option[{k}]//@value")[0]
                    if village_name_input == village_name:
                        break
                village_payload = {
                    "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddlvname",
                    "__EVENTARGUMENT": "",
                    "__LASTFOCUS": "",
                    "__VIEWSTATE": f"{VIEWSTATE_tehsil}",
                    "__VIEWSTATEGENERATOR": "9C91F57C",
                    "__SCROLLPOSITIONX": "0",
                    "__SCROLLPOSITIONY": "0",
                    "__VIEWSTATEENCRYPTED": "",
                    "__EVENTVALIDATION": f"{EVENTVALIDATION_tehsil}",
                    "ctl00$ContentPlaceHolder1$a": "RdobtnKhasra",
                    "ctl00$ContentPlaceHolder1$ddldname": f"{district_code}",
                    "ctl00$ContentPlaceHolder1$ddltname": f"{tehsil_code}",
                    "ctl00$ContentPlaceHolder1$ddlvname": f"{village_code}",
                    # "ctl00$ContentPlaceHolder1$ddlPeriod":"2022-2023",
                }
                village_response = session.post(url, data=village_payload)
                village_tree = html.fromstring(village_response.text)
                VIEWSTATE_village = village_tree.xpath('//input[@ id="__VIEWSTATE"]//@value')[0]
                EVENTVALIDATION_village = village_tree.xpath('//input[@id="__EVENTVALIDATION"]//@value')[0]


                year = village_tree.xpath("//*[contains(text(),'Jamabandi Year')]//..//select//option[2]//text()")[0]
                year_payload = {
                    "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddlPeriod",
                    "__EVENTARGUMENT": "",
                    "__LASTFOCUS": "",
                    "__VIEWSTATE": f"{VIEWSTATE_village}",
                    "__VIEWSTATEGENERATOR": "9C91F57C",
                    "__SCROLLPOSITIONX": "0",
                    "__SCROLLPOSITIONY": "0",
                    "__VIEWSTATEENCRYPTED": "",
                    "__EVENTVALIDATION": f"{EVENTVALIDATION_village}",
                    "ctl00$ContentPlaceHolder1$a": "RdobtnKhasra",
                    "ctl00$ContentPlaceHolder1$ddldname": f"{district_code}",
                    "ctl00$ContentPlaceHolder1$ddltname": f"{tehsil_code}",
                    "ctl00$ContentPlaceHolder1$ddlvname": f"{village_code}",
                    "ctl00$ContentPlaceHolder1$ddlPeriod": f"{year}",
                }
                year_response = session.post(url, data=year_payload)
                year_tree = html.fromstring(year_response.text)
                VIEWSTATE_year = year_tree.xpath('//input[@ id="__VIEWSTATE"]//@value')[0]
                EVENTVALIDATION_year = year_tree.xpath('//input[@id="__EVENTVALIDATION"]//@value')[0]

                data_list = []
                khasra_payload = {
                    "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddlkhasra",
                    "__EVENTARGUMENT": "",
                    "__LASTFOCUS": "",
                    "__VIEWSTATE": f"{VIEWSTATE_year}",
                    "__VIEWSTATEGENERATOR": "9C91F57C",
                    "__SCROLLPOSITIONX": "0",
                    "__SCROLLPOSITIONY": "0",
                    "__VIEWSTATEENCRYPTED": "",
                    "__EVENTVALIDATION": f"{EVENTVALIDATION_year}",
                    "ctl00$ContentPlaceHolder1$a": "RdobtnKhasra",
                    "ctl00$ContentPlaceHolder1$ddldname": f"{district_code}",
                    "ctl00$ContentPlaceHolder1$ddltname": f"{tehsil_code}",
                    "ctl00$ContentPlaceHolder1$ddlvname": f"{village_code}",
                    "ctl00$ContentPlaceHolder1$ddlPeriod": f"{year}",
                    "ctl00$ContentPlaceHolder1$ddlkhasra": f"{khasra_number}",

                }
                khasra_response = session.post(url, data=khasra_payload)
                khasra_tree = html.fromstring(khasra_response.text)
                VIEWSTATE_khasra = khasra_tree.xpath('//input[@ id="__VIEWSTATE"]//@value')[0]
                EVENTVALIDATION_khasra = khasra_tree.xpath('//input[@id="__EVENTVALIDATION"]//@value')[0]
                nakal_payload = {
                    "__EVENTTARGET": "ctl00$ContentPlaceHolder1$GridView1",
                    "__EVENTARGUMENT": "",
                    "__LASTFOCUS": "",
                    "__VIEWSTATE": f"{VIEWSTATE_khasra}",
                    "__VIEWSTATEGENERATOR": "9C91F57C",
                    "__SCROLLPOSITIONX": "0",
                    "__SCROLLPOSITIONY": "0",
                    "__VIEWSTATEENCRYPTED": "",
                    "__EVENTVALIDATION": f"{EVENTVALIDATION_khasra}",
                    "ctl00$ContentPlaceHolder1$a": "RdobtnKhasra",
                    "ctl00$ContentPlaceHolder1$ddldname": f"{district_code}",
                    "ctl00$ContentPlaceHolder1$ddltname": f"{tehsil_code}",
                    "ctl00$ContentPlaceHolder1$ddlvname": f"{village_code}",
                    "ctl00$ContentPlaceHolder1$ddlPeriod": f"{year}",
                    "ctl00$ContentPlaceHolder1$ddlkhasra": f"{khasra_number}",

                }
                nakal_response = session.post(url, data=nakal_payload)
                khewat_no = khasra_tree.xpath("//td//a[contains(text(),'Nakal')]//..//following-sibling::td[1]//text()")[0]
                khatoni_no = khasra_tree.xpath("//td//a[contains(text(),'Nakal')]//..//following-sibling::td[2]//text()")[0]
                html_url = 'https://jamabandi.nic.in/land%20records/Nakal_khewat'
                inner_details_list = []
                hadbast_no = khasra_tree.xpath("//div[contains(text(),'Hadbast No.')]//following-sibling::div//span//text()")[0]

                inner_details_list.append(f'village(गांव) : {village_name}')
                inner_details_list.append(f'hadbastNo(हदब):{hadbast_no}')
                inner_details_list.append(f'tehsil(तहसील):{tehsil_name}')
                inner_details_list.append(f'district(िजला):{district_name}')
                inner_details_list.append(f'year (साल):{year}')
                inner_details = ' | '.join(inner_details_list)
                if khasra_number != '':
                    data_list.append(district_name)
                    data_list.append(district_code)
                    data_list.append(tehsil_name)
                    data_list.append(tehsil_code)
                    data_list.append(village_name)
                    data_list.append(village_code)
                    data_list.append(year)
                    data_list.append(khasra_number)
                    data_list.append(khewat_no)
                    data_list.append(khatoni_no)
                    data_list.append(html_url)
                    data_list.append(inner_details)
                    out_data = '\t'.join(data_list) + '\n'
                    self.puse_data_to_file(out_data)
                    print('--data insert in output.txt file---')
                    break


            except Exception as e:
                print('please check in response')
                pnf_data= district_code + '\t' + tehsil_code +'\t' + village_code + '\t' +khasra_number +'\n'
                self.puse_data_to_PNF(pnf_data)
                break




    def remove_junk(self, text):
        text = re.sub('\s+|\\\\t|\\t', ' ', str(text).strip())
        text = re.sub('\\\\n|\\\\r|\\n|\\r', '', text.strip())
        text = str(text).replace('\r', ' ').replace('\n', '').replace('\t', ' ')
        text = text.replace('    ', ' ').replace('  ', ' ')
        text = text.replace(';', '')
        text = text.strip()
        return text

    def puse_data_to_file(self, data):
        with open(self.current_path + self.output_file + ".txt", "a", encoding='utf-8') as f:
            f.write(data)

    def puse_data_to_PNF(self, data):
        with open(self.current_path + self.PNF_file + ".txt", "a", encoding='utf-8') as f:
            f.write(data)
    def puse_data_to_csv(self, data):
        with open('Output.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([data])


    def get_user_agent(self):
        temp = [
            "Mozilla/5.0 (Linux; Android 12; SM-A137F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "yacybot (/global; amd64 Linux 5.13.0-52-generic; java 11.0.15; Europe/es) http://yacy.net/bot.html",
            "yacybot (webportal-global; amd64 Linux 5.13.0-52-generic; java 11.0.15; Europe/es) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.10.0-9-amd64; java 11.0.14; Etc/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.18.5-gentoo; java 17.0.3; Europe/de) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.17.9-gnu-hardened1-1-hardened; java 18.0.1.1; Europe/en) http://yacy.net/bot.html",
            "yacybot (freeworld/global; amd64 Linux 5.10.0-13-amd64; java 11.0.15; Etc/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Windows 10 10.0; java 1.8.0_331; Europe/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.17.7-gnu-hardened1-1-hardened; java 1.8.0_332; Europe/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.10.0-12-amd64; java 1.8.0_212; GMT/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.17.7-gentoo; java 17.0.3; Europe/de) http://yacy.net/bot.html",
            "yacybot (-global; amd64 Linux 4.19.0-20-amd64; java 11.0.15; Etc/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 4.15.0-176-generic; java 1.8.0_242; Etc/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 4.4.301; java 1.8.0_322; US/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.17.4-arch1-1; java 18.0.1; US/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.4.0-109-generic; java 11.0.15; Europe/en) http://yacy.net/bot.html",
            "yacybot (-global; amd64 Linux 5.15.12-gnu-1; java 17.0.3; UTC/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 4.19.0-19-amd64; java 11.0.14; America/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Linux 5.4.0-99-generic; java 11.0.13; Etc/en) http://yacy.net/bot.html",
            "yacybot (/global; amd64 Windows 11 10.0; java 17.0.2; Europe/en) http://yacy.net/bot.html",

        ]
        temp_user_agent = random.choice(temp).replace("\n", "")
        return temp_user_agent

if __name__ == "__main__":
    class_obj = JamabandiName()
    class_obj.Initiate()
