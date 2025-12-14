import multiprocessing
import requests
import os
import re
import json
import time
import random

# ✅ MÀU SẮC
class Colors:
    RESET = '\033[0m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    GRAY = '\033[1;30m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_main_banner():
    banner = f"""
{Colors.CYAN}⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⡿⣯⡷⡴⢦⣤⡠⣶⡶⠀⢷⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⡾⠀
⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⣼⣥⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⠀⠈⢧⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⡇⠀
⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⠛⢦⠀⠀⢸⡇⠀⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⠳⠀⢳⡀⢹⡇⠀⠀⠀⠀⠀⡾⡇⠀
⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⠘⠀⠀⠹⣼⡇⠀⠀⠀⠀⢠⠇⠀⠀
⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⡾⠀⠀⠀
⠀⠀⢠⡏⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⢸⠁⠀⠀⠀
⠀⠀⡾⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⡟⠀⠀⠀⠀
⠀⣴⠓⣾⣳⣀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⢸⡇⢀⠇⠀⠀⠀⠀
⣾⠃⠀⠀⠀⠑⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠈⡇⢸⠀⠀⠀⠀⠀
⠹⡀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣾⠀⠀⠀⠀⠀
⠀⢳⡄⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⣿⠀⠀⠀⠀⠀
⠀⠀⣷⡄⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⡏⠀⠀⠀⠀⠀
⠀⢀⡇⢹⣄⠀⠀⠀⠀⣀⠉⠓⠶⢄⡀⠀⠀⠀⠀⠀⢀⣠⠴⠋⠣⣄⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⣸⣧⠀⠀⠀⠀⠀
⠀⣴⣿⠋⠘⣆⠀⢰⠶⠤⢍⣛⣶⠤⠿⣷⣦⡀⠒⠚⡟⠀⠀⠀⠀⠈⠛⠢⠤⡄⠀⠀⢀⡴⢯⠴⣳⠇⠀⠀⠀⠀⠀
⠀⠀⠉⠀⠀⠘⢦⡈⠻⣖⠤⣤⣉⣉⣹⣯⣭⠉⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠛⣫⣼⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠑⣄⠉⢦⡀⠀⠀⠈⠉⠁⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢿⣷⢚⡝⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢶⣷⠇⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠷⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀{Colors.RESET}
    """
    return banner

def check_live(cookie):
    try:
        if 'c_user=' not in cookie:
            return {"status": "failed", "msg": "Cookie không chứa user_id"}
        
        user_id = cookie.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'vi-VN,vi;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        profile_response = requests.get(f'https://m.facebook.com/profile.php?id={user_id}', headers=headers, timeout=30)
        name = profile_response.text.split('<title>')[1].split('<')[0].strip()
        return {
            "status": "success",
            "name": name,
            "user_id": user_id,
            "msg": "successful"
        }
    except Exception as e:
        return {"status": "failed", "msg": f"Lỗi xảy ra: {str(e)}"}

def load_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        if not lines:
            raise Exception(f"File {file_path} trống!")
        return lines
    except Exception as e:
        raise Exception(f"Lỗi đọc file {file_path}: {str(e)}")

def parse_selection(input_str, max_index):
    try:
        numbers = [int(i.strip()) for i in input_str.split(',')]
        return [n for n in numbers if 1 <= n <= max_index]
    except:
        print("Định dạng không hợp lệ!")
        return []

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

class Messenger:
    def __init__(self, cookie):
        self.cookie = cookie
        self.user_id = self.get_user_id()
        self.fb_dtsg = None
        self.jazoest = None
        self.init_params()
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        ]

    def get_user_id(self):
        try:
            return re.search(r"c_user=(\d+)", self.cookie).group(1)
        except:
            raise Exception("Cookie không hợp lệ")

    def init_params(self):
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0'
        }
        try:
            for url in ['https://www.facebook.com', 'https://mbasic.facebook.com', 'https://m.facebook.com']:
                response = requests.get(url, headers=headers)
                match_dtsg = re.search(r'name="fb_dtsg" value="(.*?)"', response.text)
                match_jazoest = re.search(r'name="jazoest" value="(.*?)"', response.text)
                if match_dtsg:
                    self.fb_dtsg = match_dtsg.group(1)
                if match_jazoest:
                    self.jazoest = match_jazoest.group(1)
                if match_dtsg and match_jazoest:
                    return
            raise Exception("Không tìm thấy fb_dtsg hoặc jazoest")
        except Exception as e:
            raise Exception(f"Lỗi khởi tạo: {str(e)}")

    def get_thread_list(self, limit=100):
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
                    members.append({
                        "name": user.get("name"),
                        "id": user.get("id")
                    })
                return {"success": True, "members": members}
            else:
                return {"error": "Không tìm thấy dữ liệu thành viên"}
        except Exception as e:
            return {"error": f"Lỗi lấy danh sách thành viên: {str(e)}"}

    def send_message(self, recipient_id, content, list_tag, list_name_tag):
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Cookie': self.cookie,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Referer': f'https://www.facebook.com/messages/t/{recipient_id}'
        }
        
        # Tạo danh sách tag và mentions
        tag_parts = []
        mentions = []
        offset = len(content) + 1  # +1 cho space sau content
        
        for i in range(len(list_tag)):
            name = list_name_tag[i]
            tag_text = f"@{name}"
            tag_parts.append(tag_text)
            
            mention = Mention(thread_id=list_tag[i], offset=offset, length=len(tag_text))
            mentions.append(mention)
            
            # Cộng độ dài tag + 1 space (cho tag tiếp theo)
            offset += len(tag_text) + 1
        
        # Tạo message hoàn chỉnh
        full_message = f"{content} {' '.join(tag_parts)}"
        ts = str(int(time.time() * 1000))
        
        payload = {
            "thread_fbid": recipient_id,
            "action_type": "ma-type:user-generated-message",
            "body": full_message,
            "client": "mercury",
            "author": f"fbid:{self.user_id}",
            "timestamp": ts,
            "offline_threading_id": ts,
            "message_id": ts,
            "source": "source:chat:web",
            "ephemeral_ttl_mode": "0",
            "__user": self.user_id,
            "__a": '1',
            "__req": '1b',
            "__rev": '1015919737',
            "fb_dtsg": self.fb_dtsg,
            "source_tags[0]": "source:chat"
        }
        
        # Thêm mentions vào payload
        for idx, mention in enumerate(mentions):
            payload.update(mention._to_send_data(idx))
        
        try:
            response = requests.post("https://www.facebook.com/messaging/send/", headers=headers, data=payload, timeout=10)
            return "success" if response.status_code == 200 else "failed"
        except:
            return "failed"

