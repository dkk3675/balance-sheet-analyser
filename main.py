import sys
import subprocess
import pkg_resources
from copy import deepcopy

print("------------------------------------------------------------------------")
print("Please have an active internet connection before running this program!!!")
print("------------------------------------------------------------------------")

required = {'requests','colorama','tabulate','matplotlib'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if missing:
    print("\n-----------------------------------------------------------------------------")
    print("Please wait for few minutes while we load the system libraries in your pc ...")
    print("-----------------------------------------------------------------------------")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import requests
from colorama import Fore
from tabulate import tabulate
import matplotlib.pyplot as plt

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

def calc():
    print(Fore.LIGHTBLUE_EX+"\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(color.BOLD+"\t| Company : "+ company + " for Financial Year " + balance_sheet['calendarYear'] + " |" +color.END)
    print(Fore.LIGHTBLUE_EX+"\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(Fore.LIGHTMAGENTA_EX + color.BOLD + "---------------------------")
    print(" # Analysis (in US Dollars)")
    print("---------------------------" + color.END)
    print(Fore.LIGHTGREEN_EX + f" - Total Current Assets : $ {balance_sheet['totalCurrentAssets']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Total Current Liabilities : $ {balance_sheet['totalCurrentLiabilities']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Working Capital : $ {balance_sheet['totalCurrentAssets'] - balance_sheet['totalCurrentLiabilities']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Current Ratio : {balance_sheet['totalCurrentAssets'] / balance_sheet['totalCurrentLiabilities']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Cash and Short Term Investments : $ {balance_sheet['cashAndShortTermInvestments']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Cash Ratio : {balance_sheet['cashAndShortTermInvestments'] / balance_sheet['totalCurrentLiabilities']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Total Debt : $ {balance_sheet['totalDebt']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Total Stockholders Equity : $ {balance_sheet['totalStockholdersEquity']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Debt to Equity : {balance_sheet['totalDebt'] / balance_sheet['totalStockholdersEquity']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Long Term Debt : $ {balance_sheet['totalDebt']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Long Term Debt to Equity : {balance_sheet['longTermDebt'] / balance_sheet['totalStockholdersEquity']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Total Assets : $ {balance_sheet['totalAssets']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Financial Leverage : {balance_sheet['totalAssets'] / balance_sheet['totalStockholdersEquity']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Good will and Intangible Assets : $ {balance_sheet['goodwillAndIntangibleAssets']:,}")
    print(Fore.LIGHTGREEN_EX + f" - Percentage Intangibles : {balance_sheet['goodwillAndIntangibleAssets'] / balance_sheet['totalAssets'] *100 } %")

    print(Fore.LIGHTMAGENTA_EX + "---------------------------\n")

    return [balance_sheet['totalCurrentAssets'],balance_sheet['totalCurrentLiabilities'],balance_sheet['totalCurrentAssets'] - balance_sheet['totalCurrentLiabilities'],balance_sheet['cashAndShortTermInvestments'],balance_sheet['totalDebt'],balance_sheet['totalStockholdersEquity'],balance_sheet['totalDebt'],balance_sheet['totalAssets'],balance_sheet['goodwillAndIntangibleAssets']],[balance_sheet['totalCurrentAssets'] / balance_sheet['totalCurrentLiabilities'],balance_sheet['cashAndShortTermInvestments'] / balance_sheet['totalCurrentLiabilities'],balance_sheet['totalDebt'] / balance_sheet['totalStockholdersEquity'],balance_sheet['longTermDebt'] / balance_sheet['totalStockholdersEquity'],balance_sheet['totalAssets'] / balance_sheet['totalStockholdersEquity'],balance_sheet['goodwillAndIntangibleAssets'] / balance_sheet['totalAssets'] *100]


def tabulate_sheet(x,y,flag):
    balance_sheet = []
    for i in range(0,len(x)-1,1):
        if i < len(y)-1 and flag:
            y[i] += x[i]
            balance_sheet.append(y[i])
        elif i < len(y)-1 and not flag:
            x[i] += y[i]
            balance_sheet.append(x[i])
        else:
            if flag :
                balance_sheet.append(['','',x[i][0],x[i][1]])
            else :
                balance_sheet.append([x[i][0],x[i][1],'',''])
    balance_sheet.append(['','','',''])
    if flag :
        balance_sheet.append(['TOTAL ASSETS',y[len(y)-1][1],'TOTAL LIABILITIES',x[i+1][1]])
    else :
        balance_sheet.append(['TOTAL ASSETS',x[i+1][1],'TOTAL LIABILITIES',y[len(y)-1][1]])
    return balance_sheet

def name():
    print(Fore.LIGHTRED_EX + color.BOLD + "\n\n------------------------------")
    print("Project by : \n 1 - Abhishree - 521\n 2 - Divya Kumar Karan - 561\n 3 - Gautam Raj - 563\n 4 - Tanishque Shukla - 616")
    print("------------------------------"  + color.END)



api_key = 'bf356a576e1da2f93c4f7e92bcbfe278'
n = int(input(Fore.LIGHTCYAN_EX+ color.BOLD +"\nChoose company to analyse : \n\n 1 - Facebook\n 2 - Apple\n 3 - Microsoft\n\n @ Enter your choice : " ))
print("\n---------------------------\n" + color.END)
if n==1 : company = "FB"
elif n==2 : company = "AAPL"
else : company = "MSFT"

years = int(input(Fore.LIGHTCYAN_EX+ color.BOLD +"Choose no. of years to analyse : " ))
print("\n---------------------------\n" + color.END)

try:
    balance_sheet_api = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={api_key}").json()

    plt.figure(f'FINANCIAL HEALTH OF {company}')
    plot1 = plt.subplot2grid((10,1),(0,0),rowspan=4)
    plot2 = plt.subplot2grid((10,1),(6,0),rowspan=4)

    x1 = ['Total\nCurrent\nAssets','Total\nCurrent\nLiabilities','Working\nCapital','Cash and\nShort\nTerm\nInvestments','Total\nDebt','Total\nStockholders\nEquity','Long\nTerm\nDebt','Total\nAssets','Good will\nand\nIntangible\nAssets']

    x2 = ['Current\nRatio','Cash\nRatio','Debt to\nEquity','Long Term\nDebt to Equity','Financial\nLeverage','Percentage\nIntangibles']

    for i in range(0,years,1):
        balance_sheet = balance_sheet_api[i]
    
        y1,y2 = calc()

        plot1.plot(x1,y1,marker = 'o',label = 'FY - ' + balance_sheet['calendarYear'])
        plot2.plot(x2,y2,marker = 'o',label = 'FY - ' + balance_sheet['calendarYear'])

        assets = []
        liabilities = []
        for key,value in balance_sheet.items():
            if type(value) is int or type(value) is float:
                value = int(value)
                value = ('$ {:,}'.format(value))
                liabilities.append([key,value])
                if key == 'totalAssets':
                    assets = deepcopy(liabilities)
                    liabilities.clear()
                if key == 'totalLiabilitiesAndTotalEquity':
                    break

        if len(liabilities) > len(assets):
            balance_sheet = tabulate_sheet(liabilities,assets,1)
        else:
            balance_sheet = tabulate_sheet(assets,liabilities,0)

        print(Fore.LIGHTMAGENTA_EX + "\n--------------------------------")
        print(" # Balance Sheet (in US Dollars)")
        print("--------------------------------")
        print(Fore.LIGHTGREEN_EX + tabulate(balance_sheet,tablefmt='fancy_grid'))
        print(f"\nRef. : https://www.financialmodelingprep.com/balance-sheet-data/{company}\n")
        print(Fore.LIGHTMAGENTA_EX + "--------------------------------\n")

    name()
    plot1.legend()
    plot1.set_title('FINANCIAL TERMS')
    plot1.set_ylabel('VALUE x $100 BILLIONS')

    plot2.legend()
    plot2.set_title('FINANCIAL RATIOS')
    plot2.set_ylabel('RATIO')

    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()
    print(Fore.LIGHTYELLOW_EX +"\n\t -----------")
    print("\t[ Thank You ]")
    print("\t -----------\n")

    
except:
    print(Fore.RED + color.BOLD +"-----------------------------------------------------------------------------------------")
    print("Error you do not have an active connection, please retry after turning on the internet!!!")
    print("-----------------------------------------------------------------------------------------"+ color.END)