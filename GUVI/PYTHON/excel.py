import xlrd

loc = "new.xlsx"

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

# Please refer the video