def start_spam(cookie, account_name, user_id, thread_ids, thread_names, delay, message_lines, replace_text, tag_ids, tag_names):
    """✅ FIX: Gửi CẢ nội dung VÀ tag"""
    try:
        messenger = Messenger(cookie)
        message_index = 0
        success_count = 0
        fail_count = 0
        
        while True:
            for thread_id, thread_name in zip(thread_ids, thread_names):
                # ✅ LẤY NỘI DUNG TỪ FILE
                content = message_lines[message_index]
                
                # Replace {name} nếu có
                if "{name}" in content and replace_text:
                    content = content.replace("{name}", replace_text)
                
                # ✅ GỬI CẢ NỘI DUNG + TAG
                status = messenger.send_message(thread_id, content, tag_ids, tag_names)
                
                if status == "success":
                    success_count += 1
                    # Log với màu xanh
                    tag_info = f" (tag {len(tag_ids)} người)" if tag_ids else ""
                    print(f"{Colors.GREEN}✓ [{account_name}] → {thread_name}{tag_info}: Thành Công{Colors.RESET}")
                else:
                    fail_count += 1
                    # Log với màu đỏ
                    print(f"{Colors.RED}✗ [{account_name}] → {thread_name}: Thất Bại{Colors.RESET}")
                
                # Hiển thị stats mỗi 10 tin
                if (success_count + fail_count) % 10 == 0:
                    total = success_count + fail_count
                    rate = (success_count / total * 100) if total > 0 else 0
                    print(f"{Colors.YELLOW}📊 [{account_name}] Stats: {success_count}/{total} ({rate:.1f}%){Colors.RESET}")
                
                message_index = (message_index + 1) % len(message_lines)
                time.sleep(delay)
                
    except Exception as e:
        print(f"{Colors.RED}⚠️ Lỗi tài khoản {account_name}: {str(e)}{Colors.RESET}")

