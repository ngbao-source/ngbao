import requests
import json
import time
import random
import re
import glob
import os
from pystyle import Colors, Colorate
import sys
from time import sleep

def Ngbao_delay_tool(p):
    while p > 1:
        p -= 1
        print(f'\033[1;31m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][-][..............][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;32m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][+][Đ.............][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;33m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][|][ĐA............][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;34m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][/][ĐAN..........][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;35m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][-][ĐANG........][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;36m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][+][ĐANG K......][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;37m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][\][ĐANG KE....][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;38m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][|][ĐANG KET..][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;37m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][\][ĐANG KET N....][{p}]', '     ', end='\r')
        sleep(1 / 6)
        print(f'\033[1;38m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][|][ĐANG KET NO..][{p}]', '     ', end='\r')
        print(f'\033[1;38m[ 🕊️ VUI LÒNG ĐỢI 🕊️ ][|][ĐANG KET NỐI..][{p}]', '     ', end='\r')
        
        os.system("cls" if os.name == "nt" else "clear")

p = random.randint(3, 3)
Ngbao_delay_tool(p)

class Mention:
    def __init__(self, thread_id, offset, length):
        self.thread_id = thread_id
        self.offset = offset
        self.length = length

    def _to_send_data(self, i):
        return {
            f"profile_xmd[{i}][id]": self.thread_id,
            f"profile_xmd[{i}][offset]": self.offset,
            f"profile_xmd[{i}][length]": self.length,
            f"profile_xmd[{i}][type]": "p",
        }

