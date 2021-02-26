import os
print('''Windows10 System version lifter(版本升降器) 
Version number: 1.0
Compile date: 2021-2-27
Open source address: https://gitee.com/ddos_ling/windows-10-version-lifter
By DDoS_LING
----------------------------------------------------------------------------------------------------
请先阅读并同意以下协议才可开始使用
不同意以上协议请退出
Please read and agree the following agreement before use.
If you don't agree with the above agreement, please exit.

Chinese:
1. 该程序仅允许用于个人学习/研究使用,禁止商用!
2. 因违规使用或使用不当导致的所有后果原作者概不负责!
3. 本软件涉及到的序列号均来源于网络
4. 二次开发请遵循 MIT 开源许可协议
5. 数据无价,重要文件建议备份
6. 请务必以管理员身份运行本程序

English:
1. This program can only be used for personal study / research, commercial use is prohibited!
2. The original author is not responsible for all consequences caused by illegal use or improper use!
3. The serial numbers involved in this software are all from the network.
4. Please follow MIT open source license agreement for secondary development.
5. Data is priceless, backup of important documents is recommended.
6. Be sure to run this program as an administrator.
----------------------------------------------------------------------------------------------------''')
print('''Enter "agree" to agree to the above agreement.
输入"agree"表示同意以上协议: ''')
if(input(">>> ")=="agree"):
    os.system("cls")
    print('''You have agreed to use the agreement.
您已同意使用协议

Be sure to run this program as an administrator
请务必以管理员身份运行本程序
''')
    while True:
        choice=-1
        print('''Windows10 System version lifter(版本升降器) 
Version number: 1.0
Compile date: 2021-2-27
Open source address: https://gitee.com/ddos_ling/windows-10-version-lifter
By DDoS_LING
----------------------------------------------------------------------------------------------------
Please enter the number of the operation you want to perform
请输入你要执行的操作对应的编号

1.查看可升/降级的版本 View upgradeable / downgradeable versions

2.升级到专业版 Upgrade to professional
3.升级到专业教育版 Upgrade to professional education
4.升级到专业工作站版 Upgrade to professional workstation
5.升级到企业版 Upgrade to enterprise version
6.升级到教育版 Upgrade to education
7.升级到家庭版 Upgrade to home version

8.获取激活软件 Get activation software

0.退出 Sign out
        ''')
        choice=input(">>> ")
        if(choice=="0"):
            break
        elif(choice=="1"):
            os.system("dism /online /get-targeteditions")
        elif(choice=="2"):
            os.system("changepk.exe /productkey VK7JG-NPHTM-C97JM-9MPGT-3V66T")
        elif(choice=="3"):
            os.system("changepk.exe /productkey 8PTT6-RNW4C-6V7J2-C2D3X-MHBPB")
        elif(choice=="4"):
            os.system("changepk.exe /productkey DXG7C-N36C4-C4HTG-X4T3X-2YV77")
        elif(choice=="5"):
            os.system("changepk.exe /productkey XGVPP-NMH47-7TTHJ-W3FW7-8HV2C")
        elif(choice=="6"):
            os.system("changepk.exe /productkey YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY")
        elif(choice=="7"):
            os.system("changepk.exe /productkey YTMG3-N6DKC-DKB77-7M9GH-8HVX7")
        elif(choice=="8"):
            print('''
Download address(下载地址):
     url https://stgzs.lanzous.com/b01677a9g
password 7bte

Note(注意): 
The source of the resource is from the network, please check the security of the file by yourself!
资源来源由网络，请自行检测文件安全性！
            ''')
        else:
            print('''
The number you entered is wrong.
您输入的数字有误
            ''')
        print("Command execution complete 命令执行完毕")
        input("Press enter to return.(按回车键返回)")
        os.system("cls")