def start_multiple_accounts():
    clear()
    print(create_main_banner())
    print("="*60)
    print("        Facebook Messenger Auto Sender v2.0")
    print("="*60)
    
    # ✅ THÊM MENU CHỌN CHỂ ĐỘ
    print("\n╔════════════════════════════════════════╗")
    print("║          CHỌN CHẾ ĐỘ HOẠT ĐỘNG        ║")
    print("╚════════════════════════════════════════╝")
    print("[1] TREO - Tag @everyone (tất cả mọi người)")
    print("[2] REO - Tag người cụ thể (chọn từ danh sách)")
    print("=" * 60)
    
    mode_choice = input("\n🔸 Chọn chế độ (1/2): ").strip()
    mode = "treo" if mode_choice == "1" else "reo"
    
    try:
        num_accounts = int(input("\n💠 Nhập số lượng acc muốn chạy: "))
        if num_accounts < 1:
            print("Số lượng tài khoản phải lớn hơn 0. Thoát chương trình.")
            return
    except ValueError:
        print("Số lượng tài khoản phải là số nguyên. Thoát chương trình.")
        return

    processes = []
    for i in range(num_accounts):
        print(f"\n{'='*60}")
        print(f"Nhập thông tin cho tài khoản {i+1}")
        print(f"{'='*60}")
        
        cookie = input("🍪 Nhập Cookie: ").strip()
        if not cookie:
            print("Cookie không được để trống. Bỏ qua tài khoản này.")
            continue
        
        cl = check_live(cookie)
        if cl["status"] == "success":
            print(f"Facebook: {cl['name']} (ID: {cl['user_id']}) - Cookie Sống!")
        else:
            print(f"Lỗi: {cl['msg']}. Bỏ qua tài khoản này.")
            continue

        try:
            messenger = Messenger(cookie)
            print(f"\nĐang lấy danh sách box cho tài khoản {cl['name']}...")
            result = messenger.get_thread_list(limit=100)
            
            if "error" in result:
                print(f"Lỗi: {result['error']}. Bỏ qua tài khoản này.")
                continue
            
            threads_list = result['threads']
            if not threads_list:
                print("Không tìm thấy box nào. Bỏ qua tài khoản này.")
                continue
            
            print(f"\nTìm thấy {len(threads_list)} box:")
            print("=" * 60)
            for idx, thread in enumerate(threads_list, 1):
                thread_name = thread.get('thread_name', 'Không có tên') or 'Không có tên'
                display_name = f"{thread_name[:45]}{'...' if len(thread_name) > 45 else ''}"
                print(f"{idx}. {display_name}")
                print(f"   ID: {thread['thread_id']}")
                print("-" * 55)
            
            raw = input("\n🔸 Nhập số thứ tự box muốn chạy (VD: 1,3): ")
            selected = parse_selection(raw, len(threads_list))
            if not selected:
                print("Không chọn box nào! Bỏ qua tài khoản này.")
                continue
            
            selected_ids = [threads_list[i - 1]['thread_id'] for i in selected]
            selected_names = [threads_list[i - 1]['thread_name'] or 'Không có tên' for i in selected]
            
            # ✅ LẤY DANH SÁCH MEMBERS
            print(f"\nĐang lấy danh sách thành viên cho box...")
            all_members = []
            for thread_id in selected_ids:
                result = messenger.get_group_members(thread_id)
                if result.get("success"):
                    all_members.extend(result["members"])
                else:
                    print(f"Lỗi lấy thành viên: {result['error']}")
            
            if not all_members:
                print("Không tìm thấy thành viên nào. Bỏ qua tài khoản này.")
                continue
            
            # ✅ Loại bỏ duplicate
            unique_members = []
            seen_ids = set()
            for member in all_members:
                if member['id'] not in seen_ids and member['id']:
                    unique_members.append(member)
                    seen_ids.add(member['id'])
            
            tag_ids = []
            tag_names = []
            
            # ✅ XỬ LÝ THEO CHẾ ĐỘ
            if mode == "treo":
                # CHẾ ĐỘ TREO - Tự động tag tất cả
                tag_ids = [m['id'] for m in unique_members]
                tag_names = [m['name'] for m in unique_members]
                print(f"\n✓ Chế độ TREO: Sẽ tag @everyone ({len(tag_ids)} người)")
                
            else:
                # CHẾ ĐỘ REO - Cho chọn người cụ thể
                print(f"\nTìm thấy {len(unique_members)} thành viên:")
                print("=" * 60)
                for idx, member in enumerate(unique_members, 1):
                    print(f"{idx}. {member['name']} (ID: {member['id']})")
                    print("-" * 55)
                
                raw_tags = input("\n🔸 Nhập số thứ tự người muốn réo (VD: 1,2,3) hoặc 'khong' để bỏ qua: ")
                
                if raw_tags.lower() != 'khong':
                    selected_tags = parse_selection(raw_tags, len(unique_members))
                    if not selected_tags:
                        print("Không chọn thành viên nào để tag! Bỏ qua tài khoản này.")
                        continue
                    tag_ids = [unique_members[i - 1]['id'] for i in selected_tags]
                    tag_names = [unique_members[i - 1]['name'] for i in selected_tags]
                    print(f"✓ Sẽ tag {len(tag_ids)} người")
                else:
                    print("✓ Không tag ai")
            
            file_txt = input("\n📂 Nhập tên file .txt chứa nội dung: ").strip()
            try:
                message_lines = load_file(file_txt)
                print(f"Đã tải {len(message_lines)} dòng nội dung từ {file_txt}")
            except Exception as e:
                print(f"Lỗi: {str(e)}. Bỏ qua tài khoản này.")
                continue
            
            replace_text = input("\n✏️ Nhập nội dung thay thế cho {name} (nhấn Enter nếu không thay thế): ").strip()
            
            try:
                delay = int(input("\n⏳ Nhập delay giữa các lần gửi (giây): "))
                if delay < 1:
                    print("Delay phải là số nguyên dương. Bỏ qua tài khoản này.")
                    continue
            except ValueError:
                print("Delay phải là số nguyên. Bỏ qua tài khoản này.")
                continue
            
            mode_text = "TREO (@everyone)" if mode == "treo" else "REO (Custom)"
            print(f"\nKhởi động bot {mode_text} cho acc {cl['name']}...\n")
            
            p = multiprocessing.Process(
                target=start_spam,
                args=(cookie, cl['name'], cl['user_id'], selected_ids, selected_names, delay, message_lines, replace_text, tag_ids, tag_names)
            )
            processes.append(p)
            p.start()
        
        except Exception as e:
            print(f"Lỗi tài khoản {cl.get('name', 'Unknown')}: {str(e)}. Bỏ qua tài khoản này.")
            continue
    
    if not processes:
        print("\nKhông có tài khoản nào được khởi động. Thoát chương trình.")
        return
    
    mode_text = "TREO (@everyone)" if mode == "treo" else "REO (Custom)"
    print("\n" + "="*60)
    print(f"TẤT CẢ BOT ĐÃ KHỞI ĐỘNG THÀNH CÔNG - Chế độ: {mode_text}")
    print("="*60)
    print("Nhấn Ctrl+C để dừng.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Đã dừng tool. Chào tạm biệt!")
        for p in processes:
            p.terminate()
        os._exit(0)

if __name__ == "__main__":
    start_multiple_accounts()