class NgbaoMessenger:
    def __init__(self, cookie):
        self.cookie = cookie
        self.user_id = self.id_user()
        self.fb_dtsg = None
        self.jazoest = None
        self.init_params()
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        ]

    def id_user(self):
        try:
            c_user = re.search(r"c_user=(\d+)", self.cookie).group(1)
            return c_user
        except:
            raise Exception("Cookie không hợp lệ")

    def init_params(self):
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate', 
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }

        try:
            # Thử lấy từ www.facebook.com
            response = requests.get('https://www.facebook.com', headers=headers, timeout=10)
            fb_dtsg_match = re.search(r'"token":"(.*?)"', response.text)
            jazoest_match = re.search(r'"jazoest":"(.*?)"', response.text)
            
            # Nếu không tìm thấy, thử mbasic.facebook.com
            if not fb_dtsg_match or not jazoest_match:
                response = requests.get('https://mbasic.facebook.com', headers=headers, timeout=10)
                if not fb_dtsg_match:
                    fb_dtsg_match = re.search(r'name="fb_dtsg" value="(.*?)"', response.text)
                if not jazoest_match:
                    jazoest_match = re.search(r'name="jazoest" value="(.*?)"', response.text)
                
                # Nếu vẫn không tìm thấy, thử m.facebook.com
                if not fb_dtsg_match or not jazoest_match:
                    response = requests.get('https://m.facebook.com', headers=headers, timeout=10)
                    if not fb_dtsg_match:
                        fb_dtsg_match = re.search(r'name="fb_dtsg" value="(.*?)"', response.text)
                    if not jazoest_match:
                        jazoest_match = re.search(r'name="jazoest" value="(.*?)"', response.text)

            # Lưu giá trị tìm được
            if fb_dtsg_match:
                self.fb_dtsg = fb_dtsg_match.group(1)
            
            if jazoest_match:
                self.jazoest = jazoest_match.group(1)
            else:
                # Nếu không tìm thấy jazoest, tạo giá trị mặc định
                self.jazoest = '2' + str(sum(ord(c) for c in self.fb_dtsg))
                
            if not self.fb_dtsg:
                raise Exception("Không thể lấy được fb_dtsg")

        except requests.exceptions.Timeout:
            raise Exception("Timeout khi kết nối Facebook")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Lỗi kết nối: {str(e)}")
        except Exception as e:
            raise Exception(f"Lỗi khi khởi tạo tham số: {str(e)}")

    def get_thread_list(self, limit=100):
        """Lấy danh sách box chat"""
        headers = {
            'Cookie': self.cookie,
            'User-Agent': random.choice(self.user_agents),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-FB-Friendly-Name': 'MessengerThreadListQuery',
            'X-FB-LSD': 'null'
        }
        
        form_data = {
            "av": self.user_id,
            "__user": self.user_id,
            "__a": "1",
            "__req": "1b",
            "__hs": "19234.HYP:comet_pkg.2.1..2.1",
            "dpr": "1",
            "__ccg": "EXCELLENT",
            "__rev": "1015919737",
            "__comet_req": "15",
            "fb_dtsg": self.fb_dtsg,
            "jazoest": self.jazoest,
            "lsd": "null",
            "__spin_r": "",
            "__spin_b": "trunk",
            "__spin_t": str(int(time.time())),
            "queries": json.dumps({
                "o0": {
                    "doc_id": "3336396659757871",
                    "query_params": {
                        "limit": limit,
                        "before": None,
                        "tags": ["INBOX"],
                        "includeDeliveryReceipts": False,
                        "includeSeqID": True,
                    }
                }
            })
        }
        
        try:
            response = requests.post(
                'https://www.facebook.com/api/graphqlbatch/',
                data=form_data,
                headers=headers,
                timeout=15
            )
            
            if response.status_code != 200:
                return {"error": f"HTTP Error: {response.status_code}"}
            
            response_text = response.text.split('{"successful_results"')[0]
            data = json.loads(response_text)
            
            if "o0" not in data:
                return {"error": "Không tìm thấy dữ liệu thread list"}
            
            if "errors" in data["o0"]:
                return {"error": f"Facebook API Error: {data['o0']['errors'][0]['summary']}"}
            
            threads = data["o0"]["data"]["viewer"]["message_threads"]["nodes"]
            thread_list = []
            
            for thread in threads:
                if not thread.get("thread_key") or not thread["thread_key"].get("thread_fbid"):
                    continue
                thread_list.append({
                    "thread_id": thread["thread_key"]["thread_fbid"],
                    "thread_name": thread.get("name", "Không có tên")
                })
            
            return {
                "success": True,
                "thread_count": len(thread_list),
                "threads": thread_list
            }
            
        except json.JSONDecodeError as e:
            return {"error": f"Lỗi parse JSON: {str(e)}"}
        except Exception as e:
            return {"error": f"Lỗi không xác định: {str(e)}"}

    def get_group_members(self, thread_id):
        """Lấy danh sách thành viên trong box"""
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'python-http/0.27.0',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Host': 'www.facebook.com',
            'Referer': 'https://www.facebook.com/'
        }
        
        payload = {
            'queries': json.dumps({
                'o0': {
                    'doc_id': '3449967031715030',
                    'query_params': {
                        'id': thread_id,
                        'message_limit': 0,
                        'load_messages': False,
                        'load_read_receipts': False,
                        'before': None
                    }
                }
            }),
            'batch_name': 'MessengerGraphQLThreadFetcher',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest
        }
        
        try:
            response = requests.post('https://www.facebook.com/api/graphqlbatch/', headers=headers, data=payload)
            content = response.text
            if content.startswith('for(;;);'):
                content = content[9:]
            
            json_objects = []
            current_json = ""
            in_quotes = False
            escape_next = False
            brackets = 0
            
            for char in content:
                if escape_next:
                    current_json += char
                    escape_next = False
                    continue
                if char == '\\':
                    current_json += char
                    escape_next = True
                    continue
                if char == '"' and not escape_next:
                    in_quotes = not in_quotes
                if not in_quotes:
                    if char == '{':
                        brackets += 1
                    elif char == '}':
                        brackets -= 1
                        if brackets == 0:
                            current_json += char
                            json_objects.append(current_json)
                            current_json = ""
                            continue
                if brackets > 0:
                    current_json += char
            
            if json_objects:
                data = json.loads(json_objects[0])
                thread_data = data.get("o0", {}).get("data", {}).get("message_thread", {})
                all_participants = thread_data.get("all_participants", {}).get("edges", [])
                members = []
                for participant in all_participants:
                    user = participant.get("node", {}).get("messaging_actor", {})
                    member_id = user.get("id")
                    if member_id and member_id != self.user_id:
                        members.append({
                            "name": user.get("name"),
                            "id": member_id
                        })
                return {"success": True, "members": members}
            else:
                return {"error": "Không tìm thấy dữ liệu thành viên"}
        except Exception as e:
            return {"error": f"Lỗi lấy danh sách thành viên: {str(e)}"}

    def gui_tn(self, recipient_id, message, mention_ids=None, mention_names=None):
        if not message or not recipient_id:
            raise ValueError("ID người nhận và nội dung tin nhắn không được để trống")

        timestamp = int(time.time() * 1000)
        offline_threading_id = str(timestamp)
        message_id = str(timestamp)

        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Host': 'www.facebook.com',
            'Referer': 'https://www.facebook.com/messages/t/' + recipient_id
        }

        # Tạo danh sách tag và mentions
        if mention_ids and mention_names:
            tag_parts = []
            mentions = []
            offset = len(message) + 1  # +1 cho space sau content
            
            for i in range(len(mention_ids)):
                name = mention_names[i]
                tag_text = f"@{name}"
                tag_parts.append(tag_text)
                
                mention = Mention(thread_id=mention_ids[i], offset=offset, length=len(tag_text))
                mentions.append(mention)
                
                # Cộng độ dài tag + 1 space (cho tag tiếp theo)
                offset += len(tag_text) + 1
            
            # Tạo message hoàn chỉnh
            full_message = f"{message} {' '.join(tag_parts)}"
        else:
            full_message = message
            mentions = []

        data = {
            'thread_fbid': recipient_id,
            'action_type': 'ma-type:user-generated-message',
            'body': full_message,
            'client': 'mercury',
            'author': f'fbid:{self.user_id}',
            'timestamp': timestamp,
            'source': 'source:chat:web',
            'offline_threading_id': offline_threading_id,
            'message_id': message_id,
            'ephemeral_ttl_mode': '0',
            '__user': self.user_id,
            '__a': '1',
            '__req': '1b', 
            '__rev': '1015919737',
            'fb_dtsg': self.fb_dtsg,
            'source_tags[0]': 'source:chat'
        }

        # Thêm mentions vào payload
        for idx, mention in enumerate(mentions):
            data.update(mention._to_send_data(idx))

        try:
            response = requests.post(
                'https://www.facebook.com/messaging/send/',
                data=data,
                headers=headers,
                timeout=10
            )
            if response.status_code != 200:
                return {
                    'success': False,
                    'error': 'HTTP_ERROR',
                    'error_description': f'Status code: {response.status_code}'
                }

            if 'for (;;);' in response.text:
                clean_text = response.text.replace('for (;;);', '')
                try:
                    result = json.loads(clean_text)
                    
                    if 'error' in result:
                        return {
                            'success': False,
                            'error': result.get('error'),
                            'error_description': result.get('errorDescription', 'Unknown error')
                        }
                        
                    return {
                        'success': True,
                        'message_id': message_id,
                        'timestamp': timestamp
                    }
                except json.JSONDecodeError:
                    pass 
            
            return {
                'success': True,
                'message_id': message_id,
                'timestamp': timestamp
            }
                
        except Exception as e:
            return {
                'success': False,
                'error': 'REQUEST_ERROR',
                'error_description': str(e)
            }


