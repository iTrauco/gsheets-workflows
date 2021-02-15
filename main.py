#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gspread
import pygsheets

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
sh  = gc.open_by_key("13MDkXxt9pSbPWtqJK0DXHH81kTCjg2Y_1RJa7mgALCQ")

# Select worksheet by index. Worksheet indexes start from zero:
wks = sh.get_worksheet(2)

# Creating a Worksheet
# worksheet = sh.add_worksheet(title="data", rows="1000", cols="52")

print(sh.sheet1.get('A1:D11'))

worksheet_list = sh.worksheets()

print(worksheet_list)
print(wks)
