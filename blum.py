import requests
from requests.structures import CaseInsensitiveDict
import time
import datetime
from colorama import init, Fore, Style
init(autoreset=True)
# Fungsi untuk mendapatkan informasi pengguna
def get_user_info(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get('https://gateway.blum.codes/v1/user/me', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        hasil = response.json()
        if hasil['message'] == 'Token is invalid':
            print(f"{Fore.RED+Style.BRIGHT}Token salah")
            return None
        else:
            print(f"{Fore.RED+Style.BRIGHT}Gagal mendapatkan informasi user")
            return None

# Fungsi untuk mendapatkan saldo
def get_balance(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get('https://game-domain.blum.codes/api/v1/user/balance', headers=headers)
    return response.json()

# Fungsi untuk memainkan game
def play_game(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/game/play', headers=headers)
    return response.json()


# Fungsi untuk mengklaim hadiah game
def claim_game(token, game_id, points):
    url = "https://game-domain.blum.codes/api/v1/game/claim"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["authorization"] = "Bearer "+token
    headers["content-type"] = "application/json"
    headers["origin"] = "https://telegram.blum.codes"

    headers["priority"] = "u=1, i"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    data = '{"gameId":"'+game_id+'","points":'+str(points)+'}'

    resp = requests.post(url, headers=headers, data=data)
    return resp  # Kembalikan objek respons, bukan teksnya



def claim_balance(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/farming/claim', headers=headers)
    return response.json()

# Fungsi untuk memulai farming
def start_farming(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/farming/start', headers=headers)
    return response.json()

def refresh_token(old_refresh_token):
    url = 'https://gateway.blum.codes/v1/auth/refresh'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'origin': 'https://telegram.blum.codes',
        'referer': 'https://telegram.blum.codes/'
    }
    data = {
        'refresh': old_refresh_token
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{Fore.RED+Style.BRIGHT}Gagal refresh token untuk: {old_refresh_token}")
        return None  # atau kembalikan respons untuk penanganan lebih lanjut
# Membaca semua token dan menyimpannya dalam list
with open('token.txt', 'r') as file:
    tokens = file.read().splitlines()

# Fungsi untuk memeriksa saldo teman
def check_balance_friend(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get('https://gateway.blum.codes/v1/friends/balance', headers=headers)
    balance_info = response.json()
    return balance_info

# Fungsi untuk mengklaim saldo teman


def claim_balance_friend(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://gateway.blum.codes/v1/friends/claim', headers=headers)
    return response.json()

# cek daily 

def check_daily_reward(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/daily-reward?offset=-420', headers=headers)
    try:
        return response.json()
    except ValueError:  # Menangkap kesalahan jika json tidak dapat diurai
        print(f"{Fore.RED+Style.BRIGHT}Gagal claim daily")
        return None

while True:
    for token in tokens:
        user_info = get_user_info(token)
        if user_info is None:
            continue
        print(f"{Fore.BLUE+Style.BRIGHT}\n==================[{Fore.WHITE+Style.BRIGHT}{user_info['username']}{Fore.BLUE+Style.BRIGHT}]==================")  
        print(f"\r{Fore.YELLOW+Style.BRIGHT}Getting Info....", end="", flush=True)



        balance_info = get_balance(token)
        print(f"\r{Fore.YELLOW+Style.BRIGHT}[Balance]: {balance_info['availableBalance']}", flush=True)
        print(f"{Fore.RED+Style.BRIGHT}[Tiket Game]: {balance_info['playPasses']}")

        # Periksa apakah 'farming' ada dalam balance_info sebelum mengaksesnya
        farming_info = balance_info.get('farming')
        if farming_info:
            end_time_ms = farming_info['endTime']
            end_time_s = end_time_ms / 1000.0
            end_utc_date_time = datetime.datetime.fromtimestamp(end_time_s, datetime.timezone.utc)
            current_utc_time = datetime.datetime.now(datetime.timezone.utc)
            time_difference = end_utc_date_time - current_utc_time
            hours_remaining = int(time_difference.total_seconds() // 3600)
            minutes_remaining = int((time_difference.total_seconds() % 3600) // 60)
            print(f"Waktu Claim: {hours_remaining} jam {minutes_remaining} menit | Balance: {farming_info['balance']}")
        else:
            print(f"{Fore.RED+Style.BRIGHT}Informasi farming tidak tersedia")
        # cek daily 
        print(f"\r{Fore.YELLOW+Style.BRIGHT}Checking daily reward...", end="", flush=True)
        daily_reward_response = check_daily_reward(token)

        if daily_reward_response is None:
            print(f"\r{Fore.RED+Style.BRIGHT}Gagal cek hadiah harian, mencoba lagi...", flush=True)
        else:
            if daily_reward_response['message'] == 'same day':
                print(f"\r{Fore.RED+Style.BRIGHT}Hadiah harian sudah diklaim hari ini", flush=True)
            elif daily_reward_response['message'] == 'OK':
                print(f"\r{Fore.GREEN+Style.BRIGHT}Hadiah harian berhasil diklaim!", flush=True)
        # print(daily_reward_response)
    
        if hours_remaining < 0:
            print(f"\r{Fore.GREEN+Style.BRIGHT}Claiming balance...", end="", flush=True)
            claim_response = claim_balance(token)
            if claim_response:
                print(f"\r{Fore.GREEN+Style.BRIGHT}Claimed: {claim_response['availableBalance']}                ", flush=True)
                print(f"\r{Fore.GREEN+Style.BRIGHT}Starting farming...", end="", flush=True)
                start_response = start_farming(token)
                if start_response:
                    print(f"\r{Fore.GREEN+Style.BRIGHT}Farming started.", flush=True)
                else:
                    print(f"\r{Fore.RED+Style.BRIGHT}Gagal start farming", start_response.status_code, flush=True)
            else:
                print(f"\r{Fore.RED+Style.BRIGHT}Gagal claim", claim_response.status_code, flush=True)

        print(f"\r{Fore.YELLOW+Style.BRIGHT}Checking reff balance...", end="", flush=True)
        friend_balance = check_balance_friend(token)

        if friend_balance:
            if friend_balance['canClaim']:
                print(f"{Fore.GREEN+Style.BRIGHT}Reff Balance: {friend_balance['amountForClaim']}", flush=True)
                print(f"\r{Fore.GREEN+Style.BRIGHT}Claiming Ref balance.....", flush=True)
                claim_friend_balance = claim_balance_friend(token)
                if claim_friend_balance:
                    claimed_amount = claim_friend_balance['claimBalance']
                    print(f"{Fore.GREEN+Style.BRIGHT}Sukses claim total: {claimed_amount}", flush=True)
                else:
                    print(f"{Fore.RED+Style.BRIGHT}Gagal mengklaim saldo ref", flush=True)
            else:
                # Periksa apakah 'canClaimAt' ada sebelum mengaksesnya
                can_claim_at = friend_balance.get('canClaimAt')
                if can_claim_at:
                    claim_time = datetime.datetime.fromtimestamp(int(can_claim_at) / 1000)
                    current_time = datetime.datetime.now()
                    time_diff = claim_time - current_time
                    hours, remainder = divmod(int(time_diff.total_seconds()), 3600)
                    minutes, seconds = divmod(remainder, 60)
                    print(f"{Fore.RED+Style.BRIGHT}\rReff Balance: Klaim pada {hours} jam {minutes} menit lagi", flush=True)
                else:
                    print(f"{Fore.RED+Style.BRIGHT}\rReff Balance: Akun ga punya reff", flush=True)
        else:
            print(f"{Fore.RED+Style.BRIGHT}\rGagal cek reff balance", flush=True)





        while balance_info['playPasses'] > 0:
            print(f"{Fore.CYAN+Style.BRIGHT}Playing game...")
            game_response = play_game(token)
            print(f"\r{Fore.CYAN+Style.BRIGHT}Checking game...", end="", flush=True)
            time.sleep(1)
            claim_response = claim_game(token, game_response['gameId'], 2000)
            if claim_response is None:
                print(f"\r{Fore.RED+Style.BRIGHT}Gagal mengklaim game, mencoba lagi...", flush=True)

            while True:
                if claim_response.text == '{"message":"game session not finished"}':
                    time.sleep(1)  # Tunggu sebentar sebelum mencoba lagi
                    print(f"\r{Fore.RED+Style.BRIGHT}Game belum selesai.. mencoba lagi", flush=True)
                    claim_response = claim_game(token, game_response['gameId'], 2000)
                    if claim_response is None:
                        print(f"\r{Fore.RED+Style.BRIGHT}Gagal mengklaim game, mencoba lagi...", flush=True)
                elif claim_response.text == '{"message":"game session not found"}':
                    print(f"\r{Fore.RED+Style.BRIGHT}Game sudah berakhir", flush=True)
                    break
                else:
                    print(f"\r{Fore.YELLOW+Style.BRIGHT}Game selesai: {claim_response.text}", flush=True)
                    break
            refresh_response = refresh_token(token)
            print(f"\r{Fore.YELLOW+Style.BRIGHT}Refreshing token...", end="", flush=True)
            if refresh_response:
                token = refresh_response['refresh']  # Update token dengan yang baru
                print(f"\r{Fore.GREEN+Style.BRIGHT}Token refreshed.             ", flush=True)
            else:
                print(f"{Fore.RED+Style.BRIGHT}Token tidak diperbarui: {token}")
            # Setelah klaim game, cek lagi jumlah tiket
            balance_info = get_balance(token)  # Refresh informasi saldo untuk mendapatkan tiket terbaru
            if balance_info['playPasses'] > 0:
                print(f"\r{Fore.GREEN+Style.BRIGHT}Tiket masih tersedia, memainkan game lagi...", flush=True)
                continue  # Lanjutkan loop untuk memainkan game lagi
            else:
                print(f"\r{Fore.RED+Style.BRIGHT}Tidak ada tiket tersisa.", flush=True)
                break
     
       
    # Refresh token setelah semua token diproses
    updated_tokens = []
    print(f"\n{Fore.GREEN+Style.BRIGHT}========={Fore.WHITE+Style.BRIGHT}Semua akun berhasil di proses{Fore.GREEN+Style.BRIGHT}=========", end="", flush=True)
    print(f"\r\n\n{Fore.GREEN+Style.BRIGHT}Refreshing token...", end="", flush=True)
    for token in tokens:
        refresh_response = refresh_token(token)
        if refresh_response:
            updated_tokens.append(refresh_response['refresh'])
        else:
            print(f"{Fore.RED+Style.BRIGHT}Token tidak diperbarui: {token}")
    # Menulis kembali semua token ke file

    with open('token.txt', 'w') as file:
        for updated_token in updated_tokens:
            file.write(updated_token + '\n')
    import sys
    import time

    waktu_tunggu = 300  # 5 menit dalam detik
    for detik in range(waktu_tunggu, 0, -1):
        sys.stdout.write(f"\r{Fore.CYAN}Menunggu waktu claim berikutnya dalam {Fore.CYAN}{Fore.WHITE}{detik // 60} menit {Fore.WHITE}{detik % 60} detik")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rWaktu claim berikutnya telah tiba!                                      \n")