if __name__ == "__main__":
    banner = """
\033[1;32m░██████╗░██╗░█████╗░  ██████╗░░█████╗░░█████╗░
\033[1;34m██╔════╝░██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗
\033[1;36m██║░░██╗░██║███████║  ██████╦╝███████║██║░░██║
\033[1;35m██║░░╚██╗██║██╔══██║  ██╔══██╗██╔══██║██║░░██║
\033[1;31m╚██████╔╝██║██║░░██║  ██████╦╝██║░░██║╚█████╔╝
\033[1;33m░╚═════╝░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░
\033[1;37m 
\033[1;30m\033[3m  Facebook:Ngbao - Zalo:0988467271                                   

    """
    
    print(banner)
    
    try:
        # Chọn cách nhập cookie
        print("\033[38;5;87m╔════════════════════════════════════════╗")
        print("║     CHỌN CÁCH NHẬP COOKIE FACEBOOK     ║")
        print("╚════════════════════════════════════════╝\033[0m")
        print("\033[38;5;226m[1] Nhập cookie thủ công")
        print("[2] Đọc từ file cookies.txt\033[0m")
        print("─" * 60)
        
        choice = input(f"\033[38;5;87m[+] Chọn (1/2): \033[0m").strip()
        
        cookies = []
        if choice == '1':
            num_accounts = int(input(f"\033[38;5;87m[+] Nhập số lượng tài khoản muốn chạy: \033[0m").strip())
            
            if num_accounts <= 0:
                raise Exception("\033[38;5;196m[!] Số lượng tài khoản phải lớn hơn 0\033[0m")
            
            print(f"\n\033[38;5;226m[*] Nhập {num_accounts} cookie Facebook:\033[0m")
            for i in range(1, num_accounts + 1):
                cookie = input(f"\033[38;5;87m[Cookie {i}]: \033[0m").strip()
                if cookie:
                    cookies.append(cookie)
                    print(f"\033[38;5;82m[✓] Đã thêm cookie {i}\033[0m")
                else:
                    print(f"\033[38;5;196m[!] Cookie {i} trống, bỏ qua\033[0m")
            
            if not cookies:
                raise Exception("\033[38;5;196m[!] Chưa nhập cookie nào hợp lệ\033[0m")
            
            # Lưu cookie vào file để dùng sau
            with open('cookies.txt', 'w', encoding='utf-8') as f:
                for cookie in cookies:
                    f.write(cookie + '\n')
            print(f"\033[38;5;82m[✓] Đã lưu {len(cookies)} cookie vào cookies.txt\033[0m")
            
        elif choice == '2':
            try:
                with open('cookies.txt', 'r', encoding='utf-8') as f:
                    cookies = [line.strip() for line in f if line.strip()]
                if not cookies:
                    raise Exception("File cookies.txt trống")
                print(f"\033[38;5;82m[✓] Đã tải {len(cookies)} cookie từ file\033[0m")
            except FileNotFoundError:
                raise Exception("\033[38;5;196m[!] Không tìm thấy file cookies.txt\033[0m")
        else:
            raise Exception("\033[38;5;196m[!] Lựa chọn không hợp lệ\033[0m")

        messengers = []
        for i, cookie in enumerate(cookies, 1):
            try:
                messenger = NgbaoMessenger(cookie)
                messengers.append(messenger)
                print(f"\033[38;5;82m[✓] Cookie {i}: Đã lấy được user_id: {messenger.user_id}\033[0m")
            except Exception as e:
                print(f"\033[38;5;196m[×] Cookie {i}: Không hợp lệ - {str(e)}\033[0m")
        
        if not messengers:
            raise Exception("\033[38;5;196m[!] Không có cookie nào hợp lệ\033[0m")
            
        # Sử dụng cookie đầu tiên để lấy danh sách box
        main_messenger = messengers[0]
        
        print("\n" + "─" * 60)
        print("\033[38;5;226m[*] Đang lấy danh sách box chat...\033[0m")
        result = main_messenger.get_thread_list(limit=100)
        
        if "error" in result:
            print(f"\033[38;5;196m[!] Lỗi: {result['error']}\033[0m")
            print("\033[38;5;196m[!] Không thể lấy danh sách box, nhập thủ công\033[0m")
            recipient_id = input(f"\033[38;5;87m[+] Nhập ID box: \033[0m")
            tag_mode = "none"
            mention_ids = None
            mention_names = None
        else:
            threads = result['threads']
            if not threads:
                print("\033[38;5;196m[!] Không tìm thấy box nào\033[0m")
                recipient_id = input(f"\033[38;5;87m[+] Nhập ID box: \033[0m")
                tag_all = False
            else:
                print(f"\n\033[38;5;82m[✓] Tìm thấy {len(threads)} box:\033[0m")
                print("=" * 60)
                for idx, thread in enumerate(threads, 1):
                    thread_name = thread.get('thread_name', 'Không có tên') or 'Không có tên'
                    display_name = f"{thread_name[:45]}{'...' if len(thread_name) > 45 else ''}"
                    print(f"\033[38;5;87m{idx}. {display_name}")
                    print(f"   ID: {thread['thread_id']}\033[0m")
                    print("-" * 55)
                
                box_choice = input(f"\n\033[38;5;87m[+] Chọn số thứ tự box (hoặc nhập ID trực tiếp): \033[0m")
                
                try:
                    box_index = int(box_choice) - 1
                    if 0 <= box_index < len(threads):
                        recipient_id = threads[box_index]['thread_id']
                        print(f"\033[38;5;82m[✓] Đã chọn box: {threads[box_index]['thread_name']}\033[0m")
                    else:
                        recipient_id = box_choice
                except ValueError:
                    recipient_id = box_choice
                
                # Menu chọn chế độ tag
                print("\n\033[38;5;87m╔════════════════════════════════════════╗")
                print("║         CHỌN CHỾ ĐỘ TAG MENTION       ║")
                print("╚════════════════════════════════════════╝\033[0m")
                print("\033[38;5;226m[1] Tag @everyone (tất cả mọi người)")
                print("[2] Tag người cụ thể (chọn từ danh sách)")
                print("[3] Không tag ai cả\033[0m")
                print("─" * 60)
                
                tag_choice = input(f"\033[38;5;87m[+] Chọn (1/2/3): \033[0m").strip()
                
                mention_ids = None
                mention_names = None
                tag_mode = "none"
                
                if tag_choice == '1':
                    # Tag @everyone
                    print("\033[38;5;226m[*] Đang lấy danh sách thành viên...\033[0m")
                    members_result = main_messenger.get_group_members(recipient_id)
                    if members_result.get("success"):
                        members = members_result["members"]
                        if members:
                            mention_ids = [m['id'] for m in members]
                            mention_names = [m['name'] for m in members]
                            tag_mode = "everyone"
                            print(f"\033[38;5;82m[✓] Sẽ tag {len(members)} thành viên (@everyone)\033[0m")
                        else:
                            print("\033[38;5;196m[!] Không tìm thấy thành viên nào\033[0m")
                    else:
                        print(f"\033[38;5;196m[!] Lỗi: {members_result['error']}\033[0m")
                
                elif tag_choice == '2':
                    # Tag người cụ thể
                    print("\033[38;5;226m[*] Đang lấy danh sách thành viên...\033[0m")
                    members_result = main_messenger.get_group_members(recipient_id)
                    if members_result.get("success"):
                        members = members_result["members"]
                        if members:
                            print(f"\n\033[38;5;82m[✓] Tìm thấy {len(members)} thành viên:\033[0m")
                            print("=" * 60)
                            for idx, member in enumerate(members, 1):
                                print(f"\033[38;5;87m{idx}. {member['name']} (ID: {member['id']})\033[0m")
                                print("-" * 55)
                            
                            raw_tags = input(f"\n\033[38;5;87m[+] Nhập số thứ tự người muốn tag (VD: 1,2,3): \033[0m")
                            try:
                                selected_nums = [int(i.strip()) for i in raw_tags.split(',')]
                                selected_members = [members[i-1] for i in selected_nums if 1 <= i <= len(members)]
                                
                                if selected_members:
                                    mention_ids = [m['id'] for m in selected_members]
                                    mention_names = [m['name'] for m in selected_members]
                                    tag_mode = "specific"
                                    print(f"\033[38;5;82m[✓] Sẽ tag {len(selected_members)} người đã chọn\033[0m")
                                else:
                                    print("\033[38;5;196m[!] Không chọn người nào hợp lệ\033[0m")
                            except:
                                print("\033[38;5;196m[!] Định dạng không hợp lệ\033[0m")
                        else:
                            print("\033[38;5;196m[!] Không tìm thấy thành viên nào\033[0m")
                    else:
                        print(f"\033[38;5;196m[!] Lỗi: {members_result['error']}\033[0m")
                
                else:
                    tag_mode = "none"
                    print("\033[38;5;226m[✓] Không tag ai cả\033[0m")
        
        delay = float(input(f"\033[38;5;87m[+] Nhập delay (giây): \033[0m"))
        print("─" * 60 + "\n")
        
        print("\033[38;5;226m[Nguyen hoang gia bao] Bắt đầu gửi tin nhắn...\033[0m")
        
        while True:
            nanh_files = sorted(glob.glob("Ngbaox2008*.txt"))
            
            if not nanh_files:
                print("\033[38;5;196m[!] Không tìm thấy file Ngbaox2008 nào!\033[0m")
                break
            else:
                for file_path in nanh_files:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            message = f.read().strip()
                            
                        if message: 
                            for i, messenger in enumerate(messengers, 1):
                                result = messenger.gui_tn(
                                    recipient_id, 
                                    message,
                                    mention_ids if tag_mode != "none" else None,
                                    mention_names if tag_mode != "none" else None
                                )
                                if result['success']:
                                    if tag_mode == "everyone":
                                        tag_info = " (@everyone)"
                                    elif tag_mode == "specific":
                                        tag_info = f" (tag {len(mention_ids)} người)"
                                    else:
                                        tag_info = ""
                                    print(f"\033[38;5;82m[✓] Cookie {i}: Gửi thành công{tag_info} nội dung từ {file_path}\033[0m")
                                else:
                                    print(f"\033[38;5;196m[×] Cookie {i}: Lỗi khi gửi nội dung từ {file_path}: {result['error_description']}\033[0m")
                            
                            sys.stdout.write("\033[38;5;226m[*] Đang chờ ")
                            for i in range(int(delay)):
                                sys.stdout.write("⌛")
                                sys.stdout.flush()
                                sleep(1)
                            sys.stdout.write("\033[0m\n")
                            
                    except Exception as e:
                        print(f"\033[38;5;196m[!] Lỗi khi đọc hoặc gửi file {file_path}: {str(e)}\033[0m")
                        
    except Exception as e:
        print(f"\033[38;5;196m[!] Lỗi: {str(e)}\033[0m")