#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gspread
import pygsheets

gc = gspread.service_account('credentials.json')

client = pygsheets.authorize()
# Open a sheet from a spreadsheet in one go
sh  = client.open_by_key("13MDkXxt9pSbPWtqJK0DXHH81kTCjg2Y_1RJa7mgALCQ")

# Select worksheet by index. Worksheet indexes start from zero:
wks = sh[2]


# open a worksheet as in the first example.

header = wks.cell('A1')
header.value = 'Names'
header.text_format['bold'] = True # make the header bold
header.update()

# The same can be achieved in one line
wks.cell('B1').set_text_format('bold', True).value = 'heights'

# set the names
wks.update_values('A2:A5',[['name1'],['name2'],['name3'],['name4']])

#print(sh.sheet1.get('A1:D11'))

#worksheet_list = sh.worksheets()

#print(worksheet_list)
